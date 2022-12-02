import bs4
import requests
import os
import pandas as pd
import tqdm


def get_bsoup(link, sub_link=None):
    if sub_link:
        link = os.path.join(link, sub_link)
    page_contents = requests.get(link).text
    return bs4.BeautifulSoup(page_contents, features="lxml")


class FridmanKarpathyPodcastScraper:

    """
    Scrapes Karpathy's transcription of Lex Fridman Podcast.

    The resulting dataframe was uploaded to
    https://huggingface.co/datasets/lambdaofgod/lex_fridman_podcast
    """

    podcast_link = "https://karpathy.ai/lexicap/"

    def get_podcast_df(self):
        podcast_page = get_bsoup(self.podcast_link)
        subpage_links = self.get_subpage_links(podcast_page)
        episode_dfs = [
            self.scrape_episode(episode_relative_link)
            for episode_relative_link in tqdm.tqdm(subpage_links)
        ]
        return pd.concat(episode_dfs)

    def scrape(self) -> pd.DataFrame:
        pass

    def scrape_episode(self, episode_relative_link) -> pd.DataFrame:
        episode_link = os.path.join(self.podcast_link, episode_relative_link)
        episode_page = get_bsoup(episode_link)
        episode_name = episode_page.find_all("h2")[0].text
        html_rows = self.get_html_rows(episode_page)
        lines_df = pd.DataFrame.from_records(
            [self.parse_html_row(row, episode_link) for row in html_rows]
        )
        lines_df["episode"] = episode_name
        return lines_df[["episode", "text", "timestamp_link"]]

    @classmethod
    def get_subpage_links(cls, page):
        page_links = [elem["href"] for elem in page.find_all(href=True)]
        return [link for link in page_links if "html" in link and not "index" in link]

    @classmethod
    def get_html_rows(cls, subpage):
        html_rows = subpage.findAll("div", attrs={"class": "c"})
        return html_rows

    @classmethod
    def parse_html_row(cls, html_row, episode_link):
        timestamp = html_row.findAll(attrs={"class": "l"})[0]["id"]
        timestamp_link = episode_link + "#" + timestamp
        text_div = html_row.findAll("div", attrs={"class": "t"})
        if len(text_div) > 0:
            return {"text": text_div[0].text.strip(), "timestamp_link": timestamp_link}
        else:
            return {"text": None, "timestamp_link": None}
