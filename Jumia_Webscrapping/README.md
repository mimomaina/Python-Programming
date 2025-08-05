

# Jumia Kenya Product Scraper

A Python-based web scraper that extracts product data from the "Flash Sales" section of Jumia Kenya (https://www.jumia.co.ke), performs basic market analysis, and provides actionable insights for sellers.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collected](#data-collected)
- [Analysis Methodology](#analysis-methodology)
- [Output](#output)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [License](#license)

## Overview

This project scrapes product information from Jumia Kenya's "Flash Sales | Live Now" section, analyzes customer engagement metrics, and generates data-driven recommendations. The scraper is designed to handle Jumia's dynamic HTML structure with obfuscated class names and changing layouts.

The tool enables users to extract e-commerce data for market research, trend analysis, and business intelligence without relying on APIs. It demonstrates practical web scraping techniques using Python's requests and BeautifulSoup libraries.

## Features

- **Dynamic Section Detection**: Automatically locates the "Flash Sales" section using flexible text matching with regular expressions
- **Robust Element Selection**: Uses content-based selection (e.g., "Ksh" for prices) rather than relying solely on class names
- **Multiple Fallback Strategies**: Implements several approaches to find product elements when primary methods fail
- **Structured Data Export**: Saves extracted information to CSV format for further analysis
- **Popularity Analysis**: Uses review count as a proxy for product demand and sales volume
- **Rating Stabilization**: Applies statistical adjustment to ratings to account for small sample sizes
- **Seller Recommendations**: Identifies trending brands based on high-review products
- **Error Resilience**: Includes comprehensive error handling to skip problematic products without stopping execution

## Installation

### Prerequisites

- Python 3.6 or higher

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jumia-scraper.git
   cd jumia-scraper
(Recommended) Create a virtual environment to isolate dependencies:
bash


1
2
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required Python packages:
bash


1
pip install requests beautifulsoup4
Usage
Run the scraper script:

bash


1
python scraper.py
Expected Workflow
The script sends an HTTP request to Jumia Kenya with browser-like headers
It parses the HTML response using BeautifulSoup
The "Flash Sales | Live Now" section is identified through text pattern matching
Product elements are extracted from the section container
Relevant data points are collected for each product
Data is saved to products.csv in the project directory
Analysis results and recommendations are displayed in the console
Sample Output


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
Successfully accessed Jumia Kenya
Found section: 'Flash Sales | Live Now'
Found 12 products in the deals section
Successfully saved 12 products to 'products.csv'


##POPULARITY ANALYSIS AND SELLER RECOMMENDATION


##Top 5 Most Reviewed Products:
1. Original Wireless Earbuds | Reviews: 45 | Rating: 4.2 → Adj: 4.18
2. Smartphone X Pro | Reviews: 38 | Rating: 4.5 → Adj: 4.47
3. Smart LED TV | Reviews: 29 | Rating: 4.1 → Adj: 4.08

##Recommendation: Sellers should consider products from 'Original'.
Data Collected
The scraper extracts the following information for each product in the Flash Sales section:

###Product Name
Full name of the product
Text content of
<h3>
tag within product element
Brand
Manufacturer or brand name
First word of the product name
Price (Ksh)
Selling price in Kenyan Shillings
Text containing "Ksh" with non-numeric characters removed
Discount (%)
Available percentage discount
Text containing "%" with non-numeric characters removed
Reviews
Number of customer reviews
Numeric value extracted from review count text
Rating
Average customer rating out of 5
Decimal number extracted from star rating text

###Analysis Methodology
Popularity Metric
The analysis uses number of reviews as a proxy for product popularity and sales volume. This assumption is based on the correlation between customer reviews and purchase frequency in e-commerce platforms.

###Adjusted Rating Formula
To prevent products with few reviews from appearing artificially high-rated, the script calculates an adjusted rating using the formula:



1
adjusted_rating = (original_rating × review_count + 4) / (review_count + 2)
This Bayesian adjustment adds one 5-star and one 1-star review to the existing data, providing a more realistic measure of customer satisfaction that accounts for sample size. Products with many reviews see minimal adjustment, while those with few reviews are pulled toward a neutral 2.5 average.

Seller Recommendation Logic
The recommendation engine:

Filters products with 5 or more reviews to ensure meaningful data
Counts brand occurrences among these high-review products
Identifies the most frequently appearing brand
Recommends this brand as a potentially profitable option for sellers
This approach identifies brands that are currently popular and well-received in the marketplace.

Output
File Output
products.csv: Comma-separated values file containing all scraped product data with the following columns:
Product Name
Brand
Price (Ksh)
Discount (%)
Reviews
Rating
The CSV file uses UTF-8 encoding to support special characters and is formatted with a header row followed by data rows.

Console Output
The script provides real-time feedback including:

Status of page access (success/failure)
Name of detected deals section
Number of products found
Success confirmation with count of saved products
Popularity analysis results
Top 5 most reviewed products with original and adjusted ratings
Brand recommendation for sellers
Troubleshooting
Common Issues and Solutions
"Could not find 'Flash Sales' section"
Section temporarily unavailable or renamed
Verify the section exists on the live site; check for alternative names like "Top Deals"
"No products found"
HTML structure changes or JavaScript rendering
Inspect current page structure; consider implementing Selenium for JavaScript support
Connection errors or 403 status
Request blocking by server
Use different network; add delays between requests; rotate user agents
Empty CSV file
No data extraction or file writing failure
Check script completion; verify write permissions; add debug output
Incomplete data
Missing fields in some products
The scraper skips products with missing critical data; this is normal behavior

Debugging Tips
Inspect Current HTML Structure: Use browser developer tools to examine the current structure of the Flash Sales section.
Add Debug Output: Temporarily insert:
python


1
print("Container sample:", container.prettify()[:1000])
after locating the container to see the actual HTML being processed.
Test Selectors: Use the Python interpreter to test individual BeautifulSoup queries on the soup object.
Check Network Requests: Verify that the initial request returns the expected content by printing response.text[:500].
Limitations
HTML Structure Dependency: The scraper relies on consistent HTML patterns and may break if Jumia significantly changes its page layout or class naming conventions.
JavaScript Rendering: Content loaded dynamically via JavaScript may not be accessible through requests/BeautifulSoup alone, requiring Selenium or similar tools.
Rate Limiting: Frequent requests may trigger anti-bot measures, including IP blocking or CAPTCHA challenges.
Data Completeness: Some products may have incomplete information due to variations in how Jumia displays product details.
Brand Extraction: The brand identification method (first word of product name) is simplistic and may not accurately represent all brands.
Section Availability: The "Flash Sales" section may be temporarily empty or unavailable, resulting in no data collection.
Legal and Ethical Considerations: Web scraping should comply with the website's terms of service and robots.txt directives.
Future Improvements
Technical Enhancements
Selenium Integration: Implement Selenium WebDriver to handle JavaScript-rendered content and improve reliability.
Retry Mechanism: Add exponential backoff retry logic for failed requests with configurable attempt limits.
Comprehensive Logging: Implement structured logging to track scraping progress, errors, and performance metrics.
Configuration File: Support for configuration via JSON or YAML file to customize behavior without code changes.
Command-Line Arguments: Add argparse support for runtime options like output path, section selection, and verbosity level.
Data Collection Expansion
Product Images: Extract image URLs for visual analysis and cataloging.
Product Links: Capture direct URLs to product pages for deeper analysis.
Additional Categories: Extend scraping to other sections like "Top Deals", "Special Offers", or category-specific pages.
Historical Tracking: Implement timestamped data collection to track price and availability changes over time.
Analysis and Output
Data Validation: Add data cleaning and validation routines to ensure quality.
Duplicate Detection: Implement logic to identify and handle duplicate products.
Enhanced Analytics: Include price distribution analysis, discount effectiveness, and category trends.
Visualization: Add basic charts using matplotlib or export to Jupyter notebook for analysis.
API Output: Support JSON output format for integration with other applications.
License
This project is provided for educational and personal use. Users are responsible for ensuring compliance with applicable laws and website terms of service.

Usage Guidelines
Respect Rate Limits: Implement delays between requests to avoid overloading servers.
Check robots.txt: Review https://www.jumia.co.ke/robots.txt for crawling permissions.
Non-Commercial Use: This scraper is intended for learning and personal analysis.
Attribution: If sharing results, acknowledge the data source (Jumia Kenya).
Cease if Blocked: Stop scraping if you receive 403 errors or other blocking signals.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

