import bs4
import requests

def request(base_url,page):

    req = requests.get(base_url.format(page))
    return req.text

def soupify(data):

    soup = bs4.BeautifulSoup(data,'lxml')
    return soup

def find_element(soup,element):

    result = set()
    for name in soup.select(element):
        result.add(name.text)
    
    return result

link ='http://quotes.toscrape.com/page/{}/'
i = 1
author_set = set()
element = '.author'

while True:

    html_page = request(link,i)
    html_soup = soupify(html_page)
    if len(html_soup.select('.quote')) == 0:
        break
    else:
        author_set.update(find_element(html_soup,element))
        i += 1

for author in author_set:
    print(author)

print('\nTotal number of authors: ',len(author_set))