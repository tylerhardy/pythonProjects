#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

"""pseudocode:
What the program does:
- Get a street address from the command line arguments or clipboard.
- Open the web browser to the google maps page for the address.
Code will need to do the following:
- Read the command line arguments from sys.argv.
- Read the clipboard contents.
- Call the webbrowser.open() function to open the web browser.
"""

"""run example:
python mapit.py 870 Valencia St, San Francisco, CA 94110
"""


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/{0}'.format(address))