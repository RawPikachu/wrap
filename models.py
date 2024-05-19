import random


class Person:
    def __init__(self, name: str, choices: list):
        self.name = name
        self.choices = []
        self.stats = {}

    def calculate_stats(self):
        self.stats["couch"] = random.randint(8, 51)
        self.stats["red_bull"] = random.randint(23, 401)
        self.stats["ankles"] = random.randint(2, 28)
        self.stats["HP"] = random.randint(59, 101)
        self.stats["clip"] = random.randint(6, 301)
        self.stats["shoulder"] = random.randint(2, 26)
        self.stats["french"] = random.randint(19, 401)
        self.stats["locations"] = random.randint(1, 15)
        self.stats["caps"] = random.randint(60, 301)
        self.stats["followers"] = random.randint(100, 601)
        self.stats["connection"] = random.randint(30, 301)

        for stat in self.stats:
            pass
