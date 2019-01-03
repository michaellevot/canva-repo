#!/usr/bin/python
# Syntax: getCodepoints.py -f TEXT_FILE
# OR to enter text directly to terminal:
# getCodepoints.py

import argparse,sys,codecs
from unicodedata import *
from collections import Counter

def main():

    # If there is a file too parse, use argparse
    if len(sys.argv) == 3:

    # Define argument
        parser = argparse.ArgumentParser()

        parser.add_argument('-f','--file',type=str,default=None,
                        help='file to be parsed')
        args = parser.parse_args()

        # Set input file encoding to utf-8
        text_input = codecs.open(args.file, encoding='utf-8')
    
    # If no file to parse, prompt for text string
    else:
        # Convert to unicode, prompt for text string, set encoding to utf-8
        text_input = unicode(raw_input("Enter text: "),encoding='utf-8')

    characters = []

    # Get list of all words in input file.
    for word in text_input:
        word = word.strip("")

        # Gets list of all unicode characters in words
        for character in word:
            characters.append(character)

    # Gets dictionary of characters: frequency sorted by frequnecy. 
    characters = sorted(Counter(characters).items(), key=lambda x: x[1], reverse=True)

    # Prints codepoint information, frequnecy
    for codepoint, freq in characters:
        
        # If character is not new line ("-" is a default when the line is empty
        # Print the character, the codepoint of that character, then the unicode name of that character
        if name(codepoint,'-')!='-':
            print eval('u"\\u%04x"' % ord(codepoint)).encode('utf-8'), "%04x"%(ord(codepoint)), name(codepoint), freq

if __name__ == '__main__':
        main()
