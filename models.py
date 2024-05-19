import random


class User:
    def __init__(self, name: str, choices: list):
        self.name = name
        self.choices = []
        self.stats = []

    def calculate_stats(self):
        self.stats.append(random.randint(8, 50))
        self.stats.append(random.randint(23, 400))
        self.stats.append(random.randint(2, 27))
        self.stats.append(random.randint(59, 100))
        self.stats.append(random.randint(6, 300))
        self.stats.append(random.randint(2, 25))
        self.stats.append(random.randint(19, 400))
        self.stats.append(random.randint(1, 14))
        self.stats.append(random.randint(60, 300))
        self.stats.append(random.randint(100, 600))
        self.stats.append(random.randint(30, 300))

        for stat in self.stats:
            pass
