from findkit import indexes
import datasets


class LexFridmanPodcastRetriever:
    """
    Search Karpathy's transcription of Lex Fridman Podcast
    """

    def __init__(self):
        podcast_dataset = datasets.load_dataset("lambdaofgod/lex_fridman_podcast")[
            "train"
        ]
        df = podcast_dataset.to_pandas().dropna()
        self.index = indexes.InMemoryBM25Index.build(df["text"], df)

    def retrieve(self, query, n_lines=10):
        """
        Retrieve dataframe with lines containing:
        - episode name
        - line text
        - link with line timestamp (can navigate to transcription page)
        - bm25 score that measures similarity with query
        """
        results_df = self.index.find_similar(query, n_returned=n_lines)
        return results_df.rename({"distance": "bm25_score"}, axis=1).reset_index(drop=True)
