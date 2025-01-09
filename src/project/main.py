#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
from project.crew import MarketAnalysisFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def main():
    """Main function to execute the market analysis flow"""
    flow = MarketAnalysisFlow()
    result = flow.kickoff()
    
    print("\n=== Flow Execution Complete ===")
    print("Results:", result)

if __name__ == "__main__":
    main()