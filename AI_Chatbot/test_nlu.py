from pyvi import ViTokenizer, ViPosTagger

print(ViTokenizer.tokenize("Học viện kỹ thuật quân sự"))
print(ViPosTagger.postagging(ViTokenizer.tokenize("Tôi muốn đi chơi công viên nước")))

import feedparser

NewsFeed = feedparser.parse("https://www.shb.com.vn/feed/")
entry = NewsFeed.entries[1]

print(entry.title)