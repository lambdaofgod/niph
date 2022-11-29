import re
from typing import List

from dataclasses import dataclass

from niph import podcast_searchers 


@dataclass
class KarpathyFridmanSearcher(podcast_searchers.DDGExternalSearcher):
    podcast_site_url: str = "https://karpathy.ai/lexicap/"

    def augmented_search(self, query: str, max_results: int = 10) -> List[dict]:
        """
        adds links with closest timestamps to search results
        """
        search_results = self.search(query, max_results)
        augmented_results = self.get_augmented_results(search_results)
        return augmented_results

    @classmethod
    def get_augmented_results(cls, search_results):
        for res in search_results:
            maybe_closest_entry_url = cls.get_closest_entry_url(
                res["href"], res["body"]
            )
            if maybe_closest_entry_url:
                res["link"] = maybe_closest_entry_url
        return search_results

    @classmethod
    def get_closest_entry_url(cls, podcast_link, text):
        """
        navigate to closest link found in `text`
        we can do this because Karpathy's site has links to sections indexed by timestamps
        """
        timestamp = cls.parse_timestamp(text)
        if timestamp:
            return f"{podcast_link}#{timestamp}"
        else:
            return None

    @classmethod
    def parse_timestamp(cls, text):
        """
        parse first occurence of timestamp from text
        inputs: text: str
        output: timestamp
        """
        timestamp = re.search(r"\d{2}:\d{2}:\d{2}.\d{3}", text)
        if timestamp:
            return timestamp.group(0)
        else:
            return None
