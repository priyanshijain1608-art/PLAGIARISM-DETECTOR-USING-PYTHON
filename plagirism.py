

from difflib import SequenceMatcher

with open('txt1.txt') as fileone, open('txt2.txt') as filetwo:
    d_one = fileone.read()
    d_two = filetwo.read()

matches = SequenceMatcher(None, d_one, d_two).ratio()

print(f"The plagiarized content is {matches*100:.2f}%")