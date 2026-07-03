import requests
from bs4 import BeautifulSoup
from loguru import logger
import re

def scrape_propakistani():

    articles_data = []
    page = 1
    keep_scraping = True

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    logger.info("Starting ProPakistani scrape...")

    while keep_scraping:

        url = f"https://propakistani.pk/category/tech-and-telecom/page/{page}/" if page > 1 else "https://propakistani.pk/category/tech-and-telecom/"
        logger.debug(f"Fetching page {page}: {url}")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')

            target_div = soup.find('div', class_= "col-md-8 content-area", id= "primary")
            if not target_div:
                logger.warning("Could not find the main content div. Stopping.")
                break

            main = target_div.find('main', class_= "site-main mb-5", id= "main")

            for article in main.find_all('article'):
                timestamp = article.find('div', class_="entry-meta").find('span', class_="posted-on").a.get_text(strip=True)
                timestamp = timestamp.lower().strip()

                if "hour" in timestamp or "hours" in timestamp or "minutes" in timestamp or "min" in timestamp:
                    news_header = article.find('header').h2.a.get_text(strip=True)
                    news_link = article.find('div', class_="entry-content").p.a.get('href')

                    logger.info(f"Extracting: {news_header}")

                    try:
                        content_response = requests.get(news_link, headers=headers, timeout=10).text
                        content_soup = BeautifulSoup(content_response, 'lxml')

                        content_div = content_soup.find('div', class_= "the-post-content")

                        if content_div:
                            for junk in content_div.select("section.wpfsc-stay-connected"):
                                junk.decompose()
                            
                            for para in content_div.find_all('p'):
                                raw_content = " ".join(para.get_text(strip=True))
                                
                            news_content = re.sub(r'(?<=\S) (?=\S)', '', raw_content)
                            news_content = re.sub(r'\s+', ' ', news_content).strip()  
                        else:
                            news_content = "Content Not Found"

                    except Exception as e:
                        logger.error(f"Failed to fetch content for {news_header}: {e}")
                        news_content = "Failed to extract content"
                
                    articles_data.append({
                        "title" : news_header,
                        "link" : news_link,
                        "body" : news_content,
                        "source" : "propakistani"
                    })
                
                else:
                    logger.warning(f"Hit time barrier: '{timestamp}'. Scraper stopping.")
                    keep_scraping = False
                    break

            page += 1

        except Exception as e:
            logger.error(f"Failed to load ProPakistani page {page}: {e}")
            break
    
    logger.success(f"Successfully scraped {len(articles_data)} articles from ProPakistani.")
    return articles_data


if __name__ == "__main__":
    data = scrape_propakistani()
    print(data)