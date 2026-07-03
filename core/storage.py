from pathlib import Path
import csv
from datetime import datetime

def csv_history(articles, filename="data/history.csv"):
    file_path = Path(filename)
    file_path.parent.mkdir(parents=True,exist_ok=True)

    file = file_path.is_file()

    headers = ["title", "link", "body", "source", "region", "score", "timestamp"]

    with file_path.open(mode='a', newline='', encoding='utf-8') as f:

        writer = csv.DictWriter(f, fieldnames=headers)
        if not file:
            writer.writeheader()
        
        for article in articles:
            article['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(article)
