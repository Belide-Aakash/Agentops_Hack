import requests 
from bs4 import BeautifulSoup

# API URL for RSS feed (Replace this with the actual URL)
rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"

def rss_extract(top_n):
    # Make a GET request to fetch the RSS data
    response = requests.get(rss_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the RSS feed
        soup = BeautifulSoup(response.text, "xml")

        # Extract all articles
        articles = []
        for item in soup.find_all("item"):
            title = item.find("title").text if item.find("title") else "No Title"
            link = item.find("link").text if item.find("link") else "No Link"
            creator = item.find("dc:creator").text if item.find("dc:creator") else "No Creator"
            pub_date = item.find("pubDate").text if item.find("pubDate") else "No Publication Date"

            articles.append({
                "title": title,
                "link": link,
                "creator": creator,
                "pub_date": pub_date
            })

        # Print extracted data
        # for article in articles:
        #     print(article)
        return articles[:min(top_n, len(articles))]

    else:
        print(f"Failed to fetch RSS feed. Status code: {response.status_code}")
        return []
    