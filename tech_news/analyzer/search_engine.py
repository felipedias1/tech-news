from datetime import datetime
from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    news = find_news()
    news_find = []
    for new in news:
        if new["title"].lower() == title.lower():
            news_find.append((new["title"], new["url"]))
    return news_find


# Requisito 7
def search_by_date(date):
    news = find_news()
    news_find = []
    try:
        datetime.strptime(date, '%Y-%m-%d')
        for new in news:
            data_atual = datetime.strptime(
                (new["timestamp"])[:10], '%Y-%m-%d'
            ).date()
            if str(data_atual) == date:
                news_find.append((new["title"], new["url"]))
        return news_find
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = find_news()
    news_find = []
    for new in news:
        for item in new["sources"]:
            if source.lower() == item.lower():
                news_find.append((new["title"], new["url"]))
    return news_find


# Requisito 9
def search_by_category(category):
    news = find_news()
    news_find = []
    for new in news:
        for item in new["categories"]:
            if category.lower() == item.lower():
                news_find.append((new["title"], new["url"]))
    return news_find
