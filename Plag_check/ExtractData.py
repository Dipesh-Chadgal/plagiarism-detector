import requests,re 
from bs4 import BeautifulSoup

def  Extract_data_website(websiteURL):
    url = websiteURL

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url,headers=headers)
    #print(response.content)
    soup = BeautifulSoup(response.content,'html.parser')
    #text1 = soup.find_all("p")
    #print(text1)
    for data in soup.find_all("p"):
        sum = data.get_text()
        print(sum)