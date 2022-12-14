# GPT-3 IPython Bot
[![Docker Pulls](https://img.shields.io/docker/pulls/dmnkss/gpt3-ipython-bot)](https://hub.docker.com/r/dmnkss/gpt3-ipython-bot)

A bot that searches for answers to questions using IPython commands.
Inspired by https://twitter.com/goodside/status/1581805503897735168

[![asciicast](https://asciinema.org/a/Zi7Mn2si2nRyKV5Fw6R3WW3aQ.svg)](https://asciinema.org/a/Zi7Mn2si2nRyKV5Fw6R3WW3aQ)
___
# Do not use this in production
This is a proof of concept and should not be used in production. It is not secure and can be used to execute arbitrary code on your machine. It is also not optimized for performance and will be slow.
___

Sorry for dirty code.

## Usage
You can to specify OpenAI API token in
- Argument `--openai_token`
- Environment variable `OPENAI_API_KEY`

Cost per 1000 tokens is 0.02 USD by default. You can change it with `--cost_per_1000_tokens`.

### Python
```bash
pip install -r requirements.txt
python cli.py "Your question" [--max_iterations=5] [--openai_token] [--cost_per_1000_tokens]
```
### Docker
```bash
docker run dmnkss/gpt3-ipython-bot "Your question" [--max_iterations=5] [--openai_token] [--cost_per_1000_tokens]
```
