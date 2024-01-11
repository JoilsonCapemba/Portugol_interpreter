def isLetra(char):
    return char.isalpha()

def isNumber(char):
    return char.isdigit()

def isEqual(char):
    return char is '='

def isMoreOrLess(char):
    return char in '><'

def isNot(char):
    return char is '!'

def isAspas(char):
    return char is '"'

def fimDoArquivo(string, i):
    return (i == len(string))

def isAritimetricOperator(char):
    return char in '+-*/'

def isSemiColon(char):
    return char is ';'

def isOpenBlock(char):
    return char is '{'

def isCloseBlock(char):
    return char is '}'

def isParenthesesOpened(char):
    return char is '('

def isParenthesesClosed(char):
    return char is ')'

def isCharDesconhecido(char):
    return((not char.isspace()) and (not isLetra(char)) and (not isNumber(char)) and (not isAritimetricOperator(char)) and (not isEqual(char)) and (not isOpenBlock(char)) and (not isCloseBlock(char)) and (not isAspas(char)) and (not isParenthesesClosed(char)) and (not isParenthesesOpened(char)) and (not isSemiColon(char)) and (not isComma(char))and (not isMoreOrLess(char)) and (not isNot(char))) 

def isComma(char):
    return char is ','

def isDateType(string):
    tipoDedados = ['inteiro','real','caracter','logico','string']
    return string in tipoDedados

def isReservateWord(stringg):
    reservateWord = ['inicio','inteiro','real','caracter','logico','string','se','senao','enquanto','para','de',
    'ate','mostre','ler']

    return stringg in reservateWord
