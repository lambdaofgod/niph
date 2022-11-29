from typing import List

from dataclasses import dataclass
from duckduckgo_search import ddg

from niph import podcast_searchers


@dataclass
class DDGExternalSearcher(podcast_searchers.BasePodcastSearcher):
    podcast_site_url: str

    def search(self, query: str, max_results: int = 10) -> List[dict]:
        return ddg(self.get_search_query(query))[:max_results]

    def get_search_query(self, query: str):
        return f'site:"{self.podcast_site_url}" "{query}"'
