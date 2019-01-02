#!/usr/bin/python

import argparse,codecs
from unicodedata import *

def main():
    
    # Define argument
    parser = argparse.ArgumentParser()

    parser.add_argument('-f','--file',type=str,default=None,
                        help='file to be parsed into n-grams')
    args = parser.parse_args()  

    # Set input file encoding to utf-8
    text_input = codecs.open(args.file, encoding='utf-8')
    
    characters = []

    # Get list of all words in input file.
    for word in text_input:
        word = word.strip("")

        # Gets list of all unicode characters in words
        # (non-unique, so I can add a frequency counter later)
        for character in word:
            characters.append(character)

    # Sorts and uniques list of unicode characters
    for codepoint in sorted(set(characters)):
        
        # If character is not new line ("-" is a default when the line is empty
        # Print the character, the codepoint of that character, then the unicode name of that character
        if name(codepoint,'-')!='-':
            print eval('u"\\u%04x"' % ord(codepoint)).encode('utf-8'), "%04x"%(ord(codepoint)), name(codepoint)

if __name__ == '__main__':
        main()
