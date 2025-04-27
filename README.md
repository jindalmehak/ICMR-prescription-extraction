# ICMR Prescription Extraction

## Overview
This project extracts structured data from handwritten medical prescriptions using a multimodal LLM (Donut model).

## Structure
- `models/`: Multimodal model extraction
- `utils/`: Postprocessing and evaluation utilities
- `data/`: Sample data
- `notebooks/`: EDA and experimentation
- `main.py`: Main execution script

## Model
- **Donut Model**: Fine-tuned on document understanding tasks (docVQA).
- **Huggingface Model Name**: `naver-clova-ix/donut-base-finetuned-docvqa`

## Evaluation
- Field-level F1 Score
- Edit Distance
