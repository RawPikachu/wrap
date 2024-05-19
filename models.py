import random

TRANSLATION = {
    "pepper": 0,
    "eggplant": 1,
    "turnips": 2,
    "pumpkin": 3,
    "potato": 4,
    "tomato": 5,
    "pea": 6,
    "onion": 7,
    "lettuce": 8,
}


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

        # Give random modification to stats based on choices
        for choice in self.choices:
            self.stats[TRANSLATION[choice] + 1] = int(self.stats[TRANSLATION[choice] + 1] * random.uniform(1.0, 10.0))
