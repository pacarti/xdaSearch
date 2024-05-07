# Get the number of subpages:
def numOfSubpages(url):
    urlSplitList = url.split('page-')
    numOfPages = urlSplitList[1]
    return int(numOfPages)

# Get the url root
def urlRoot(url):
    urlSplitList = url.split('page-')
    urlRoot = urlSplitList[0]
    return urlRoot

import requests, bs4, webbrowser

# Set headers:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 1st phase - constant link, 2nd phase - link from argument

subforumLink = 'https://xdaforums.com/f/redmi-9-power-9t.12055/page-9999999' # page numer so that it goes to the last page
# subforumLink = 'https://xdaforums.com/f/redmi-9-power-9t.12055/page-2' # page numer so that it goes to the last page

res = requests.get(subforumLink, headers=headers)

currentUrl = res.url


phrase = 'wifi'

# print(res.raise_for_status())

subforumSoup = bs4.BeautifulSoup(res.text, 'html.parser') # <-- res.text - fetches text from CURRENT url(subforumlink in res variable as argument), that's why it is not updated in the loop

linkElems = subforumSoup.select('a[data-xf-init="preview-tooltip"]') # <-- this is not overwritten in the loop so that is the problem

# Search the selected phrase from this page:

while not currentUrl.endswith('page-1'):

    for linkElem in linkElems:
        # linkText = linkElem.getText()
        if phrase in linkElem.getText():
            print(linkElem.getText())
        # print(linkElem.getText())

    if currentUrl.endswith('page-1') == True:
        break


    newNumOfSubpages = numOfSubpages(currentUrl) - 1
    currentUrl = urlRoot(currentUrl) + 'page-' + str(newNumOfSubpages)


    # linkElems = []
    # to debug

    res = requests.get(currentUrl, headers=headers)

    subforumSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = subforumSoup.select('a[data-xf-init="preview-tooltip"]') 


# TODO: Search the selected phrase from all pages
    # TODO: Print text from all pages to check if script searches them correctly.

# while not url.endswith(''):
    # prevLink = soup.select('li.pageNav-page.pageNav-page--earlier')
    # Easier way will be to get current page url and subtract 1


# TODO: Open the webbrowser on distinguished websites 

# TODO: Change static link and phrase to dynamic