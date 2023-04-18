from requests import get # 웹사이트를 받아오는 방식
from bs4 import BeautifulSoup
base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "java"
response = get(f"{base_url}{search_term}") #웹사이트 받아옴
if response.status_code != 200:
  print("Can't request website")
else:
  results = []
  soup = BeautifulSoup(response.text , 'html.parser')
  jobs = soup.find_all('section' , class_= "jobs")
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      anchors = post.find_all('a')
      anchors = anchors[1]
      link = anchors['href']
      company, kind, region = anchors.find_all('span', class_="company")
      title = anchors.find('span')
      job_data = {
        'company' : company.string,
        'region' : region.string,
        'position' : title.string
      }
      results.append(job_data)
  for result in results:
    print(result)
    print("////////////")