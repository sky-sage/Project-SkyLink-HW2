# Project Handover

This project performs semantic analysis of aircraft/FMS requirements using local LLMs. `main.py` parses requirements and generates structured JSON logs via DeepSeek-R1. `hierarchy_llm.py` classifies those logs into subsystem hierarchies and exports an HTML visualization.

Run:

```bash
python3 main.py
python3 hierarchy_llm.py
```

Ensure Ollama and `deepseek-r1:1.5b` are installed before execution.


DP5_datasets -> all synthetic data
logs -> pregenerated from main.py, can reuse but generate freshly from main.py instead
pdfs -> TRUE CERTIFICATIONS for different aircrafts
mvp2 -> containers log generator
mvp2 -> graph gen -> attempt at creating pictorial plots (samarth to make two charts)

TODO:
iv) MAKE PROPER CLUSTERS
i) make website for interactive session
ii) attempt ocr for pdfs reading and extraction
iii) make ppt 

nice to have: 
i) hover mode: gives info about that cluster
ii) node colour CONFIDENCE SCORE: rates how much the req actually belongs to the cluster
    (0-> 1, red -> blue)