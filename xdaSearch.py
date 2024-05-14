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

import requests, bs4, webbrowser, sys

# Set headers:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


coreLink = 'https://xdaforums.com'

if len(sys.argv) == 1:
    print("Syntax: python3 xdaSearch.py <XDASearch forum URL> <phrase>")
    exit()

subforumLink = sys.argv[1] + '/page-9999999' # page numer so that it goes to the last page

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print("Syntax: python3 xdaSearch.py <XDASearch forum URL> <phrase>")
    exit()
elif not sys.argv[1].startswith(coreLink):
    print("The url must come from xdaforums.com!")
    exit()

if subforumLink[22] != 'f': # Checks if there is a 'f' on that position to determine if it's subforum link
    print("Please pass the link from some subforum!(Not the main page, etc.)")

if len(sys.argv) < 3:
    print("Please specify a search phrase.")
    exit()

phrase = sys.argv[2]



res = requests.get(subforumLink, headers=headers)

currentUrl = res.url


subforumSoup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = subforumSoup.select('a[data-xf-init="preview-tooltip"]') 


# Search the selected phrase from this page:

while not currentUrl.endswith('page-1'):

    for linkElem in linkElems:
        if phrase in linkElem.getText():
            resultLink = coreLink + linkElem.get('href')
            webbrowser.open(resultLink)

    if currentUrl.endswith('page-1') == True:
        break


    newNumOfSubpages = numOfSubpages(currentUrl) - 1
    currentUrl = urlRoot(currentUrl) + 'page-' + str(newNumOfSubpages)


    res = requests.get(currentUrl, headers=headers)

    subforumSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = subforumSoup.select('a[data-xf-init="preview-tooltip"]') 