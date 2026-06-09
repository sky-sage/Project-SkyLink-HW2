# Project SkyLink

Project SkyLink is an AI-powered requirements analysis platform for aircraft and Flight Management System (FMS) documentation. Using local LLMs, it extracts semantic information from requirements, generates structured JSON logs, classifies them into subsystem hierarchies, and visualizes relationships through interactive HTML graphs.

## Team
- Akashneel Bhattacharya 
- Samarth S Sastry
- Aayush Shah
- Rane Rushil Devendra

## Usage

Generate semantic requirement logs:

```bash
python3 main.py
```

Generate hierarchy classification and visualization:

```bash
python3 hierarchy_llm.py
```

## Prerequisites
- Python 3
- Ollama
- `deepseek-r1:1.5b`

## Repository Notes
- `DP5_datasets/` contains synthetic logs generated from `main.py`.
- Aircraft certification PDFs are provided as source documents.
- Existing datasets may be reused, but fresh log generation is recommended.

## Future Work
- Improved clustering and hierarchy generation
- Interactive web interface
- OCR-based PDF extraction
- Confidence-based node coloring
- Hoverable cluster information
- Additional analytics and presentation materials
