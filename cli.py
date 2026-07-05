import typer
from loguru import logger
import sys
from pathlib import Path
from core.pipeline import run_pipeline

app = typer.Typer(help="Tech Pulse - Smart News Digest CLI")

def setup_logging():

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger.remove()

    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        level="INFO"
    )

    logger.add(
        log_dir / "app.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
        rotation="1 MB"
    )

@app.command()
def run(
    no_email: bool = typer.Option(False, help="Run the pipeline without sending the email digest.")
):
    logger.info("Starting the Tech Pulse Pipeline...")

    if no_email:
        logger.warning("Email digest is disabled via the --no-email flag.")
    else:
        logger.info("Email digest is enabled. (Will be sent at the end of the pipeline)")

    run_pipeline(send_email= not no_email)
    logger.success("Tech Pulse Finised Successfully")

if __name__ == "__main__":
    setup_logging()
    app()
