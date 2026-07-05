from loguru import logger
from scraper.propakistani import scrape_propakistani
from core.filter import filtering_and_tagging
from core.scorer import score_articles
from core.storage import csv_history
from email_digest.builder import build_email_html
from email_digest.sender import send_digest_email

def run_pipeline(send_email : bool = True):
    
    logger.info("Pipeline Is Starting...")
    raw_articles = scrape_propakistani()

    if not raw_articles:
        logger.error("Unable to provide service. No articles scraped.")
        return
    logger.info(f"Raw articles scraped: {len(raw_articles)}")
    
    filtered_articles = filtering_and_tagging(raw_articles)
    logger.info(f"Articles surviving the filter: {len(filtered_articles)}")

    scored_articles = score_articles(filtered_articles)

    csv_history(scored_articles)

    if send_email:
        html = build_email_html(scored_articles)
        send_digest_email(html)
    else:
        logger.debug("Email sending skipped via CLI flag.")