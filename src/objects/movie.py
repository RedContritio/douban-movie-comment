class Movie:
    def __init__(self, id: int, title: str, rate: float):
        self.id = id
        self.title = title
        self.rate = rate
        assert(rate >= 0 and rate <= 10)
    