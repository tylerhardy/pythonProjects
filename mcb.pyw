#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage:
# py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
'''
Program Semantics
- The command line argument for the keyword is checked
- if the argument is 'save', then the clipboard contents are saved to the keyword.
- If the argument is 'list', then all the keywords are copied to the clipboard.
- Otherwise, the text for the keyword is copied to the clipboard.

Program actions:
- Read the command line arguments from sys.argv.
- Read and write to the clipboard.
- Save and load to a shelf file.
'''
# Import Modules
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    if mcbShelf[sys.argv[2]].isspace():
        print("There is nothing copied in your clipboard.  Please select the text and copy it.")
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.clear()
        pyperclip.copy('')
    else:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

