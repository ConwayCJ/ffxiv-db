import requests
from bs4 import BeautifulSoup
from html_to_craftables import parse_page

def main():
  parse_page('carper', 50)

main()