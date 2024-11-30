from typing import List, Tuple
from datetime import datetime, timedelta

class Movie:
    def __init__(self, name: str, dates: List[Tuple[datetime, datetime]]):
        self.name = name
        self.dates = dates

    def schedule(self) -> List[str]:
        res = []
        for interval in self.dates:
            d1, d2 = interval
            diff = (d2 - d1).days
            for day in range(diff + 1):
                res.append(str(d1+timedelta(days=day)))
        return res
    

dates = [(datetime(2024,11,1), datetime(2024,11,7)), 
         (datetime(2024,12,15),datetime(2024,12,31))]

movie = Movie("fasfsaf", dates)
print("\n".join(movie.schedule()))