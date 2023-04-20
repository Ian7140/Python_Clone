from requests import get # 웹사이트를 받아오는 방식
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}") #웹사이트 받아옴 / 전체의 url 만듦
    if response.status_code != 200:
     print("Can't request website")
    else:
     results = []
     soup = BeautifulSoup(response.text , 'html.parser') 
     #response.text는 방금 얻은 웹사이트의 코드를 줌
    #BeautifulSoup는 우리가 가진 html코드를 우리가 다룰 수 있는 python entity로 바꾸어줌
     jobs = soup.find_all('section' , class_= "jobs")
     for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
         anchors = post.find_all('a')
         anchors = anchors[1]
         link = anchors['href']
         company, kind, region = anchors.find_all('span', class_="company")
         title = anchors.find('span') #find는 하나의 항목만 줌
         job_data = {
            'link' : f"https://weworkmotely.com{link}",
            'company' : company.string,
            'region' : region.string,
            'position' : title.string #문자부분만 남기게 해주는 역할 ex)<h1>click here</h1> -> click here 만 가지고 옴
         }
         results.append(job_data) #jobsection 에서 추출된 list에서 job을 추출할때마다 result 리스트에 값을 넣음
        for result in results:
         print(result)
         print("////////////")
