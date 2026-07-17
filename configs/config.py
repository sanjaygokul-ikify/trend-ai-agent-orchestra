import logging
from typing import Dict

class Config:
    def __init__(self, config_dict: Dict[str, str]):
        self.config_dict = config_dict
        self.logger = logging.getLogger(__name__)

    def get_config(self, key: str) -> str:
        try:
            return self.config_dict[key]
        except KeyError:
            self.logger.error(f'Config key {key} not found')
            raise ValueError(f'Config key {key} not found')
