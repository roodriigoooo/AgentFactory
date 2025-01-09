from typing import Optional
from datetime import datetime
from pydantic import BaseModel
import os
import asyncio

class MarketAnalysisResult(BaseModel):
    analysis: str = ""

class MarketAnalysisFlow:
    def __init__(self):
        self.results_dir = "results"
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
        self.state = MarketAnalysisResult()

    async def run_market_analysis(self):
        from crew import MarketAnalysisFlow
        result = MarketAnalysisFlow().kickoff()
        # Remove the ```yaml and ``` markers from the result
        result_str = str(result)
        if result_str.startswith("```yaml\n"):
            result_str = result_str[8:]
        if result_str.endswith("\n```"):
            result_str = result_str[:-4]
        self.state.analysis = result_str
        return result_str

    async def save_results(self, result):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"market_analysis_{timestamp}.yaml"
        filepath = os.path.join(self.results_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(result)
        
        print(f"Analysis completed and saved to: {filepath}")
        print("*" * 100)
        print("Market Analysis Complete!")
        return filepath

    async def run(self):
        result = await self.run_market_analysis()
        await self.save_results(result)

async def main():
    flow = MarketAnalysisFlow()
    await flow.run()

if __name__ == "__main__":
    asyncio.run(main())
