# 🚀 Startup Data Scraper (Modular Engine)

A professional, config-driven web scraping framework built to collect and structure data from various web sources. Designed with scalability in mind to support AI-native platforms and predictive data models.

## 📌 Overview
This project provides a robust, modular engine capable of scraping unstructured web data and converting it into a clean, structured `CSV` format. By separating the scraping logic from the target configuration, it allows for rapid pivoting between different data sources.

## 🛠 Features
- **Config-Driven Architecture:** Easily adapt to new websites by updating a configuration dictionary—no need to rewrite the core engine.
- **Data Structuring:** Built on `pandas`, ensuring data is automatically cleaned and exported into production-ready CSV files.
- **Resilient Logic:** Includes built-in error handling and `User-Agent` spoofing to ensure reliable data fetching.
- **Lightweight & Modular:** Separation of concerns makes the codebase easy to maintain and extend for complex needs.

## 📋 Project Structure
```text
scrapper/
├── data/               # Output directory for structured CSV data
├── .venv/              # Isolated environment for dependencies
├── main.py             # Entry point: handles config and execution
├── scraper_engine.py   # Core logic: handles requests and parsing
├── req.txt             # Project dependencies
└── .gitignore          # Keeps the repository clean

