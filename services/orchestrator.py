from packages.core import Engine
from packages.utils import logging

class Orchestrator:
    def __init__(self):
        self.logger = logging.setup_logging()
        self.engine = Engine([], [], {})

    def start(self):
        self.logger.info('Orchestrator started')
        self.engine.run()
        self.logger.info('Orchestrator finished')