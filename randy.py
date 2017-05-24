from sys import *

def open_file(filename):
    data = open(filename, 'r').read()#open file in for reading and read it
    return data# return the what the file read
    

'''
lexer is used to split the data from the file that is read
into tokens that are then processed
'''
def lexer(filecontents):
    #list of things to be returned and sent to the parser
    tokens = []
    #each char is appended to this token string
    #this allows to read in things that are
    #more than one char. This is reset
    #almost each run through the loop
    #unless somthing is being read
    token = ""
    #mode dicitates what the tokens should match 
    #0=default 1=reading string 2=adding ints
    mode = 0
    #when in mode 1 each char is appened to this string
    #untill a second '
    #then it is appended to the list of tokens
    string = ''
    #when in mode 2 each number is appended 
    #to this string untill a ,
    #then it is reset and appended to the list of tokens
    number = ''
    #this list of numbers for checking if the token is currently a number
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    #break the file contens that are passed into a list
    filecontents = list(filecontents)
    #go throught each char in the file
    for char in filecontents:
    	#start be appending that char to a var called token
    	#this is done that it can read entire words like PRINT
        token = token + char
        #if we get a new line reset the token
        if token == '\n':
            token = ''
        #if there is a space and we are not reading a string
        #reset the token
        elif token == ' ':
            if mode == 0:
                token = ''
        #if the token says print
        #append print to the tokens to be returned
        #reset the token
        elif token == 'PRINT':
            tokens.append('PRINT:')
            token = ''
        #if the token is a number
        #and the mode is 2 then append that number
        #to the number string, reset token
        elif token in numbers:
            if mode == 2:
                number += token
                token =''
        #
        elif token == 'ADD':
            tokens.append('ADD:')
            token = ''
            mode = 2
        elif token == ',':
            if mode == 2:
                tokens.append(number)
                token = ''
                number = ''
        elif token == ')':
            if mode == 2:
                tokens.append(number)
                tokens.append(None)
                mode = 0
                token = ''
                number = ''
        elif token == '(':
            token = ''
        elif token == '\"':
            if mode == 0:
                mode = 1
                token = ''
            elif mode == 1:
                tokens.append(string)
                string = '' 
                token = ''
                mode = 0
        elif mode == 1:
            string += token
            token = ''
    return tokens

def parse(tokens):
    print tokens
    mode = 0
    runningAdditionTotal = 0
    for item in tokens:
        if item == 'PRINT:':
            mode = 1
        elif mode == 1:
            print item
            mode = 0
        elif item == 'ADD:':
            mode = 2
        elif mode == 2:
            if item == None:
                print runningAdditionTotal
                mode = 0
            else:
            	runningAdditionTotal += int(item)

def run():
    data = open_file(argv[1])#call function openfile on file called in args
    tokens = lexer(data)
    parse(tokens)

if __name__ == '__main__':
    run()