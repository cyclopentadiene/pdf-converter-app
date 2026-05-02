# PDF to Markdown Converter

A lightweight desktop application that converts PDF files to Markdown format, preserving text, tables, images, and page boundaries.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)

## Features

- **One-click conversion** — Select a PDF, choose where to save, done
- **Page-preserving** — Each PDF page becomes a `## Page N` section in Markdown
- **Image extraction** — Embedded images are saved to a companion `_images/` folder
- **Table support** — Tables are converted to Markdown table syntax
- **Native desktop GUI** — Runs as a standalone macOS app (no terminal needed)

## Installation

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Install dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install pymupdf4llm
```

### Run the app

```bash
python pdf2md.py
```

### Build a standalone macOS app (optional)

```bash
# Install build dependencies
uv sync --extra build

# Build with PyInstaller
pyinstaller "PDF Converter.spec"
```

The built app will be in `dist/PDF Converter.app`.

## Usage

1. Launch the app (`python pdf2md.py` or open the built `.app`)
2. Click **"Select PDF & Convert"**
3. Choose your input PDF file
4. Choose where to save the output `.md` file
5. Wait for the conversion to complete
6. Images are saved alongside in a `{filename}_images/` folder

## How It Works

Under the hood, this uses [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) — a library built on MuPDF that extracts structured content from PDFs optimized for LLM consumption. It handles:

- Text extraction with layout preservation
- Image extraction and referencing in Markdown
- Table detection and Markdown table generation
- Page-by-page chunking

## License

This project is licensed under the [MIT License](LICENSE).
