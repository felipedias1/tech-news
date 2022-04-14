import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    info = selector.css(
        "h3.tec--card__title a::attr(href)"
    ).getall()
    return info


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    link = selector.css(
        ".tec--list.tec--list--lg > a::attr(href)"
    ).get()
    return link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    link = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    time_stamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get().strip()
    shares_count = selector.css("div.tec--toolbar__item::text").get()
    if shares_count:
        shares_count = shares_count.strip()
        shares_count = int(shares_count[0])
    else:
        shares_count = 0
    comments = selector.css("#js-comments-btn::attr(data-count)").get().strip()
    summary = selector.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = "".join(summary)
    new_sources = []
    sources = selector.css("div.z--mb-16 a::text").getall()
    for source in sources:
        new_sources.append(source.strip())
    categories = selector.css("div#js-categories > a::text").getall()
    new_categories = []
    for category in categories:
        new_categories.append(category.strip())
    new_info = {
        "url": link,
        "title": title,
        "timestamp": time_stamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": int(comments),
        "summary": summary,
        "sources": new_sources,
        "categories": new_categories,
    }
    return new_info


# Requisito 5
def get_tech_news(amount):
    data = fetch("https://www.tecmundo.com.br/novidades")
    news_links = scrape_novidades(data)

    while len(news_links) < amount:
        link = scrape_next_page_link(data)
        data = fetch(link)
        more_news = scrape_novidades(data)
        news_links.extend(more_news)

    news_data = []
    for link in news_links[:amount]:
        data = fetch(link)
        news_data.append(scrape_noticia(data))

    create_news(news_data)
    return news_data
