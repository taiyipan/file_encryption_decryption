# This program uses a cipher to decrypt messages

def main():
    # intro
    print('\nWelcome to Decryption Program!')
    # load cipher and store in dictionary
    cname = 'cipher.txt'
    cipher = load_cipher(cname)
    # read and encrypt message
    read_decrypt(cipher)
    # output result
    print('\nFile decryption successful.')

# load cipher and store in dictionary
def load_cipher(cname):
    print('Searching for cipher...')
    # open file, read mode
    try:
        infile = open(cname, 'r')
        print('Cipher located.')
    except IOError:
        print('Error: cipher not found.')
        quit()
    # create an empty dictionary
    cipher = dict()
    # read line by line
    for line in infile:
        # remove whitespace
        line.rstrip()
        # split the line into a list of 2 parts
        parts = line.split()
        # add each key/value pair to dictionary in a reverse order
        cipher[parts[1]] = parts[0]
    # close file
    infile.close()
    print('Cipher installed successfully.')
    # return dictionary
    return cipher

# read and decrypt message
def read_decrypt(cipher):
    # get user input
    in_fname = input('\nPlease name the input file for decryption: ')
    print('Searching...')
    # open input file, read mode
    try:
        infile = open(in_fname, 'r')
        print('File located.')
    except IOError:
        print('Error: file cannot be located.')
        quit()
    # get user input
    out_fname = input('\nPlease name the output file for decryption: ')
    # open output file, write mode
    outfile = open(out_fname, 'w')
    print('File created.')
    # read input file line by line
    for line in infile:
        # remove whitespace
        line.rstrip()
        # split line into a list of words
        words = line.split()
        # go through each word in the list
        for word in words:
            # go through each character in individual word
            for char in word:
                # use cipher to encrypt the character
                nchar = cipher.get(char, '-1')
                if nchar != '-1':
                    outfile.write(nchar)
                else:
                    outfile.write('ERROR')
            # add a space after word
            outfile.write(' ')
        # add a new line after each line
        outfile.write('\n')
    # close files
    infile.close()
    outfile.close()

main()
