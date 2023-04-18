from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

for each in websites: 
    #for 뒤에 오는 건 placeholder , 보통 movie in movies, website in websites 의 형식으로 만듦
    if not each.startswith("https://"):
        each = f"https://{each}"
    response = get(each) #띄어쓰기 중요함
    print(response)