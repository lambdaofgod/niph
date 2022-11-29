# niph - needle in podcast haystack

## Tools for searching and text mining transcribed podcasts

HAIL ANDREJ KARPATHY!

GLORY TO OpenAI WHISPER!

Long live Lex Fridman and his podcast!

Because of their effort it gets easier and faster to search and analyze transcribed podcasts.

This project is aiming to provide utils for searching transcribed podcast sites like [Karpathy's Lex Fridman Podcast transcriptions](https://karpathy.ai/lexicap/)

Supported podcasts:
- `KarpathyFridmanSearcher` for searching [Lex Fridman AI Podcast](https://www.youtube.com/@lexfridman) based on Karpathy's transcription (also see [clips](https://www.youtube.com/@LexClips), although we do not support them yet)

### Usage

```
import pprint
from niph import podcast_searchers
searcher = podcast_searchers.KarpathyFridmanSearcher()

results = searcher.search("machine learning", max_results=2)
>>> pprint.pprint(results)
[{'body': 'Lexicap: Lex Fridman Podcast Whisper captions. These are '
          'transcripts for Lex Fridman episodes. First we get all the episodes '
          'in the playlist (ty youtubesearchpython ), see their docs. Then we '
          'download the audio for all of them (ty yt-dlp ): yt-dlp -x '
          '--audio-format mp3 -o {mp3_file} -- {youtube_video_id}',
  'href': 'https://karpathy.ai/lexicap/',
  'title': 'Lexicap: Lex Fridman Podcast Whisper captions - karpathy.ai'},
 {'body': 'The machine learning person says, look, my algorithm does well on '
          'the. link | 01:17:20.240. test set. And its a clean test set. I '
          'didnt peek. And the machine in the business person says, link | '
          '01:17:25.440. thank you very much, but your algorithm sucks. It '
          'doesnt work. And the machine learning person ...',
  'href': 'https://karpathy.ai/lexicap/0073-small.html',
  'title': 'Lexicap - karpathy.ai'}]
```

*The KarpathyFridmanSearcher also supports augmented search that makes navigating website easier. It adds link field that links to closest found Karpathy's site link with timestamp. Be aware though that these links are addded from the text responses from search engine, so they will not be available for all records though.*

```
results = searcher.augmented_search("machine learning", max_results=2)
>>> pprint.pprint(results)
[{'title': 'Lexicap', 'href': 'https://karpathy.ai/lexicap/0040-large.html', 'body': 'Regina Barzilay: Deep Learning for Cancer Diagnosis and Treatment | Lex Fridman Podcast #40. When broadly, before we talk about how machine learning'},
pprint.pprint(searcher.augmented_search("machine learning")[:2])
[{'body': 'Lexicap: Lex Fridman Podcast Whisper captions. These are '
          'transcripts for Lex Fridman episodes. First we get all the episodes '
          'in the playlist (ty youtubesearchpython ), see their docs. Then we '
          'download the audio for all of them (ty yt-dlp ): yt-dlp -x '
          '--audio-format mp3 -o {mp3_file} -- {youtube_video_id}',
  'href': 'https://karpathy.ai/lexicap/',
  'title': 'Lexicap: Lex Fridman Podcast Whisper captions - karpathy.ai'},
 {'body': 'The machine learning person says, look, my algorithm does well on '
          'the. link | 01:17:20.240. test set. And its a clean test set. I '
          'didnt peek. And the machine in the business person says, link | '
          '01:17:25.440. thank you very much, but your algorithm sucks. It '
          'doesnt work. And the machine learning person ...',
  'href': 'https://karpathy.ai/lexicap/0073-small.html',
  'link': 'https://karpathy.ai/lexicap/0073-small.html#01:17:20.240',
  'title': 'Lexicap - karpathy.ai'}]
```
