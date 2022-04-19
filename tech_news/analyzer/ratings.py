from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
