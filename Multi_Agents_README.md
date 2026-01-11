# Deep Research Agent Implementation

Implementation code for the paper "Optimizing Cross-Functional Decision Intelligence Through Deep Research Agent Architectures" by Singh & Vakkalagadda (2026).

## Overview

This repository contains the implementation of three analytical synthesis approaches:
1. Traditional Manual Analysis (baseline)
2. Multi-Agent Coordination System (predetermined protocols)
3. Deep Research Agent (adaptive planning with reflection)

## Requirements

Python 3.8+
OpenAI API key
Required packages listed in requirements.txt

## Installation
```bash
pip install openai pandas numpy python-dotenv
```

## Dataset

Download the Superstore dataset from Zenodo:
DOI: 10.5281/zenodo.18049149
URL: https://doi.org/10.5281/zenodo.18049149

Place the dataset in the `data/` directory.

## Usage

### Set up your OpenAI API key

Create a `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

### Run Deep Research Agent
```python
from deep_research_agent import DeepResearchAgent

agent = DeepResearchAgent(
    model="gpt-4-turbo-2024-04-09",
    temperature=0.2
)

query = "Why is Technology category profit declining in West region despite increasing sales?"
result = agent.analyze(query, data_path="data/superstore.csv")
```

## Replication

Setup time: ~15 minutes
Cost: ~$38 in API fees for N=120 queries
Expected results: 93% analytical accuracy, 33.8 minutes average completion time

## Citation

If you use this code, please cite:
```
Singh, A. P., & Vakkalagadda, R. (2026). Optimizing Cross-Functional Decision Intelligence 
Through Deep Research Agent Architectures. RSS: Data Science and Artificial Intelligence.
```

## License

MIT License

## Contact

Arun Pratap Singh: asingh09894@ucumberlands.edu
```

