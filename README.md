# Lab 8 - Continuous Integration (GitHub Actions)
Python project with unit tests and a GitHub Actions pipeline:
tests (Python 3.9-3.12) -> lint (Black, Flake8) -> email on failure.

Run locally: pip install -r requirements.txt && pytest
Required GitHub secrets: EMAIL_USERNAME, EMAIL_PASSWORD (Gmail app password), EMAIL_TO
