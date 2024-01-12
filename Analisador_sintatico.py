from dis import Instruction
from StringHelper import*

class AnalisadorSintatico:
    def __init__(self, listaDeTokens):
        self.listaDeInstrucoes = criarListaDeInstrucoes(listaDeTokens)
        self.instruction = self.listaDeInstrucoes[0]
        self.positionOfInstruction = 0
        self.token = self.instruction[0]
        self.positionOfToken = -1

    def nextInstruction(self):
        self.positionOfInstruction += 1
        return self.listaDeInstrucoes[self.positionOfInstruction - 1]

    def proximoTokenDaInstrucao(self):
        self.positionOfToken += 1
        return self.instruction[self.positionOfToken]
    
    def mensagemDeErro(self,esperado):
        print('Erro Sintatico na linha {} coluna {}: eperava {} mas encontrou {}'.format(self.token.linha ,  self.token.coluna, esperado, self.token.valor))
    
    
    #----------------- Gerenciador de Analises --------------------
    def gerencidarSintatico(self):
        i = 1
        for self.instruction in self.listaDeInstrucoes:
            self.positionOfToken = -1
            if (i == 1):
                self.regraDeCiacaoDoBlocoPrincipar(self.instruction)
                i = 2
            else:
                firstToken = self.instruction[0]
                if(isDateType(firstToken.valor)):
                    self.RegraDeDeclaracaoDeVariaveis(self.instruction)
                elif((not isReservateWord(firstToken.valor)) and (firstToken.tipo == firstToken.tkIdentificador or  firstToken.tipo == firstToken.tkNumero)):
                    self.RegraDeOperacaoAritmetrica(self.instruction)


    #---------------------------------------------------------------

    #--------------------Regra de inicializacao do bloco Principal-------------
    def regraDeCiacaoDoBlocoPrincipar(self,instruction):
        self.instruction = instruction
        if (self.instruction[0].valor != 'inicio'):
            self.mensagemDeErro('"inicio"')
        if (not isOpenBlock(self.instruction[1].valor)):
            self.mensagemDeErro('"{"')

    
    
    
    # ------------- Regra de operacoes Aritmetricas (concluuido)----------------

    def RegraDeOperacaoAritmetrica(self, instruction):
        self.instruction = instruction
        self.Operando()
        self.RegraDeOperacaoAux(';')

    def RegraDeOperacaoAux(self, delimitador):
        if ((len(self.instruction) - 1) > self.positionOfToken):
            self.token = self.proximoTokenDaInstrucao()
            if (self.token.valor != delimitador):
                self.Operador()
                if ((len(self.instruction) - 1) > self.positionOfToken):
                    self.Operando()
                    self.RegraDeOperacaoAux(delimitador)

    def Operando(self):
        self.token = self.proximoTokenDaInstrucao()
        if ((not isReservateWord(self.token.valor)) and self.token.tipo != self.token.tkIdentificador and self.token.tipo != self.token.tkNumero and self.token.tipo != self.token.tkString):
            self.mensagemDeErro('Identificador ou um Numero')

    def Operador(self):
        if (not isAritimetricOperator(self.token.valor)):
            self.mensagemDeErro('um Operador')

#-----------------------------------------------------------------------




#-----------------Regra de Declaracao de variaveis----------------------

    def RegraDeDeclaracaoDeVariaveis(self, instruction):
        self.instruction = instruction
        self.isTipoDeDados()
        self.identificador()
        self.proximoId()

    def isTipoDeDados(self):
        self.token = self.proximoTokenDaInstrucao()
        if ((not isDateType(self.token.valor))):
            self.mensagemDeErro('um tipo de dados')
    
    def identificador(self):
        self.token = self.proximoTokenDaInstrucao()
        if ((isReservateWord(self.token.valor)) or (self.token.tipo != self.token.tkIdentificador)):
            self.mensagemDeErro('um identificador')

    def proximoId(self):
        if(not isSemiColon(self.token.valor)):
            self.token = self.proximoTokenDaInstrucao()
            if (not isSemiColon(self.token.valor)):
                if ((self.positionOfToken == len(self.instruction) - 1) & (not isSemiColon(self.token))):
                    self.mensagemDeErro('";"')
                else:
                    self.virgula()
                    self.identificador()
                    self.proximoId()
    
    def virgula(self):
        if (self.token.valor != ','):
            self.mensagemDeErro('","')
#-------------------------------------------------------------------------



#----------------------Regra de Atribuicao de valor ----------------------

    def regraDeAtribuicao(self, instruction):
        self.instruction = instruction
        self.identificador()
        self.sinalDeAtribuicao()
        self.valorDaAtribuicao()


    def sinalDeAtribuicao(self):
        self.token = self.proximoTokenDaInstrucao()
        if (not isEqual(self.token.valor)):
            self.mensagemDeErro('"="')
    
    def valorDaAtribuicao(self):
        self.token = self.proximoTokenDaInstrucao()
        if (isReservateWord(self.token.valor)):
            self.mensagemDeErro('um valor')
        elif (((self.token.tipo == self.token.tkString) or (self.token.tipo == self.token.tkIdentificador)) or ((self.token.tipo == self.token.tkNumero))):
            self.positionOfToken -= 1
            self.RegraDeOperacaoAritmetrica(self.instruction)   
        else:
            self.mensagemDeErro('"valor"')
#------------------------------------------------------------------------------------------------


#----------------------- imprenssao de valores na tela -----------------------------------------
    def regraDeImpressaoNaTela(self, instruction):
        self.instruction = instruction
        self.token = self.proximoTokenDaInstrucao()
        if (self.token.valor != 'imprima'):
            self.mensagemDeErro('"imprima"')  

        self.token = self.proximoTokenDaInstrucao()
        if (self.token.tipo != self.token.tkAberturaDeParenteses):
            self.mensagemDeErro('"("')
        
        self.Operando()
        self.RegraDeOperacaoAux(")")

        if (self.token.tipo != self.token.tkFinalDeParenteses):
            self.mensagemDeErro('")"')
        
        self.token = self.proximoTokenDaInstrucao()
        if (self.token.tipo != self.token.tkFimDeLinha):
            self.mensagemDeErro('";"')
#-----------------------------------------------------------------------------------------------


#----------------------- Regra de leitura de dados -----------------------------------------
    def regraDeLeituraDedados(self, instruction):
        self.instruction = instruction
        self.token = self.proximoTokenDaInstrucao()
        if (self.token.valor != 'leia'):
            self.mensagemDeErro('"leia"')
        
        self.token = self.proximoTokenDaInstrucao()
        if (self.token.tipo != self.token.tkAberturaDeParenteses):
            self.mensagemDeErro('"("')
        
        self.identificador()

        self.token = self.proximoTokenDaInstrucao()
        if (self.token.tipo != self.token.tkFinalDeParenteses):
            self.mensagemDeErro('")"')
        
        self.token = self.proximoTokenDaInstrucao()
        if (self.token.tipo != self.token.tkFimDeLinha):
            self.mensagemDeErro('";"')
#-----------------------------------------------------------------------------------------------
















#----------------criador de Lista de instrucoes -------------------------

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
#--------------------------------------------------------------------------