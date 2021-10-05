import os
import re


def inputfile(filename):
    if os.path.exists(filename) == False:
        print('No input file')
        return False

    if os.stat(filename).st_size == 0:
        print('No DNA sequence')
        return False

    f = open(filename,'r')

    lines = f.readlines()
    if lines[0][0]!= '>':
        print('No correct format')
        return False

    sentence = ''

    index = 0
    for line in lines:
        if index == 0:
            index += 1
            continue

        if line[0] != '>':
            sentence = sentence + line
        
        if line[0] == '>':
            break

    sentence = sentence.replace('\n','')
    sentence = sentence.replace('\t','')
    sentence = sentence.replace(' ','')

    sentence.upper()

    if len(sentence) == 0:
        print('No correct format')
        return False

    check = False
    for ind in range(0, len(sentence)):
        if sentence[ind] == 'A' or sentence[ind] == 'C' or sentence[ind] == 'G' or sentence[ind] == 'T':
            continue
        else:
            check = True
            break
    
    if check:
        print('No DNA sequence')
        return False

    return sentence

def main():
    sentence = inputfile("C:\\Users\\qowor\\Documents\\assignment1_input.txt")
    if sentence != False:
        print(sentence)

if __name__ == "__main__":
	main()