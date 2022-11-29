import abc
from typing import List


class BasePodcastSearcher(abc.ABC):
    def search(self, query: str, max_results: int = 10) -> List[dict]:
        pass
