# Setup Guide

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/asingh122/deep_research_agent.git
cd deep_research_agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download dataset
Download from https://doi.org/10.5281/zenodo.18049149
Place in `data/superstore.csv`

### 4. Configure API key
Create `.env` file:
```
OPENAI_API_KEY=your_key_here
```

### 5. Run example
```bash
python deep_research_agent.py
```

## Expected Results

Analytical Accuracy: 93%
Average Completion Time: 33.8 minutes
Information Coverage: 94%
Average Iterations: 4.2 (SD=1.7)

## Cost Estimation

Single query: ~$0.32 in API fees
Full replication (N=120): ~$38

## Troubleshooting

**API Rate Limits**: Add delays between requests
**Memory Issues**: Process queries in batches
**Dataset Not Found**: Verify path in `data/` directory
```

---

### **STEP 5: VERIFY YOUR REPOSITORY**

Your repository should now have this structure:
```
deep_research_agent/
├── README.md
├── requirements.txt
├── deep_research_agent.py
├── SETUP_GUIDE.md
├── data/
│   └── .gitkeep
├── .gitignore
└── LICENSE
