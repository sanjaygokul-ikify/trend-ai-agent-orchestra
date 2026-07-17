class OrchestrationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class TaskExecutionError(OrchestrationError):
    def __init__(self, task_id: str, message: str):
        self.task_id = task_id
        super().__init__(f'Task {task_id} execution failed: {message}')


class EventHandlingError(OrchestrationError):
    def __init__(self, event_id: str, message: str):
        self.event_id = event_id
        super().__init__(f'Event {event_id} handling failed: {message}')