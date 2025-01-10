from typing import Dict, Any
import yaml
from datetime import datetime
import json
import os

class ResultProcessor:
    def __init__(self, results_dir: str = "results"):
        self.results_dir = results_dir
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

    def process_result(self, result: str) -> Dict[str, Any]:
        """Process the raw YAML result and extract key metrics"""
        try:
            # Parse YAML content
            data = yaml.safe_load(result)
            
            # Extract metrics
            metrics = {
                "num_agents": len(data.get("config", {}).get("agents", [])),
                "num_tasks": len(data.get("config", {}).get("tasks", [])),
                "timestamp": datetime.now().isoformat()
            }
            
            # Save metrics
            self._save_metrics(metrics)
            
            return metrics
        except Exception as e:
            raise ValueError(f"Failed to process result: {str(e)}")

    def _save_metrics(self, metrics: Dict[str, Any]):
        """Save metrics to a separate file for tracking"""
        metrics_file = os.path.join(self.results_dir, "analysis_metrics.json")
        
        existing_metrics = []
        if os.path.exists(metrics_file):
            with open(metrics_file, 'r') as f:
                existing_metrics = json.load(f)
        
        existing_metrics.append(metrics)
        
        with open(metrics_file, 'w') as f:
            json.dump(existing_metrics, f, indent=2)
