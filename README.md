# upsc-evaluator-ai
An AI-powered tool that evaluates UPSC Mains answers using GPT-4 and provides personalized, rubric-based feedback.

## Features

- Upload a text/image answer to a UPSC Mains question
- Get structured feedback (score, strengths, areas for improvement)
- Based on real model answers and UPSC grading guidelines
- Supports GS Papers and Essay Paper

## Tech Stack

- Python (FastAPI backend)
- OpenAI API (GPT-4-turbo)
- OCR (Tesseract or Google Vision API)
- Hosted on GCP/AWS (free tier)

## Contributing

PRs and suggestions welcome! Open an issue or contact us.

## License

MIT

## Setup

```bash
git clone https://github.com/aisailabs/upsc-evaluator-ai.git
cd upsc-evaluator-ai
cp .env.example .env
#Add your OpenAI key in .env
pip install -r requirements.txt
python backend/main.py

