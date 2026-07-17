import unittest
from packages.core import Engine

class TestRuntime(unittest.TestCase):
    def test_engine_run(self):
        engine = Engine([], [], {})
        engine.run()
        self.assertEqual(engine.task_queue, [])
        self.assertEqual(engine.event_bus, [])