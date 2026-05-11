listaProdutos = []

# cadastra um novo produto no estoque com validações | opção número 1
def cadastrar_produto():
    print("\n" + "="*50)
    print("CADASTRAR PRODUTO")
    print("="*50)
    
    produtoCadastrado = {}

    # utilizando o método any para validar se existe algum código de algum produto repetido no dicionário
    codigo = int(input("Digite o código do produto: "))
    while any(produto['Código'] == codigo for produto in listaProdutos):
        print("---------------------------------------------")
        print('Informe um código de produto diferente!!!')
        print("---------------------------------------------")
        codigo = int(input("Digite o código do produto: "))
    produtoCadastrado['Código'] = codigo

    produtoCadastrado['Nome'] = str(input("Informe o nome do produto: "))

    # utilizando uma váriavel para validação do valor
    valor = float(input(f"Digite o valor do(a) {produtoCadastrado['Nome']}: R$ "))
    while valor <= 0:
        print("---------------------------------------------")
        print('Informe um valor válido!')
        valor = float(input(f"Digite o valor do(a) {produtoCadastrado['Nome']}: R$ "))
    produtoCadastrado['Valor'] = valor
    
    # utilizando outra váriavel para a validação da quantidade
    quantidade = int(input("Informe também a quantidade: "))
    while quantidade <= 0:
        print("---------------------------------------------")
        print('Informe uma quantidade válida!')
        quantidade = int(input("Informe a quantidade corretamente: "))
    produtoCadastrado['Quantidade'] = quantidade

    listaProdutos.append(produtoCadastrado)
    print("\n Produto cadastrado com sucesso!")
    print(produtoCadastrado)


# essa é uma função para mostrar a quantidade total de produtos no estoque
def quantidadeEstoque(produtos):
    somaQtd = 0
    for produto in produtos:
        somaQtd += produto['Quantidade']
    return somaQtd

# já essa é uma função para mostrar o valor total dos produtos em estoque
def somaValorProdutos(produtos):
    valorTotal = 0
    for produto in produtos:
        valorTotal += produto['Quantidade'] * produto['Valor']
    return valorTotal

# exibe tanto o total de produtos(qtd) quanto o valor máximo | opção número 2 no menu
def calcular_total_produtos():
    print("\n" + "="*50)
    print("TOTAL DE PRODUTOS EM ESTOQUE")
    print("="*50)
    
    if len(listaProdutos) == 0:
        print("Nenhum produto cadastrado.")
        return
    
    total_qtd = quantidadeEstoque(listaProdutos)
    total_valor = somaValorProdutos(listaProdutos)
    
    print(f"Quantidade total de produtos: {total_qtd}")
    print(f"Valor total do estoque: R${total_valor:.2f}")


# aqui, é exibido o estoque completo com númeração | opção número 3 no menu
def exibir_estoque_completo():
    print("\n" + "="*50)
    print("ESTOQUE COMPLETO")
    print("="*50)
    
    if len(listaProdutos) == 0:
        print("Nenhum produto cadastrado.")
        return
    
    for i, produto in enumerate(listaProdutos, 1):
        print(f"\n[{i}] Código: {produto['Código']}")
        print(f"    Nome: {produto['Nome']}")
        print(f"    Preço: R${produto['Valor']:.2f}")
        print(f"    Quantidade: {produto['Quantidade']}")
        print(f"    Valor Total: R${produto['Valor'] * produto['Quantidade']:.2f}")

# função do menu com quatro opções
def menu():
    while True:
        print("\n" + "="*50)
        print("  SISTEMA DE CONTROLE DE ESTOQUE")
        print("="*50)
        print("1. Cadastrar Produto")
        print("2. Calcular Total de Produtos em Estoque")
        print("3. Exibir Estoque Completo")
        print("4. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            calcular_total_produtos()
        elif opcao == "3":
            exibir_estoque_completo()
        elif opcao == "4":
            print("\n✓ Encerrando o programa. Até logo!")
            break
        else:
            print("\nErro: Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()


