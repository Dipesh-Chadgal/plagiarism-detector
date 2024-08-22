import requests,re
import time
import format
import ExtractDataV3
import random
import os
import Matching



from bs4 import BeautifulSoup
global final_link_list
lol= 5
final_link_list = []
open("result.txt", "w").close()
open("result_temp.txt", "w").close()

def fetch_google_search_result(query):

    searching_url = "https://www.google.com/search" #the url that will be search on google engine
    params = {
        "q": query + "&tbs=li:1",
        "num": 2 # number of search results to retrieve
    }
    user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
] 
    user_agent = random.choice(user_agents) 
    headers = {'User-Agent': user_agent} 
    response = requests.get(searching_url, params=params, headers=headers)
    print(response.status_code)
    response = response.content
    
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.find_all("div",{"class":"yuRUbf"})
    print(lines)
    # data = soup.find("div",{"id":"result-stats"})  # this is for fetching the no. of result that come on google search
    # if data==None:
    #     print("Google detected the automation system")
    #     quit()
    # else:
    #     print(data.get_text())
    
    count = 0
    for i in links:                                           # this is for fetching the links that come on google search
        div_url = i.find('a')
        # if div_url['href'] not in final_link_list:
        #     final_link_list.append(div_url['href'])
        final_link_list.append(div_url['href'])
        count = count + 1
        
    
def print_result():
    return final_link_list
    
st = time.time()       
for lines in format.line_seperator():
    fetch_google_search_result('"'+lines+'"')

for i in print_result():
    print(i)

if(print_result==None):
    exit()

for links in print_result():
    ExtractDataV3.extract_data_website(links)
    # os.system('cmd "python -u "d:\Plag_check\diff2HtmlCompare.py" file1.txt sample_document.txt"')
    os.system(r'cmd /c "python -u d:\Plag_check\diff2HtmlCompare.py file1.txt sample_document.txt"')

et = time.time()
elapsed_time = et - st
print("Total time taken => ", elapsed_time)

outputFile = open('result.txt', "w")
inputFile = open('result_temp.txt', "r")
lines_seen_so_far = set()
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

number_of_words = 0
outputFile.close()
# Opening our text file in read only
# mode using the open() function

result_words = 0
original_words = 0

with open(r'sample_document.txt','r') as file:
    
    data = file.read()
    lines = data.split()
    original_words += len(lines)
file.close()
with open(r'result.txt','r') as file1:
    
    data = file1.read()
    line1 = data.split()
    result_words += len(line1)
file1.close()
print(result_words)
print(original_words)
print("Total Plagiarism Percentage => " , (result_words/original_words)*100)
