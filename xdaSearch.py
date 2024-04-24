import requests, bs4, webbrowser

# Set headers:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 1st phase - constant link, 2nd phase - link from argument

subforumLink = 'https://xdaforums.com/f/redmi-9-power-9t.12055/page-9999999' # page numer so that it goes to the last page

res = requests.get(subforumLink, headers=headers)

# print(res.raise_for_status())


subforumSoup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = subforumSoup.select('a[data-xf-init="preview-tooltip"]')

for linkElem in linkElems:
    print(linkElem.getText())