# python-web-scraper

## Command for crawling and saving results to file
- scrapy runspider wikipedia.py -o article.xml -t xml -s CLOSESPIDER_PAGECOUNT=10
- scrapy runspider wikipedia.py -o article.xml -t xml
- scrapy runspider wikipedia.py -s FEED_URI=article.json -s FEED_FORMAT=json
- scrapy runspider wikipedia.py

Also in the .py file you can customize the save output settings using

```json

{
    FEED_URI="article.csv",
    FEED_FORMAT="csv"
}

```
