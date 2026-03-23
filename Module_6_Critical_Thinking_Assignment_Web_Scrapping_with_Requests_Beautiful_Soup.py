"""
Pseudocode

BEGIN PROGRAM

IMPORT libraries: requests, BeautifulSoup, nltk stopwords, WordCloud, matplotlib

DOWNLOAD nltk stopwords

FUNCTION fetch_webpage(url):
    SEND GET request to url
    RETURN HTML content

FUNCTION parse_html(html):
    PARSE html with BeautifulSoup
    RETURN extracted text

FUNCTION clean_text(text):
    CONVERT text to lowercase
    SPLIT text into words
    LOAD stopwords
    FILTER words (alphabetic AND not stopwords)
    RETURN joined cleaned text

FUNCTION generate_wordcloud(text):
    CREATE word cloud from text
    DISPLAY word cloud
    SAVE image file

MAIN:
    SET url = python.org
    html = fetch_webpage(url)
    text = parse_html(html)
    cleaned = clean_text(text)
    generate_wordcloud(cleaned)

END PROGRAM
"""


"""
Web Scraping and Word Cloud Generator

This program retrieves webpage content from python.org, parses the HTML using BeautifulSoup,
cleans the extracted text by removing stopwords using NLTK, and generates a word cloud
visualization based on the processed text.
"""

import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Download stopwords dataset
nltk.download('stopwords')

def fetch_webpage(url):
    """Fetch HTML content from a given URL."""
    response = requests.get(url)
    return response.text

def parse_html(html_content):
    """Parse HTML and extract visible text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    return text

def clean_text(text):
    """Clean text by removing stopwords and unnecessary characters."""
    text = text.lower()
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    return " ".join(filtered_words)

def generate_wordcloud(cleaned_text):
    """Generate and display a word cloud from cleaned text."""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    wordcloud.to_file("wordcloud.png")

if __name__ == "__main__":
    url = "https://www.python.org"
    html_content = fetch_webpage(url)
    extracted_text = parse_html(html_content)
    cleaned_text = clean_text(extracted_text)
    generate_wordcloud(cleaned_text)

