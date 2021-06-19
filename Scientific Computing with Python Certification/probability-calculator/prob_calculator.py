import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, values in kwargs.items():
            for n in range(values):
                self.contents.append(key)
        self.total = self.contents.copy()

    def draw(self, n):
        self.contents = self.total.copy()
        if n > len(self.contents):
            give = self.contents.copy()
        else:
            give = random.sample(self.contents, k=n)
        for i in give:
            self.contents.remove(i)
        return give


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = []
    for _ in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if result.count(key) < value:
                success = False
        if success:
            results.append(True)
    return sum(results) / num_experiments
