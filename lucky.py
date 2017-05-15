#! python3
# lucky.py - Opens several Google search results.

"""PseudoCode
What the program does:
- Get search keywords from the command line arguments.
- Retrieves the search result page.
- Opens a browser tab for each result.

Code will need to do:
- Read the command line arguments from sys.argv.
- Fetch the search result page with the requests module.
- Find the links to each search result.
- CAll the webbrowser.open() function to open the web browser.
"""

import webbrowser, requests, bs4, sys

print('Googling...') # Diskplay text while downloading the google page
res = requests.get("https://www.google.com/search?q={0}".format(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com{0}'.format(linkElems[i].get('href')))
