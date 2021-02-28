# Introdução prática de Antlr com python

## Pré requisitos

Para usar Antlr com python é necessario ter isntalado:

- [python3](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
- [antlr-4.9.1-complete.jar](https://www.antlr.org/download/antlr-4.9.1-complete.jar)
- Java jdk1.8.0_211+

## Instalação

### 1. Copia deste repositorio

`git clone https://github.com/moons2/antlr-python`

ou baixando diretamente no [repositorio](https://github.com/moons2/antlr-python), clicando no botão **code > Download Zip**

## Utilização

após baixar este repositório

1. Abra o terminal dentro da pasta `/src`

2. Digite:

```terminal
java -jar antlr-4.9.1-complete.jar -Dlanguage=Python3 AlgumaLexer.g4
```

Será gerado alguns arquivos como:

- AlgumaLexer.py
- AlgumaLexer.tokens
- AlgumaLexer.interp

3. Por fim, vamos analisar lexicamente nosso aquivo `programa.txt`, digitando no terminal

```terminal
python main.py programa.txt
```

pronto, uma lista de tokens encontrados no nosso `programa.txt` foi impressa na tela!
