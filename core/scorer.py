from config.keywords import MUST_READ_TOPICS

def score_articles(articles):

    for article in articles:
        score = 0
        title = article.get("title", "").lower()
        body = article.get("body", "").lower()

        for topic in MUST_READ_TOPICS:
            topic = topic.lower()

            if topic in title:
                score += 5
            if topic in body:
                score += body.count(topic) * 1
        
        article['score'] = score
    return articles