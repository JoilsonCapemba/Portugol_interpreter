class Token:

    tkIdentificador = 1
    tkNumero = 2
    tkAtribuicao =  3
    tkOperadorRelacional = 4
    tkString = 5
    tkOperadorLogico = 6
    tkOperadorAritmetrico = 7
    tkFimDeLinha = 8
    tkAberturaDeBloco = 9
    tkFinalDeBloco = 10
    tkAberturaDeParenteses = 11
    tkFinalDeParenteses = 12
    tkVirgula = 13


    def __init__(self,valor,tipo,linha,coluna):
        self.valor = valor
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna 
