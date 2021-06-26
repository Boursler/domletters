#!/usr/bin/python3

import sys
import string

def main():
    lines = sys.stdin.read()
    a = 97
    z = 122
    numletters = 26

    #index for each letter in alphabet
    lookup = [0] * numletters
    counts = []
    words = lines.split()
    for word in words:
        for letter in word:
            ascii = ord(letter.lower())
            if ascii >= a and ascii <= z:
                val = ascii - a
                lookup.insert(val, lookup[val]+1)
            else:
                lookup = [0] * numletters
                break
        lookup.sort(reverse=True)
        counts.append(lookup[0])
        lookup = [0] * numletters
    print(sum(counts))

if __name__ == "__main__":
    main()
