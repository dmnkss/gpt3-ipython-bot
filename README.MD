# GPT-3 IPython Bot

A bot that searches for answers to questions using IPython commands.
Inspired by https://twitter.com/goodside/status/1581805503897735168
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
docker-compose build
docker-compose run app "Your question" [--max_iterations=5] [--openai_token] [--cost_per_1000_tokens]
```
