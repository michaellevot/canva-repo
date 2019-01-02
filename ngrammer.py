#!/usr/bin/python
# Prints ngrams \t frequencies for text input. 
# Syntax: ngrammer.py -f TEXT_FILE -n MINIMUM_NUMBER -x MAXIMUM_NUMBER

import argparse,sys
from collections import Counter

def main():
    
    # Creates arguments "-f" for input file, "-n" for minimum ngram length, "-x" for max mgram length
    parser = argparse.ArgumentParser()

    parser.add_argument('-f','--file',type=str,default=None,
                        help='file to be parsed into n-grams')

    parser.add_argument('-n','--minimum',type=int,default=None,
                        help='min. no. ngrams')

    parser.add_argument('-x','--maximium',type=int,default=None,
                        help='max no. ngrams')

    args = parser.parse_args()        

    allgrams = []

    # Gets ngrams for ngram min-max
    for line in open(args.file):
        line = line.split()

        for n in range(args.minimum,args.maximium+1):
            grams = [line[i:i+n] for i in xrange(len(line)-n+1)]

            # Turns large dictionary into lists 
            for gram in grams:
                gram = ' '.join(str(e) for e in gram)
                allgrams.append(gram)

    # Gets dictionary of ({'ngram': freqs})
    frequencies = Counter(allgrams)
    
    # Turns dictionary into list of tuples [(ngram, freqs), ...]
    frequencies = (frequencies).items()
    
    # Sorts tuples by frequency
    sorted_list = sorted(frequencies, key=lambda x: x[1], reverse=True)

    # Prints ngrams, freqs tab separated
    for x, y in sorted_list:
        print x+"\t",y

if __name__ == '__main__':
        main()
