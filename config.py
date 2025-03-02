import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "microsoft/DialoGPT-medium")
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
print(OPENAI_API_KEY)