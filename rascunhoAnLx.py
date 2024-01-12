from contextlib import nullcontext
from operator import truediv
from StringHelper import *
from token import Token
from leitorDoArquivo import *


class Analisador_lexico:
    def __init__(self, codigoFonte):
        self.codigoFonte = codigoFonte
        self.posicaoAtual = 0
        self.estado = 0
        self.listaDeTokens = []

    def nextChar(self):
        self.posicaoAtual += 1
        return self.codigoFonte[self.posicaoAtual - 1]

    def isEOF(self):
        return self.posicaoAtual == len(self.codigoFonte)

    def backChar(self):
        self.posicaoAtual -= 1

    def nextToken(self):
        valorDoToken = ""
        if self.isEOF():
            return "Arquivo Vazio"

        while not self.isEOF():
            charAtual = self.nextChar()

            if self.estado == 0:
                if charAtual.isspace():
                    self.estado = 0

            if charAtual.isalpha():
                valorDoToken += charAtual
                self.estado = 1

            if charAtual.isdigit():
                valorDoToken += charAtual
                self.estado = 3

            if isEqual(charAtual):
                valorDoToken += charAtual
                self.estado = 5

            if isMoreOrLess(charAtual):
                valorDoToken += charAtual
                self.estado = 8

            if isAspas(charAtual):
                valorDoToken = +charAtual
                self.estado = 10

            if isNot(charAtual):
                self.estado = 10

            elif self.estado == 1:
                if charAtual.isalpha | charAtual.isdigit:
                    valorDoToken += charAtual

                else:
                    self.backChar()
                    token = Token(1, valorDoToken)
                    self.listaDeTokens.append(token)

#Analizador Sintatico
#reconhecimento do bloco prpincipal

def blocoPrincipal(listaDetokens):
    if(listaDetokens[0].valor != "inicio"):
        print("Erro na declaracao do bloco inicial: esperava a palavra [inicio]")
    if(listaDetokens[1].valor != "{"):
        print("Erro sintatico : esperava [{] para a abertura do bloco principal")
    if(listaDetokens[len(listaDetokens) - 1].valor != "}"):
        print("Erro sintatico : esperava [}] para o final do bloco principal")

def declaracaoDeVariaveis(listaDeTokens):
    print("teste")

def criarListaDeInstrucoes(listaDeTokens):
    ListaDeinstrucoes = []
    i = 0
    j = 0
    while i < len(listaDeTokens):
        ListaDeinstrucoes.append([])
        while listaDeTokens[i].valor not in ';}{':
            ListaDeinstrucoes[j].append(listaDeTokens[i])
            i+= 1
        
        ListaDeinstrucoes[j].append(listaDeTokens[i])
        j += 1
        i += 1

    return ListaDeinstrucoes


an = Analisador_lexico(codigoFormatoString())
"""an.nextChar()
print(an.nextChar())
print(an.nextChar())
print(an.nextChar())
print(an.nextChar())
print(an.nextChar())"""
print(an.posicaoAtual())
