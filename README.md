# 🚀 Tech Pulse — Smart News Digest

Tech Pulse is a Python-based automation pipeline designed to scrape, curate, score, and deliver the latest tech news directly to your inbox. Built as a foundational Data Engineering project, it strictly follows a modular architecture emphasizing separation of concerns, robust logging, and defensive programming.

## ✨ Features (v1.1 Scope)

- **Automated Web Scraping:** Pulls the last 24 hours of tech news from ProPakistani using a chronological time-gate. Performs a "deep dive" to extract full article bodies while stripping away junk HTML.
- **The "Brain" (Filtering & Scoring):** - *Relevance Filter:* Drops articles that do not match predefined high-value tech topics.
  - *Weighted Scorer:* Ranks articles based on keyword density (+5 for Title matches, +1 per Body match).
  - *Region Tagger:* Automatically categorizes articles into "Pakistan Tech" or "Global Tech" based on local entity keywords.
- **The Vault (CSV Storage):** Safely appends curated articles to a historical CSV database (`data/history.csv`). Automatically handles header creation and truncates article bodies to 150 characters to keep Excel views clean.
- **Email Delivery:** Compiles the fully scored and categorized data into a professional, responsive HTML email digest dispatched via SMTP.
- **Modern CLI:** Powered by `typer` for a clean command-line interface.
- **Advanced Logging:** Replaces standard print statements with `loguru` for beautiful console output and automated file logging (`logs/app.log`).

## 🛠️ Tech Stack

- **Python 3**
- **Package Management:** `uv` (Blazing fast Rust-based package manager)
- **Web Scraping:** `requests`, `beautifulsoup4`, `lxml`
- **CLI & Logging:** `typer`, `loguru`
- **Environment Management:** `python-dotenv`
- **Built-in Libraries:** `csv`, `smtplib`, `email.mime`, `re`, `pathlib`

## 📂 Project Structure

```text
tech_pulse/
├── scrapers/
│   └── propakistani.py      # Main scraper module with time-gating & deep-dive logic
├── core/
│   ├── filter.py            # Filters irrelevant news & tags by region
│   ├── scorer.py            # Calculates weighted relevance scores
│   ├── storage.py           # Handles append-safe CSV writing
│   └── pipeline.py          # Master orchestrator tying all phases together
├── email_digest/
│   ├── builder.py           # Generates HTML template for the email
│   └── sender.py            # Handles SMTP login and dispatch
├── config/
│   └── keywords.py          # Defines ALL_TOPICS and PAKISTAN_ENTITY_KEYWORDS
├── data/
│   └── history.csv          # Auto-generated historical database
├── logs/
│   └── app.log              # Auto-generated application logs
├── .env                     # Hidden environment variables (Email credentials)
├── .gitignore               # Keeps secrets and virtual environments out of version control
└── cli.py                   # Typer CLI entry point
```

## 🚀 Setup & Installation
1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/FatehAli02/Tech-Pulse.git
    cd tech_pulse
    ```
2. Create and activate a virtual environment using uv
    ```bash
    # Create the environment
    uv venv

    # Activate it (Windows)
    .venv\Scripts\activate
    # Activate it (macOS/Linux)
    source .venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    uv pip install requirements.txt
    ```

4. Set up Environment Variables:

    Create a .env file in the root directory and add your email credentials. Note: You must use a 16-character Google App Password if using Gmail.

    ```text
    # Code Snippet
    SENDER_EMAIL=your.email@gmail.com
    SENDER_PASSWORD=your_16_char_app_password
    RECEIVER_EMAIL=your.email@gmail.com
    ```

## 💻 Usage

- Run the complete pipeline (Scrape -> Filter -> Score -> Store -> Email):

    ```text
    uv run python cli.py run
    ```
- Run the pipeline without sending the email (useful for local testing and populating the CSV):

    ```text
    uv run python cli.py run --no-email
    ```

- View the CLI help menu:

    ```text
    uv run python cli.py --help
    ```

## 👨‍💻 Author

Made by Fateh Ali 
[LinkedIn](www.linkedin.com/in/fateh-ali-072348352) | [GitHub](https://github.com/FatehAli02)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

* This project is for educational and portfolio purposes.
* Always ensure you have backups of your files before running automated archival scripts.