#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

""" {Pseudocode}
What the program does:
- Loads the XKCD home page.
- Saves the comic image on that page.
- Follows the Previous Comic link.
- Repeats until it reaches the first comic.
What the code needs to do:
- Download pages with the requests module.
- Find the URL of the comic image for a page using Beautiful Soup.
- Download and save the comic image to the hard drive with iter_content().
- Find the URL of the Previous Comic link, and repeat.
"""

import requests, os, bs4, lxml

url = 'http://xkcd.com'                 # starting URL
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page {0}'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:{0}'.format(comicElem[0].get('src'))
            # Download the image.
            print('Downloading image {0}'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com{0}'.format(prevLink.get('href'))
            continue

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com{0}'.format(prevLink.get('href'))

print('Done.')
