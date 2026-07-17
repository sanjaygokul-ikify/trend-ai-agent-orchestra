import unittest
from packages.core import Engine, Task, Agent, Event
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_orchestrator_start(self):
        orchestrator = Orchestrator()
        orchestrator.start()
        self.assertEqual(orchestrator.engine.task_queue, [])
        self.assertEqual(orchestrator.engine.event_bus, [])