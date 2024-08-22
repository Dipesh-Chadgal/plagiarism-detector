import requests,re
from bs4 import BeautifulSoup

def extract_data_website(url):
    
    params = {}
     
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url,params=params,headers=headers,verify=False)
    soup = BeautifulSoup(response.content,'html.parser')
    
    file1 = open('file1.txt', 'w',encoding="utf-8")
    file1.write(re.sub(r'[\n\n]{2,}', '',soup.get_text()))
    file1.close()
