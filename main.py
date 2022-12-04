from livraria import Livraria


def menu():
    livraria = Livraria()
    print("BEM VINDO AO SISTEMA DA LIVRARIA")
    dinheiro = float(input("Digite a quantidade inicial de dinheiro em caixa: "))
    livraria.setDinheiroEmCaixa(dinheiro)

    opcoes = "1 - Consultar estoque de livros\n" \
             "2 - Dinheiro em caixa\n" \
             "3 - Efetuar venda\n" \
             "4 - Efetuar compra de novos livros\n" \
             "5 - Consultar vendas\n" \
             "6 - Sair"

    while True:
        print(opcoes)
        op = int(input("Sua escolha: "))

        if op == 6:
            break
        elif op == 1:
            livraria.consultarEstoque()
        elif op == 2:
            livraria.getDinheiroEmCaixa()
        elif op == 3:
            livraria.efetuarVenda()
        elif op == 4:
            livraria.efetuarCompra()
        elif op == 5:
            livraria.consultarVendas()
        else:
            print("\nOpção inválida\n")


if __name__ == '__main__':
    menu()
