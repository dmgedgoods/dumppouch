#! python3
# mclip.py - a multiclipboard program

TEXT = {'agree': """Yes, I agree, this is fine.""",
        'busy': """Sorry, I'm busy right now""",
        'upsell': """Would you consider making this a subscription?"""}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' coppied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

