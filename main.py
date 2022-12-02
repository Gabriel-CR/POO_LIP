from biblioteca import Biblioteca


def menu():
    biblioteca = Biblioteca()
    print("BEM VINDO AO SISTEMA DA BIBLIOTECA")
    dinheiro = float(input("Digite a quantidade inicial de dinheiro em caixa: "))
    biblioteca.setDinheiroEmCaixa(dinheiro)

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
            biblioteca.consultarEstoque()
        elif op == 2:
            biblioteca.getDinheiroEmCaixa()
        elif op == 3:
            biblioteca.efetuarVenda()
        elif op == 4:
            biblioteca.efetuarCompra()
        elif op == 5:
            biblioteca.consultarVendas()
        else:
            print("\nOpção inválida\n")


if __name__ == '__main__':
    menu()
