from config.keywords import ALL_TOPICS, PAKISTAN_ENTITY_KEYWORDS

def filtering_and_tagging(articles):
    filtered_articles = [] 
    
    for article in articles:
        text = (article.get('title') + " " + article.get('body')).lower()

        if any(topic.lower() in text for topic in ALL_TOPICS):

            if any(entity.lower() in text for entity in PAKISTAN_ENTITY_KEYWORDS):
                article['region'] = "Pakistan"
            else:
                article['region'] = "Global"

            filtered_articles.append(article)

    return filtered_articles 