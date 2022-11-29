from niph import podcast_searchers


def test_reasonably_sized_query():
    searcher = podcast_searchers.KarpathyFridmanSearcher()
    results = searcher.search("artificial life")
    assert len(results) > 2 
