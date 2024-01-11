from StringHelper import *
from token import Token

class AnalizadorLexico:
   def __init__(self, codigoFonte):
      self.codigoFonte = codigoFonte
      self.valorDoToken = ''
      self.posicaoAtual = 0
      self.estado = 0
      self.listaDeTokens = []
      self.linha = 1
      self.coluna = 0

   def nextChar(self):
      self.posicaoAtual += 1
      return self.codigoFonte[self.posicaoAtual-1]
   
   def isEOF(self):
      return self.posicaoAtual == len(self.codigoFonte)
   
   def backChar(self):
      self.posicaoAtual-=1

   def nextToken(self):
      if self.isEOF():
         return "Arquivo Vazio"
      
      self.valorDoToken = ""
      while not self.isEOF():
         
         charAtual = self.nextChar()
         self.coluna += 1
         if(charAtual == '\n'):
            self.linha += 1
            self.coluna = 0
            
         if (isCharDesconhecido(charAtual)):
               print("Erro Lexico na linha {} coluna {}: Caracter desconhecido \" {} \"".format(self.linha, self.coluna, charAtual))
            

         if self.estado == 0:
            if charAtual.isspace():
               self.estado = 0
            
            elif isLetra(charAtual):
               self.valorDoToken += charAtual
               self.estado = 1
               continue
            
            elif isNumber(charAtual):
               self.valorDoToken += charAtual
               self.estado = 2
               continue

            elif isEqual(charAtual):
               self.valorDoToken += charAtual
               self.estado = 3
               continue

            elif isAspas(charAtual):
               self.valorDoToken += charAtual
               self.estado = 4
               continue

            elif isMoreOrLess(charAtual):
               self.valorDoToken += charAtual
               self.estado = 5
               continue

            elif isNot(charAtual):
               self.valorDoToken += charAtual
               self.estado = 6
               continue

            elif isAritimetricOperator(charAtual):
               self.valorDoToken += charAtual
               self.estado = 7

            elif isSemiColon(charAtual):
               self.valorDoToken += charAtual
               self.estado = 8
               continue

            elif isOpenBlock(charAtual):
               self.valorDoToken += charAtual
               self.estado = 9

            elif isCloseBlock(charAtual):
               self.valorDoToken += charAtual
               self.estado = 10

            elif isParenthesesOpened(charAtual):
               self.valorDoToken += charAtual
               self.estado = 11

            elif isParenthesesClosed(charAtual):
               self.valorDoToken += charAtual
               self.estado = 12
            elif isComma(charAtual):
               self.valorDoToken += charAtual
               self.estado = 13

         if(self.estado == 1):
            if(isLetra(charAtual) | isNumber(charAtual)):
               self.valorDoToken += charAtual
            else:
               #Aqui tem o codigo de formacao de tk_ID
               self.estado = 0
               self.backChar()
               newToken = Token(self.valorDoToken,1, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
         
         elif(self.estado == 2):
            if(isNumber(charAtual)):
               self.valorDoToken += charAtual            
            else:
               self.estado = 0
               self.backChar()
               newToken = Token(self.valorDoToken, 2, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''

         elif(self.estado == 3):
            if(isEqual(charAtual)):
               self.estado = 0
               self.valorDoToken += charAtual
               newToken = Token(self.valorDoToken,4, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
            else:
               self.estado = 0
               self.backChar()
               newToken = Token(self.valorDoToken,3, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
         
         elif(self.estado == 4):
            if(isAspas(charAtual)):
               self.valorDoToken += charAtual
               self.estado = 0
               newToken = Token(self.valorDoToken,5, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
            else:
               self.valorDoToken += charAtual
         
         elif(self.estado == 5):
            if(isEqual(charAtual)):
               self.valorDoToken += charAtual
               self.estado = 0
               newToken = Token(self.valorDoToken,4, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
            else:
               self.estado = 0
               self.backChar()
               newToken = Token(self.valorDoToken,4, self.linha, (self.coluna - len(self.valorDoToken)))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
         
         elif(self.estado == 6):
            if(isEqual(charAtual)):
               self.estado = 0
               newToken = Token(self.valorDoToken,4, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
            else:
               self.estado = 0
               self.backChar()
               newToken = Token(self.valorDoToken,6, self.linha, self.coluna - len(self.valorDoToken))
               self.listaDeTokens.append(newToken)
               self.valorDoToken = ''
         
         elif(self.estado == 7):
            self.estado = 0
            newToken = Token(self.valorDoToken,7, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''
         
         elif(self.estado == 8):
            self.estado = 0
            newToken = Token(self.valorDoToken,8, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''
         
         elif(self.estado == 9):
            self.estado = 0
            newToken = Token(self.valorDoToken,9, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''
         
         elif(self.estado == 10):
            self.estado = 0
            newToken = Token(self.valorDoToken,10, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''

         elif(self.estado == 11):
            self.estado = 0
            newToken = Token(self.valorDoToken,11, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''
         
         elif(self.estado == 12):
            self.estado = 0
            newToken = Token(self.valorDoToken,12, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''
         elif(self.estado == 13):
            self.estado = 0
            newToken = Token(self.valorDoToken,13, self.linha, self.coluna - len(self.valorDoToken))
            self.listaDeTokens.append(newToken)
            self.valorDoToken = ''