# News Aggregator CLI Tool
A professional Python-based Command Line Interface (CLI) tool to fetch, filter, and export news headlines. This project was developed as part of an internship task at **SYNTECXHUB**.

# Features
- **Web Fetching:** Retrieves real-time news using NewsAPI.
- **Local Storage:** Stores aggregated news in a SQLite database for offline access.
- **Smart Deduplication:** Automatically skips duplicate headlines to keep the data clean.
- **CLI Filters:** Search stored news by keyword or source directly from the terminal.
- **Data Export:** Generate professional reports in **CSV** or **Excel** formats using Pandas.
- **Error Handling:** Robust try-except blocks to handle network issues and API limits.
---

# Project Structure
```text
NewsAggregator/
├── main.py            # Entry point & CLI Argument Handling
├── scraper.py         # API integration & Error Handling
├── database.py        # SQLite Logic & Deduplication
├── exporter.py        # CSV/Excel Automation Logic
├── requirements.txt   # Project Dependencies
└── README.md          # Project Documentation
```
# Installation & Setup

1. **Clone the repository:**
```bash
   git clone https://github.com/mabdullah236/Syntecxhub_internship_tasks/tree/main/week4/task1/news_aggregator.git
   cd news-aggregator-cli
```
2. **Install required libraries:**
```bash
   pip install -r requirements.txt
```
3. **Get your API Key:**
   Go to [NewsAPI.org](https://newsapi.org/) and register for a free API key.
   Open `main.py` and replace `YOUR_NEWSAPI_KEY_HERE` with your actual key.

# How to Use

# 1. Fetch News
To fetch and save news about a specific topic (e.g., Technology):
```bash
python main.py --fetch "technology"
```

# 2. List & Filter News
To view news stored in the database:
```bash
python main.py --list
```
To filter by a specific source (e.g., BBC News):
```bash
python main.py --list --source "BBC News"
```

# 3. Export Data
To generate a report in Excel or CSV:
```bash
python main.py --export excel
# OR
python main.py --export csv
```

# Error Handling
- Handles **Network Timeouts** if internet is disconnected.
- Prevents **Database Corruption** using proper connection management.
- Skips **Duplicate Entries** using SQL UNIQUE constraints.
