listaProdutos = []


print("----------------------Cadastrar Produto----------------------")
while True:
    produtoCadastrado = {}
    produtoCadastrado['Código'] = int(input("Digite o código do produto: "))
    produtoCadastrado['Nome'] = input("Informe o nome do produto: ")
    produtoCadastrado['Valor'] = float(input(f"Digite o valor do(a) {produtoCadastrado['Nome']}: R$ "))
    produtoCadastrado['Quantidade'] = int(input("Informe também a quantidade: "))

    listaProdutos.append(produtoCadastrado)
    print(produtoCadastrado)
    finalizar_programa = input("Deseja sair: (S/N): ")
    print("-------------------------------------------------------------------------------------")
    if finalizar_programa.upper() == "S":
        break

def quantidadeEstoque(produtos):
    somaQtd = 0
    for produto in produtos:
        somaQtd += produto['Quantidade']
    return f"Total de produtos no estoque: {somaQtd}"


def somaValorProdutos(produtos):
    valorTotal = 0
    for produto in produtos:
        valorTotal += produto['Quantidade'] * produto['Valor']
        
    return f"O valor total dos produtos é de R${valorTotal}" 

print(somaValorProdutos(listaProdutos))
print(quantidadeEstoque(listaProdutos))


