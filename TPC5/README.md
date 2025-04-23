# 📝 TPC5

Neste TPC, o objetivo é construir uma simulação de uma **máquina de vending** 🥤 usando o módulo `ply.lex`, explorando a gestão de estados exclusivos no analisador léxico. A máquina permite inserir moedas, selecionar produtos e consultar o saldo, mantendo a persistência de dados através de um ficheiro JSON.

### Requirements
```shell
pip install ply
```

## Usage
Para correr o programa, utilize o seguinte comando:
```shell
python tpc5.py
```

A máquina interage com o utilizador através de comandos de texto. No final da execução, o stock atualizado é guardado automaticamente no ficheiro `stock.json`.

### Comandos Disponíveis
| Comando         | Descrição                                               |
|----------------|---------------------------------------------------------|
| `SHOW`         | Lista todos os produtos em stock 📋                     |
| `BALANCE`      | Mostra o saldo atual 💵                                  |
| `INSERT X`     | Insere moeda(s) `X` na máquina (ex: `INSERT 1e,50c`) 🪙 |
| `SELECT Y`     | Seleciona o produto com código `Y` (ex: `SELECT A01`) 🛍️ |
| `EXIT`         | Sai do programa e devolve o troco 🚪💰                  |

**Atenção**: A máquina aceita apenas as seguintes moedas:
`2e, 1e, 50c, 20c, 10c, 5c, 2c, 1c`

## Author
<p><strong>Name:</strong> Fábio Magalhães</p>
<p><strong>Number:</strong> A104365</p>

## Results

### ✅ Testes de Funcionamento
- Inserção de moedas individuais e múltiplas.
- Seleção de produtos com saldo suficiente.
- Verificação correta do saldo.
- Listagem do stock.

### ⚠️ Testes de Erro
- Compra com saldo insuficiente.
- Código de produto inexistente.
- Produto com stock esgotado.
- Comando inválido.

### 🔄 Persistência
- O ficheiro `stock.json` é atualizado após cada operação de compra.
- A informação mantida entre sessões garante continuidade de stock.