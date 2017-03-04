from sys import *

def open_file(filename):
    data = open(filename, 'r').read()#open file in for reading and read it
    return data# return the what the file read
    

'''
lexer is used to split the data from the file that is read
into tokens that are then processed
'''
def lexer(filecontents):
    tokens = []
    token = ""
    mode = 0
    string = ''
    number = ''
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    filecontents = list(filecontents)
    for char in filecontents:
        token = token + char
        if token == '\n':
            token = ''
        elif token == ' ':
            if mode == 0:
                token = ''
        elif token == 'PRINT':
            tokens.append('PRINT:')
            token = ''
        elif token in numbers:
            if mode == 2:
                number += token
                token =''
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

run()