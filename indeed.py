import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  pagination = soup.find("div",{"class":"pagination"})
  links= pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(link.string)
  max_page = pages[-1]
  return max_page

def extract_jobs(last_page):
  for page in range(last_page):
    requests.get(f"{URL}&start={page*LIMIT})
