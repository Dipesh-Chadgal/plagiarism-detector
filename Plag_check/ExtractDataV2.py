from inscriptis import get_text
import time
import urllib.request
def Extract_data_website(url):

    uf = urllib.request.urlopen(url)
    html = uf.read() 
    print(html)
    
Extract_data_website("https://www.coursehero.com/file/177253387/eduf2docx/")