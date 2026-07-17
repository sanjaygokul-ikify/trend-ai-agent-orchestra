class Metrics:
    def __init__(self):
        self.metrics = {}

    def increment(self, metric_name):
        if metric_name not in self.metrics:
            self.metrics[metric_name] = 0
        self.metrics[metric_name] += 1