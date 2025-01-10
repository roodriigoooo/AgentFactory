import pytest
import os
import yaml
from src.project.market_flow import MarketAnalysisFlow
from src.project.processors.result_processor import ResultProcessor

@pytest.fixture
def market_flow():
    return MarketAnalysisFlow()

@pytest.fixture
def result_processor():
    return ResultProcessor("test_results")

def test_result_processor_metrics(result_processor):
    sample_result = """
    config:
      agents:
        - role: "Market Research Expert"
          goal: "Conduct market research"
      tasks:
        - description: "Analyze market trends"
          expected_output: "Market trends report"
    """
    
    metrics = result_processor.process_result(sample_result)
    assert metrics["num_agents"] == 1
    assert metrics["num_tasks"] == 1
    assert "timestamp" in metrics

@pytest.mark.asyncio
async def test_market_flow_initialization(market_flow):
    assert os.path.exists(market_flow.results_dir)
    assert hasattr(market_flow, "state")
    assert hasattr(market_flow, "result_processor")
