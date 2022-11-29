# niph - needle in podcast haystack

## Tools for searching and text mining transcribed podcasts

This project is aiming to provide utils for searching transcribed podcast sites like [Karpathy's Lex Fridman Podcast transcriptions](https://karpathy.ai/lexicap/)

Supported podcasts:
- `KarpathyFridmanSearcher` for searching [Lex Fridman AI Podcast](https://www.youtube.com/@lexfridman) based on Karpathy's transcription (also see [clips](https://www.youtube.com/@LexClips), although we do not support them yet)

### Usage

```
from niph import podcast_searchers
searcher = podcast_searchers.KarpathyFridmanSearcher()

>>> searcher.search("machine learning")
[{'title': 'Lexicap: Lex Fridman Podcast Whisper captions - karpathy.ai', 'href': 'https://karpathy.ai/lexicap/', 'body': 'Lexicap: Lex Fridman Podcast Whisper captions. These are transcripts for Lex Fridman episodes. First we get all the episodes in the playlist (ty youtubesearchpython ), see their docs. Then we download the audio for all of them (ty yt-dlp ): yt-dlp -x --audio-format mp3 -o {mp3_file} -- {youtube_video_id}'}, {'title': 'Lexicap - karpathy.ai', 'href': 'https://karpathy.ai/lexicap/0073-small.html', 'body': 'The machine learning person says, look, my algorithm does well on the. link | 01:17:20.240. test set. And its a clean test set. I didnt peek. And the machine in the business person says, link | 01:17:25.440. thank you very much, but your algorithm sucks. It doesnt work. And the machine learning person ...'} ...
```

*The KarpathyFridmanSearcher also supports augmented search that makes navigating website easier. It adds link field that links to closest found Karpathy's site link with timestamp. Be aware though that these links are addded from the text responses from search engine, so they will not be available for all records though.*

```
>>> searcher.augmented_search("machine learning")
[{'title': 'Lexicap', 'href': 'https://karpathy.ai/lexicap/0040-large.html', 'body': 'Regina Barzilay: Deep Learning for Cancer Diagnosis and Treatment | Lex Fridman Podcast #40. When broadly, before we talk about how machine learning'}, {'title': 'Lexicap', 'href': 'https://karpathy.ai/lexicap/0056-large.html', 'body': '00:22:41.520. None of the machine learning people clevered you? 00:25:59.840. much of the machine learning world has not considered.', 'link': 'https://karpathy.ai/lexicap/0056-large.html#00:22:41.520'}, {'title': 'Lexicap', 'href': 'https://karpathy.ai/lexicap/0224-small.html', 'body': 'NumPy formed the foundation of tensor based machine learning in Python, SciPy formed. Like its so critical to our prosperity and that were, were dangerously not learning.'}...
```

## Ideas 

HAIL ANDREJ KARPATHY!
GLORY TO OpenAI WHISPER!
Long live Lex Fridman and his podcast!

Because of their effort it will be easy to search and analyze transcribed podcasts.
