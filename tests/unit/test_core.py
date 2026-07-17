import unittest
from packages.core import Engine, Task, Agent, Event

class TestCore(unittest.TestCase):
    def test_task_creation(self):
        agent = Agent('1', 'agent1')
        task = Task('1', agent, {'key': 'value'})
        self.assertEqual(task.id, '1')
        self.assertEqual(task.agent.id, '1')
        self.assertEqual(task.data, {'key': 'value'})

    def test_event_creation(self):
        event = Event('1', 'type1')
        self.assertEqual(event.task_id, '1')
        self.assertEqual(event.type, 'type1')

    def test_engine_creation(self):
        engine = Engine([], [], {})
        self.assertEqual(engine.task_queue, [])
        self.assertEqual(engine.event_bus, [])
        self.assertEqual(engine.consensus_store, {})