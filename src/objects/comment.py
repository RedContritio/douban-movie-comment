from datetime import time

class ShortComment:
    def __init__(self, movie_id: int, user_id: str, rate: float, time: time, content: str) -> None:
        self.movie_id = movie_id
        self.user_id = user_id
        self.rate = rate
        self.time = time
        self.content = content
    
    def __repr__(self) -> str:
        raise NotImplementedError('should return a csv row')