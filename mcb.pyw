# Multiclipboard ~
# Saves and loads peices of text to the clipboard.
# Usage tips:
#       1. py.exe mcb.pyw save <keyword> - Saves the clipboard to the keyword
#       2. py.exe mcd.pyw <keyword> - Loads keyword to clipboard
#       3. py.exe mcb.pyw list - Loads all keywords to the clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Saving Clipboard content.
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv)==2:
    # List keywords and load content
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

