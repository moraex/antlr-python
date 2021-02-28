'''
para executar, basta abrir o terminal no diretorio /src
no terminal:
> java -jar antlr-4.9.1-complete.jar -Dlanguage=Python3 AlgumaLexer.g4
> python main.py programa.txt

o analizador lexico imprimira no terminal todos os tokens na forma
<tipo, valor>
'''

from antlr4 import *
from AlgumaLexer import AlgumaLexer # o mesmo nome do arquivo .g4 passados
import sys


def main():
    nomeArquivo = sys.argv[1]   # nome do arquivo a ser analisado lexicamente

    # FileStream eh um metodo a lib Antlr4 que le o arquivo passado
    # 'encoding' recebe o padrão que o arquivo esta codificado
    # lexer eh o objeto Lexer
    lexer = AlgumaLexer(FileStream(nomeArquivo, encoding='utf-8'))

    # 'getAllTokens()' eh um metodo que retorna todos os tokens encontrados na ordem
    # que foram encontrados
    tokenList = lexer.getAllTokens()

    # estou percorrendo a lista de tokens listados pelo metodo 'getAllTokens()'
    # e para cada token encontrado estou imprimindo o tipo do token e 
    for token in tokenList:
        print("<",token.type, ", '", token.text, "'>", sep="")

if __name__ == '__main__':
    main()
