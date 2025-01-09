# Market Analysis Flow Project

This project implements an automated market analysis system using AI agents to perform comprehensive market research and analysis.

## Features

- Automated market analysis using specialized AI agents
- YAML configuration for agents and tasks
- Timestamped results storage
- Asynchronous execution support

## Project Structure

```
project/
├── src/
│   └── project/
│       ├── crew.py
│       └── market_flow.py
├── results/          # Analysis results in YAML format
├── .env             # Environment variables
├── pyproject.toml   # Project dependencies
└── README.md
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the market analysis:
```bash
python src/project/market_flow.py
```

The results will be saved in the `results` directory with timestamps.

## Configuration

The system uses specialized agents for different aspects of market analysis:
- Project Objectives Specialist
- Stakeholder Analyst
- Market Research Expert
- Project Planner
- And more...

Each analysis run generates a comprehensive YAML report including:
- Task definitions and outputs
- Agent configurations
- Analysis results

## License

MIT License
