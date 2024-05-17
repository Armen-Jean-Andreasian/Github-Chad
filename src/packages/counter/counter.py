class Count:
    def __init__(self):
        self.count = 0

    def increase_by_one(self):
        self.count += 1
        return self

    def __lt__(self, other: int) -> bool:
        """Less than other"""
        return self.count < other

    @property
    def result(self):
        return self.count

    @result.setter
    def result(self, count: int):
        self.count = count

    def reset(self):
        self.count = 0
        return self
