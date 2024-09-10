# IMDb Web Scraping and Analysis Project

Overview
This project focuses on web scraping IMDb movie data using Scrapy, performing Exploratory Data Analysis (EDA) with Python in Jupyter Notebook, and creating a report using Power BI. The goal is to gather relevant movie information, analyze trends in the data, and present the insights visually in Power BI.

Table of Contents

1. Project Structure
2. Technologies Used
3.Setup Instructions
4. Web Scraping with Scrapy
5. Exploratory Data Analysis (EDA)
6.Power BI Report

Contributing
License

## Project Structure

IMDb_data/
│
├── imdb_data/
│   ├── spiders/
│   │   └── imdb_spider.py           # Scrapy spider to scrape IMDb movie data
│   ├── __init__.py
│   ├── items.py                     # Defines the structure of scraped data
│   ├── middlewares.py
│   ├── pipelines.py                 # Processing scraped data
│   └── settings.py                  # Scrapy project settings
│
├── data/
│   └── movies_data.json             # Scraped data stored in JSON format
│
├── eda/
│   └── imdb_eda.ipynb               # Jupyter notebook for Exploratory Data Analysis
│
├── power_bi_report/
│   └── imdb_power_bi.pbix           # Power BI file for data visualization
│
└── README.md                        # This README file

## Technologies Used
1.Python for web scraping and data analysis
2.Scrapy for scraping IMDb website
3. Jupyter Notebook for Exploratory Data Analysis
4. Power BI for creating the final report
5. Pandas for data manipulation and analysis
6. Playwright / Selenium for handling dynamic content (if necessary)
7. JSON format for storing scraped data


## Setup Instructions
1.Prerequisites
2.Python 3.8 or later
3. Power BI Desktop (for generating reports)
4. Jupyter Notebook
5.Scrapy

Playwright or Selenium (if needed for dynamic pages)
## Installation

Clone the repository:
git https://github.com/ABHISHEK64/Exploatory-Data-Analyticss/tree/main/imdb_data/imdb_data

cd imdb_data


Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required packages:


pip install scrapy pandas jupyter notebook selenium playwright
playwright install  # Install browser drivers for Playwright
Navigate to the Scrapy project:


cd imdb_scraper
Run the IMDb Scraper:

scrapy crawl imdb_spider -o ../data/movies_data.json
This will scrape movie data from IMDb and store it in movies_data.json.

Web Scraping with Scrapy
IMDb Scraper (imdb_spider.py)
This spider scrapes movie data such as title, release year, rating, duration, votes, and a short description from IMDb.

## Key Data Points Scraped:
1. Title: The movie's name
2. Release Year: Year of release
3. Rating: IMDb rating
4. Votes: Number of votes the movie has received
5. Meta Score: Critical rating
6. Duration: Movie duration
7. Description: Short movie plot
8. Poster URL: Link to the movie's poster

## Run the Spider

scrapy crawl imdb_spider

You can modify the number of pages or type of movies being scraped by updating the URL in the start_urls variable in imdb_spider.py.
