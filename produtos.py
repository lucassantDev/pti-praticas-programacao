listaProdutos = []
print("----------------------Cadastrar Produto----------------------")
while True:
    produtoCadastrado = {}

    # utilizando o método any para validar se existe algum código repetido no dicionario
    codigo = int(input("Digite o código do produto: "))
    while any(produto['Código'] == codigo for produto in listaProdutos):
        print("---------------------------------------------")
        print('Informe um código de produto diferente!!!')
        print("---------------------------------------------")
        codigo = int(input("Digite o código do produto: "))
    produtoCadastrado['Código'] = codigo

    produtoCadastrado['Nome'] = str(input("Informe o nome do produto: "))

    # utilizando uma váriavel momentânea para validação do valor
    valor = float(input(f"Digite o valor do(a) {produtoCadastrado['Nome']}: R$ "))
    while valor <= 0:
        print("---------------------------------------------")
        print('Informe um valor válido!')
        valor = float(input(f"Digite o valor do(a) {produtoCadastrado['Nome']}: R$ "))
    produtoCadastrado['Valor'] = valor
    
    # utilizando outra váriavel momentânea para a validação da quantidade
    quantidade = int(input("Informe também a quantidade: "))
    while quantidade <= 0:
        print("---------------------------------------------")
        print('Informe uma quantidade válida!')
        quantidade = int(input("Informe a quantidade corretamente: "))
    produtoCadastrado['Quantidade'] = quantidade

    listaProdutos.append(produtoCadastrado)
    print(produtoCadastrado)
    finalizar_programa = input("Deseja sair: (S/N): ")
    print("-------------------------------------------------------------------------------------")
    if finalizar_programa.upper() == "S":
        break

# essa é uma função para mostrar a quantidade total de produtos no estoque
def quantidadeEstoque(produtos):
    somaQtd = 0
    for produto in produtos:
        somaQtd += produto['Quantidade']
    return f"Total de produtos no estoque: {somaQtd}"

# já essa é uma função para mostrar o valor total dos produtos em estoque
def somaValorProdutos(produtos):
    valorTotal = 0
    for produto in produtos:
        valorTotal += produto['Quantidade'] * produto['Valor']

    return f"O valor total dos produtos é de R${valorTotal}" 

print(somaValorProdutos(listaProdutos))
print(quantidadeEstoque(listaProdutos))


