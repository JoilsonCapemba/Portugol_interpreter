from Analisador_lexico import*
from leitorDoArquivo import*
from token import Token
from Analisador_sintatico import*
an = AnalizadorLexico(codigoFormatoString())

print("juventina")

"""testes

print(an.codigoFonte)
print(len(an.codigoFonte))
print(an.codigoFonte[59])
an.posicaoAtual = 59
print(an.isEOF())


an.posicaoAtual = 60
print(an.isEOF())

tk = Token("joilson",2)
tk1 = Token("Nicasio",1)
tk2 = Token("Asdruba",3)
an.listaDeTokens.append(tk)
an.listaDeTokens.append(tk1)
an.listaDeTokens.append(tk2)


"""
an.nextToken()
#print(an.listaDeTokens)

"""for itens in an.listaDeTokens:
    print(itens.valor)
"""
#blocoPrincipal(an.listaDeTokens)

"""for itens in ListaDeInstrucoes[6]:
    print(itens.valor)"""

#print(ListaDeInstrucoes[0])

aStc = AnalisadorSintatico(an.listaDeTokens)

#aStc.RegraDeDeclaracaoDeVariaveis(aStc.listaDeInstrucoes[1])  //concluido

#aStc.gerencidarSintatico()

aStc.regraDeAtribuicao(aStc.listaDeInstrucoes[1])