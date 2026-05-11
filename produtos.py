listaProdutos = []
valorProdutos = []

print("----------------------Cadastrar Produto----------------------")
while True:
    produtoCadastrado = {}
    produtoCadastrado['Código'] = int(input("Digite o código do produto: "))
    produtoCadastrado['Nome'] = input("Informe o nome do produto: ")
    produtoCadastrado['Valor'] = float(input(f"Digite o valor do(a) {produtoCadastrado['Nome']}: R$ "))
    produtoCadastrado['Quantidade'] = int(input("Informe também a quantidade: "))

    valorProdutos.append(produtoCadastrado['Valor'])
    listaProdutos.append(produtoCadastrado)
    print(produtoCadastrado)
    finalizar_programa = input("Deseja sair: (S/N)")
    if finalizar_programa.upper() == "S":
        break



def somaValorProdutos(valorProdutos):
    soma = 0
    for valor in valorProdutos:
        soma += valor
    return f"O valor total dos produtos é de R${soma}" 

print(somaValorProdutos(valorProdutos))

print("\nProdutos cadastrados:")
for produto in listaProdutos:
    print(produto)
it
