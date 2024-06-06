import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    command = sys.argv[1].lower()
    keyword = sys.argv[2]
    if command == 'save':
        mcb_shelf[keyword] = pyperclip.paste()
    elif command == 'delete':
        if keyword in mcb_shelf:
            del mcb_shelf[keyword]
elif len(sys.argv) == 2:
    command = sys.argv[1].lower()
    if command == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif command == 'delete':
        for key in list(mcb_shelf.keys()):
            del mcb_shelf[key]
    elif command in mcb_shelf:
        pyperclip.copy(mcb_shelf[command])

mcb_shelf.close()
