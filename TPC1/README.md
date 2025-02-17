# 📝 TPC1

Neste TPC foi realizado o *Somador On/Off*. Na pasta está presente o script de aprendizagem e testagem de conceitos `rec_inteiros.py` bem como o script `somadoronoff.py` que implementa a tarefa pedida.
Foi pretendida nesta tarefa a implementação de um somador **SEM O USO DE REGEXP** que soma números inteiros apartir da inicialização do somador (com a palavra *on*) até ao seu desligamento (com a palavra *off*). O somador é inicializado com o valor 0 e a cada iteração é somado um número inteiro ao valor do somador. O somador apenas apresenta na consola o valor do somador até ao momento quando o caracter `=` é introduzido.

## Author
<p><strong>Name:</strong> Fábio Magalhães</p>
<p><strong>Number:</strong> A104365</p>

## Results
Foi verificado que sem expressões regulares (RegExp) a implementação do somador é mais complexa e menos eficiente. A implementação do somador sem expressões regulares é mais complexa pois é necessário verificar se a palavra *on* ou *off* está presente na string de input bem como a filtragem dos digitos na linha.
Tal problema foi ultrapassado colocando todo o input num mesmo formato o que pode ter impacto na eficiência do programa e possiveis erros.

Para iniciar o programa pode ser utilizado:
```bash
python .\somadoronoff.py
```

You can also test the result by pasting on your stdin the following:
```
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=OfF
E deu-nos 7=
dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!=
```

And the wanted result should be:
```
Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=OfF
>> 2032
E deu-nos 7=
>> 2032
dias para o fazer... ON
Cada trabalho destes vale 0.25 valores da nota final!=
>> 2057
```

or you can run the unit testing script using:
```bash
python -m unittest test_somadoronoff.py
```