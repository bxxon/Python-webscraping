
# Web Scraping Project

This project is a web scraping tool designed to extract data from different types of web pages.  
Users can input a URL and a specific class name to extract content from the web page.  
The code supports both static and dynamic websites using different approaches.

## Project Features

- **Static Pages**: Uses direct HTML parsing to extract data.
- **Dynamic Pages**: Uses Selenium and WebDriver to extract content that loads dynamically.
- **User Interface**: Allows users to enter the URL and class name to easily extract desired data.

## Ethical Guidelines

When contributing to this project, please ensure you follow the ethical guidelines below:

- **Integrity**: Write your code and contributions honestly. Do not present others’ work as your own.
- **Respect**: Treat other developers respectfully and fairly. Be positive and constructive in your contributions.
- **Accessibility**: Make your code as accessible as possible by adding explanations and keeping documentation updated.
- **Permissions and Licenses**: Respect the licenses and rights of any third-party software used. Review and follow the licenses of the libraries included in this project.
- **Legal Compliance**: Ensure that the software complies with legal regulations. Pay particular attention to data privacy laws (e.g., GDPR). When scraping, follow the website’s terms of use and check their `robots.txt` file.
- **Fair Use**: Respect fair use policies when scraping data. Avoid sending excessive requests that could overload websites.

## Requirements

To run this project, you need the following Python libraries installed:

- **requests**: For sending HTTP requests to web pages.
- **beautifulsoup4**: For parsing HTML and XML content.
- **selenium**: For scraping data from dynamic web pages.
- **webdriver_manager**: Automatically downloads the correct version of WebDriver.
- **re**: For text processing using regular expressions.

### Install Required Libraries

Install the required libraries one by one using the following commands:

```bash
pip install requests
pip install beautifulsoup4
pip install selenium
pip install webdriver_manager
```

> ⚠️ The `re` module is part of Python's standard library and does not require installation.

---

## University Email Scraper Extension

This Python-based tool scrapes `.edu` email addresses from university websites.  
It is designed to support research and academic projects by collecting publicly available contact information.

### Features

- Extracts email addresses ending with `.edu`
- Parses HTML pages using **BeautifulSoup4**
- Sends HTTP requests via **Requests**
- Filters data using **Regular Expressions**

### Use Case

Useful for:
- Creating datasets for academic conferences
- Research outreach
- Building contact lists from specific university departments

### Disclaimer

This tool is for educational and research purposes only.  
Please ensure compliance with website terms of service and data privacy regulations when using this tool.
