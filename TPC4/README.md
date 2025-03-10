# 📝 TPC4

Neste TPC, o objetivo é construir um analisador léxico para uma linguagem de consulta que permita escrever frases que deverão ser interpretadas de forma a obter toda a informação da linguagem presente nessa frase.
O analisador léxico deve ser capaz de identificar e classificar corretamente os diferentes tokens presentes na linguagem, como palavras-chave, identificadores, literais, símbolos e números.

### Requirements
```shell
pip install ply
```

## Usage
To run the program, use the following command:
```shell
python lex_analizer.py
```

**Dont forget to change the input file in the project folder.**

O programa lê de um ficheiro de texto e escreve para o stdout os tokens identificados. Este pode ser guardaado utilizando funções do sistema operativo. Como por exermplo:
```shell
python lex_analizer.py > output.txt
```

## Author
<p><strong>Name:</strong> Fábio Magalhães</p>
<p><strong>Number:</strong> A104365</p>

## Results
Ficheiro de entrada exemplo `input.txt`:
```
SELECT ?nome ?desc WHERE {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en .
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc
}
```

Ficheiro de saída exemplo `output.txt` (Tokens):
```
LexToken(SELECT,'SELECT',1,0)
LexToken(VAR,'?nome',1,7)
LexToken(VAR,'?desc',1,13)
LexToken(WHERE,'WHERE',1,19)
LexToken(OPEN_CURLY,'{',1,25)
LexToken(VAR,'?s',2,31)
LexToken(A,'a',2,34)
LexToken(IRI,'dbo:MusicalArtist',2,36)
LexToken(DOT,'.',2,53)
LexToken(VAR,'?s',3,59)
LexToken(IRI,'foaf:name',3,62)
LexToken(LITERAL,'"Chuck Berry"@en',3,72)
LexToken(DOT,'.',3,88)
LexToken(VAR,'?w',4,94)
LexToken(IRI,'dbo:artist',4,97)
LexToken(VAR,'?s',4,108)
LexToken(DOT,'.',4,110)
LexToken(VAR,'?w',5,116)
LexToken(IRI,'foaf:name',5,119)
LexToken(VAR,'?nome',5,129)
LexToken(DOT,'.',5,134)
LexToken(VAR,'?w',6,140)
LexToken(IRI,'dbo:abstract',6,143)
LexToken(VAR,'?desc',6,156)
LexToken(DOT,'.',6,161)
LexToken(CLOSE_CURLY,'}',7,163)
```