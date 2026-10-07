# Sarvam AI Python Samples

This project contains a few Python example scripts that use the Sarvam AI SDK to test text translation and text-to-speech features.

## Overview

The repository currently includes:

- `sarvam_ai.py` — sample translation example to Gujarati
- `stt.py` — sample translation example to Hindi
- `tts.py` — sample text-to-speech generation in Hindi
- `requirements.txt` — Python dependencies

These scripts are simple SDK demos and are useful for learning how to authenticate and call the Sarvam AI APIs.

## Prerequisites

- Python 3.9+
- A valid Sarvam AI API key
- Internet access to call the API

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root with your Sarvam API key:

```env
sarvam_api_key=YOUR_API_KEY_HERE
```

The scripts use `python-dotenv` to load this value automatically.

## Project Files

### `sarvam_ai.py`

Translates a sample English sentence into Gujarati using the Sarvam AI translation API.

```python
response = client.text.translate(
    input="Hi, My Name is Durga Prasad, iam a Fullstack developer.",
    source_language_code="auto",
    target_language_code="gu-IN",
    speaker_gender="Male"
)
```

### `stt.py`

Translates a sample English sentence into Hindi.

```python
response = client.text.translate(
    input="Hello, how are you?",
    source_language_code="auto",
    target_language_code="hi-IN",
    speaker_gender="Male"
)
```

### `tts.py`

Converts a text string to Hindi speech using the Sarvam AI text-to-speech API.

```python
response = client.text_to_speech.convert(
    text="Hi, My Name is Durga Prasad, iam a Fullstack developer.?",
    target_language_code="hi-IN",
)
```

## Running the Examples

Run each script individually:

```bash
python sarvam_ai.py
python stt.py
python tts.py
```

The scripts print the API response returned by Sarvam AI.

## Notes

- The code is intentionally minimal and demonstrates direct SDK usage.
- The scripts assume your `.env` file is available in the same directory as the Python files.
- If the API key is missing or invalid, the SDK call will fail.
- The repository is a sample/testing setup rather than a production-ready application.

## Dependencies

The current dependencies are:

```txt
dotenv
sarvamai
```

## License

This project does not currently include a license file. Add one if you plan to publish or distribute it.
