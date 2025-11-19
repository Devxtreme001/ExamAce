# src/config.py
from dataclasses import dataclass

@dataclass
class Config:
    worker_model: str = "demo-llm"
    critic_model: str = "demo-critic"
    max_search_iterations: int = 3

config = Config()
