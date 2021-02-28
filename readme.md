# Introdução prática de Antlr com python

## Pré requisitos

Para usar Antlr com python é necessario ter instalado:

- [python3](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
  - após instalar o python, instale o Antlr para python através do terminal
  ```terminal
  pip install antlr4-python3-runtime
  ```
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

pronto, uma lista de tokens encontrados no nosso `programa.txt` foi impressa na tela como abaixo:

```terminal
<10, ':'>
<1, 'DECLARACOES'>
<4, 'argumento'>
<10, ':'>
<1, 'INT'>
<4, 'fatorial'>
<10, ':'>
<1, 'INT'>
<10, ':'>
<1, 'ALGORITMO'>
<1, 'LER'>
<4, 'argumento'>
<1, 'ATRIBUIR'>
<4, 'argumento'>
<1, 'A'>
<4, 'fatorial'>
<1, 'SE'>
<4, 'argumento'>
<8, '='>
<2, '0'>
<1, 'ENTAO'>
<1, 'ATRIBUIR'>
<2, '1'>
<1, 'A'>
<4, 'fatorial'>
<1, 'ENQUANTO'>
<4, 'argumento'>
<8, '>'>
<2, '1'>
<1, 'INICIO'>
<1, 'ATRIBUIR'>
<4, 'fatorial'>
<9, '*'>
<11, '('>
<4, 'argumento'>
<9, '-'>
<2, '1'>
<12, ')'>
<1, 'A'>
<4, 'fatorial'>
<1, 'ATRIBUIR'>
<4, 'argumento'>
<9, '-'>
<2, '1'>
<1, 'A'>
<4, 'argumento'>
<1, 'FIM'>
<1, 'IMPRIMIR'>
<4, 'fatorial'>
```

# Observações importantes

Se os comandos iniciados com `python` não forem reconhecidos pelo terminal experimente `python3`, ou verifique se você adicionou python as variaveis de ambiente do seu sistema.
