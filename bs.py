import urllib.request
from bs4 import BeautifulSoup

containter = set()
keywords = ['experiential+learning','Hands-on+learning', 'hands+on+learning','Service+learning', 'service-learning', 'internship','externship','practicum','undergraduate+research']

for each in keywords:
    url = "http://search.buffalo.edu/search?q="+ each +"&btnG=Search+UB&client=eUB&output=xml_no_dtd&proxystylesheet=eUB&oe=UTF-8&ie=UTF-8&num=1000&lr=&sort=date%3AD%3AL%3Ad1&ulang=en&entqr=0&entqrm=0&wc=200&wc_mc=1&ud=1&site=UB"
    response = urllib.request.urlopen(url)
    html_doc = response.read().decode()
    soup = BeautifulSoup(html_doc, 'html.parser')

    for link in soup.find_all('a'):
        val = link.get('href')
        if val[0] is not 's':
            containter.add(val)

#making list to set reduced 2660 to 2160 results

with open('out.txt', 'w') as f:
    # print(soup.prettify(), file=f) #print the whole html prettified
    for item in containter:
        print(item, file=f)
