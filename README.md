# CAG Model — Cache-Augmented Generation

A minimal **Cache-Augmented Generation (CAG)** demo: instead of retrieving per query, a fixed context is loaded once and cached, then every question is answered by an LLM provided with that cached context — fast, deterministic answers over a known corpus.

## How it works

1. `context.txt` holds the knowledge base (loaded once).
2. The CLI builds a prompt = **cached context + question** and calls the [Sarvam AI](https://www.sarvam.ai/) chat API (`sarvam-m`).
3. Answers are generated strictly from the given context.

## Usage

```bash
pip install -r requirements.txt
python app.py
```

Set your Sarvam API key and it will answer questions over `context.txt` (type `exit` to quit).

## Requirements

`requests` only.

## License

No license specified — for learning/reference use.