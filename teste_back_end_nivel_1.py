#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

produtos_acima_30 = []
for loja in response:
    produtos = [produto for produto in loja["produtos"] if produto["preço"] > 30]
    if produtos:
        produtos_acima_30.append({
            "nome": loja["nome"],
            "endereço": loja["endereço"],
            "produtos": produtos
        })

print(produtos_acima_30)

# Explicação:
# Utilizei uma compreensão de lista para filtrar os produtos com preço maior que 30 Reais.
# A abordagem garante que os produtos sejam filtrados diretamente dentro do loop e adicionados à lista resultante.

# 2- Use o JSON abaixo para capturar o preço do produto B
responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

preco_produto_b = None
for produto in responsejson["produtos"]:
    if produto["nome"] == "Produto B":
        preco_produto_b = produto["preço"]
        break

print(preco_produto_b)

# Explicação:
# Utilize um laço 'for' para buscar o produto com o nome "Produto B".
# Assim que ele for encontrado, a variável `preco_produto_b` será atribuída com o preço do produto e o loop será interrompido.

# 3- Ordene a lista abaixo em ordem crescente
lista = [5,8,3,0,8,1,9,10,20,30]

lista_ordenada = sorted(lista)
print(lista_ordenada)

# Explicação:
# A função `sorted()` foi usada para retornar uma nova lista ordenada sem alterar a lista original. 
# Essa é a maneira mais simples e eficiente de ordenar uma lista em Python.

# 4- Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela
lista = ["   joao   ","   maria   ","  joana  "]

lista_nova = [nome.strip() for nome in lista]
print(lista_nova)

# Explicação:
# Utilizei a função `strip()` em cada string para remover os espaços em branco no início e no final.
# A compreensão de lista foi usada para gerar uma nova lista com os valores modificados.

# 5- Retire o segundo item dessa lista e imprima ela:
lista = [1,2,3,4,5,6]

lista.pop(1)
print(lista)

# Explicação:
# Usei a função `pop()` com o índice 1 para remover o segundo item da lista. Essa função é eficiente e simples para este propósito.

# 6- Substitua todos os "joao" da lista por "maria"
lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

lista = ["maria" if nome == "joao" else nome for nome in lista]
print(lista)

# Explicação:
# Utilizei uma compreensão de lista com uma condicional para substituir todas as ocorrências de "joao" por "maria".
# Isso permite uma modificação eficiente dos itens da lista.

# 7- Criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5.
lista = [1, 2, 3, 4, 5, 6, 7, 8]

i = 0
while i <= 5:
    print(lista[i])
    i += 1

# Explicação:
# Usei um loop `while` para iterar sobre a lista, imprimindo os itens enquanto a variável `i` for menor ou igual a 5.
# Após cada iteração, `i` é incrementado.

# 8- Usando a biblioteca requests, faça uma requisição HTTP para o endpoint https://jsonplaceholder.typicode.com/todos
import requests

def contar_tasks():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = response.json()

    completadas = len([task for task in tasks if task["completed"]])
    pendentes = len([task for task in tasks if not task["completed"]])

    return completadas, pendentes

completadas, pendentes = contar_tasks()
print(f"Completadas: {completadas}, Pendentes: {pendentes}")

# Explicação:
# Usando a biblioteca `requests`, fiz uma requisição ao endpoint para obter a lista de tasks.
# Depois, filtrei a lista de tasks completadas e pendentes usando compreensões de lista para contá-las.

# 9- Faça uma requisição em uma API https://jsonplaceholder.typicode.com/users e com os dados retornados 
def obter_dados_usuarios():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()

    parsed_users = []
    for user in users:
        parsed_users.append({
            "nome": user["name"],
            "username": user["username"],
            "email": user["email"],
            "rua": user["address"]["street"],
            "numero": user["address"]["suite"]
        })

    return parsed_users

usuarios = obter_dados_usuarios()
print(usuarios)

# Explicação:
# Fiz uma requisição ao endpoint para obter os usuários e extraí as informações necessárias 
# usando uma iteração para acessar os campos desejados.

# 10- Crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO
fila = []

fila.append('novo_item')
print(fila)

# Explicação:
# FIFO (First In, First Out) significa que o primeiro item inserido será o primeiro a ser removido.
# O método `append()` foi usado para adicionar o novo item à fila.

# 11- Crie uma lista e adicione um item novo a ela utilizando a metodologia LIFO
pilha = []

pilha.append('novo_item')
print(pilha)

# Explicação:
# LIFO (Last In, First Out) significa que o último item inserido será o primeiro a ser removido.
# Assim como no FIFO, usamos `append()`, mas o comportamento é diferente no momento de remoção.

# DESAFIO!! - Crie uma interface de banco utilizando POO

class ContaBancaria:
    contador_id = 1

    def __init__(self, nome, cpf):
        self.id = ContaBancaria.contador_id
        ContaBancaria.contador_id += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque não permitido. Saldo insuficiente: R$ {self.saldo}")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")

# Exemplo de uso
conta1 = ContaBancaria("João", "12345678900")
conta1.depositar(100)
conta1.sacar(50)
conta1.exibir_saldo()

# Explicação:
# A classe `ContaBancaria` usa POO para criar uma conta com atributos nome, CPF e saldo. O saldo começa em 0 e o ID é autoincrementado.
# Os métodos `depositar` e `sacar` permitem manipular o saldo da conta e o método `exibir_saldo` permite ver o saldo atual.
