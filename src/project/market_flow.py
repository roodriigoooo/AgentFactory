from typing import Optional
from datetime import datetime
import os
import asyncio
import logging
import yaml
import json
from processors.result_processor import ResultProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MarketAnalysisResult:
    def __init__(self):
        self.analysis = ""
        self.metrics = {}

    def to_dict(self):
        return {
            "analysis": self.analysis,
            "metrics": self.metrics
        }

class MarketAnalysisFlow:
    def __init__(self):
        self.base_results_dir = "results"
        if not os.path.exists(self.base_results_dir):
            os.makedirs(self.base_results_dir)
        self.state = MarketAnalysisResult()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results_dir = os.path.join(self.base_results_dir, self.timestamp)
        os.makedirs(self.results_dir)
        
        # Load agent configurations
        self.agent_config = self._load_agent_config()

    def _load_agent_config(self):
        config_path = os.path.join("config", "agent_config.yaml")
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.warning(f"Failed to load agent config: {str(e)}")
            return {}

    async def run_market_analysis(self):
        try:
            from crew import MarketAnalysisFlow
            logger.info("Starting market analysis...")
            
            # Initialize flow with configurations
            flow = MarketAnalysisFlow()
            result = flow.kickoff()
            
            # Process result
            result_str = str(result)
            if result_str.startswith("```yaml\n"):
                result_str = result_str[8:]
            if result_str.endswith("```"):
                result_str = result_str[:-3]
            
            # Process and store metrics
            data = yaml.safe_load(result_str)
            metrics = {
                "num_agents": len(data.get("config", {}).get("agents", [])),
                "num_tasks": len(data.get("config", {}).get("tasks", [])),
                "timestamp": datetime.now().isoformat()
            }
            
            self.state.metrics = metrics
            self.state.analysis = result_str
            
            logger.info("Market analysis completed successfully")
            return result_str
            
        except Exception as e:
            logger.error(f"Error in market analysis: {str(e)}")
            raise

    async def save_results(self, result):
        try:
            # Save analysis YAML
            analysis_file = os.path.join(self.results_dir, "analysis.yaml")
            with open(analysis_file, 'w') as f:
                f.write(result)
            
            # Save state JSON
            state_file = os.path.join(self.results_dir, "result.json")
            with open(state_file, 'w') as f:
                json.dump(self.state.to_dict(), f, indent=2)
            
            logger.info(f"Analysis completed and saved to: {self.results_dir}")
            logger.info("*" * 100)
            logger.info("Market Analysis Complete!")
            
            return self.results_dir
            
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            raise

    async def run(self):
        try:
            result = await self.run_market_analysis()
            await self.save_results(result)
        except Exception as e:
            logger.error(f"Flow execution failed: {str(e)}")
            raise

async def main():
    try:
        flow = MarketAnalysisFlow()
        await flow.run()
    except Exception as e:
        logger.error(f"Main execution failed: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
