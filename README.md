# niph - needle in podcast haystack

## Tools for searching and text mining transcribed podcasts

ALL HAIL ANDREJ KARPATHY!

GLORY TO OpenAI WHISPER!

Long live Lex Fridman and his podcast!

Because of their effort it gets easier and faster to search and analyze transcribed podcasts.

This project is aiming to provide utils for searching transcribed podcast sites like [Karpathy's Lex Fridman Podcast transcriptions](https://karpathy.ai/lexicap/)

Supported podcasts:
- `LexFridmanPodcastRetriever` for searching [Lex Fridman AI Podcast](https://www.youtube.com/@lexfridman) based on Karpathy's transcription (also see [clips](https://www.youtube.com/@LexClips), although we do not support them yet)

### Usage

```
from niph import podcast_retrievers
retriever = podcast_retrievers.LexFridmanPodcastRetriever()

results = retriever.retrieve("search engines", max_results=2)
```

Returns results that rendered in HTML look something like this

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>episode</th>      <th>text</th>      <th>timestamp_link</th>      <th>distance</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>David Ferrucci: IBM Watson, Jeopardy &amp; Deep Conversations with AI | Lex Fridman Podcast #44</td>      <td>using open source search engines,</td>      <td>https://karpathy.ai/lexicap/0044-large.html#01:14:12.700</td>      <td>20.075276</td>    </tr>    <tr>      <th>1</th>      <td>David Ferrucci: IBM Watson, Jeopardy &amp; Deep Conversations with AI | Lex Fridman Podcast #44</td>      <td>and modified those search engines,</td>      <td>https://karpathy.ai/lexicap/0044-large.html#01:14:22.540</td>      <td>20.075276</td>    </tr>    <tr>      <th>2</th>      <td>Rajat Monga: TensorFlow | Lex Fridman Podcast #22</td>      <td>and many other search engines across the world.</td>      <td>https://karpathy.ai/lexicap/0022-large.html#01:05:57.500</td>      <td>17.332366</td>    </tr>    <tr>      <th>3</th>      <td>David Ferrucci: IBM Watson, Jeopardy &amp; Deep Conversations with AI | Lex Fridman Podcast #44</td>      <td>but we had a number of different search engines</td>      <td>https://karpathy.ai/lexicap/0044-large.html#01:14:16.100</td>      <td>17.332366</td>    </tr>    <tr>      <th>4</th>      <td>Brendan Eich: JavaScript, Firefox, Mozilla, and Brave | Lex Fridman Podcast #160</td>      <td>This is why a lot of the search engines</td>      <td>https://karpathy.ai/lexicap/0160-large.html#01:59:59.780</td>      <td>17.332366</td>    </tr>  </tbody></table>
