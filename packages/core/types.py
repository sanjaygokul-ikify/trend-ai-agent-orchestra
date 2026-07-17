from dataclasses import dataclass
from typing import List, Dict


class Event:
    def __init__(self, task_id: str, type: str):
        self.task_id = task_id
        self.type = type


class Task:
    def __init__(self, id: str, agent: 'Agent', data: Dict[str, str]):
        self.id = id
        self.agent = agent
        self.data = data


class Agent:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name