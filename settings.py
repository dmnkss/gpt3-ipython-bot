import os

from prompt import PROMPT


class Settings:
    PROMPT = PROMPT
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    MODEL_COST_DOLLARS = os.environ.get('MODEL_COST_DOLLARS', 0.02)


settings = Settings()
