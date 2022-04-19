from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()
    news_find = []
    for new in news:
        new["popularity"] = new['comments_count'] + new['shares_count']
    news_sorted = sorted(
        news, key=lambda i: (i["popularity"], i["title"]), reverse=True
    )
    for new in news_sorted[:5]:
        news_find.append((new["title"], new["url"]))

    return news_find


# Requisito 11
def top_5_categories():
    news = find_news()
    categories_list = []
    for new in news:
        categories_list.extend(new['categories'])
    categories = sorted([
        *Counter(category for category in categories_list).keys()])[:5]
    return categories
