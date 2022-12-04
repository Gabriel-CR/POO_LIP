from venda import Venda
from comedia import Comedia
from drama import Drama
from aventura import Aventura


class Livraria:
    def __init__(self):
        self.estoque = {}
        self.venda = []
        self.dinheiroEmCaixa = 0
        self.id = 1

    def setDinheiroEmCaixa(self, dinheiroEmCaixa):
        self.dinheiroEmCaixa = dinheiroEmCaixa
        print(f'Valor inicial de R$ {dinheiroEmCaixa} definido com sucesso\n')

    def getDinheiroEmCaixa(self):
        print(f'\nHá R$ {self.dinheiroEmCaixa} em caixa\n')

    def consultarEstoque(self):
        print(f'\nHá {len(self.estoque)} livro(s) na livraria')
        for livro in self.estoque.values():
            print(f'\t{livro}')
        print()

    def efetuarVenda(self):
        if len(self.estoque) == 0:
            print("\nNão há livros em estoque\n")
        else:
            idLivro = int(input("\nId do livro: "))
            if self.estoque[idLivro] == None:
                print("Livro não encontrado\n")
            else:
                quantidade = int(input("Quantidade a ser vendida: "))
                if self.estoque[idLivro].getQuantidade() < quantidade:
                    print(f'\nNão há {quantidade} unidade(s) do livro {self.estoque[idLivro].getNome()} para serem vendidas\n')
                else:
                    self.estoque[idLivro].setQuantidade(self.estoque[idLivro].getQuantidade() - quantidade)
                    self.dinheiroEmCaixa += quantidade * self.estoque[idLivro].getValor()

                    self.venda.append(Venda(self.estoque[idLivro], quantidade))

                    print(f'\nVenda de {quantidade} unidade(s) do livro {self.estoque[idLivro].getNome()} efetuada com sucesso\n')

    def efetuarCompra(self):
        op = int(input("\t1 - Comprar mais unidades de livro já em estoque\n\t2 - Comprar novo livro\n\tSua escolha: "))

        if op == 1:
            idLivro = int(input("\nId do livro a ser comprado: "))

            if idLivro not in self.estoque:
                print(f'\nLivro com id {idLivro} não encontrado, tente a 2ª opção para cadastrar um novo livro\n')
            else:
                quantidade = int(input("Quantidades a serem compradas: "))
                if self.estoque[idLivro].getValor() * quantidade > self.dinheiroEmCaixa:
                    print(f'\nDinheiro induficiente para realizar compra\n'
                          f'\tDinheiro em caixa: R$ {self.dinheiroEmCaixa}\n'
                          f'\tValor da compra dos livros: R$ {self.estoque[idLivro].getValor() * quantidade}')
                else:
                    self.estoque[idLivro].setQuantidade(self.estoque[idLivro].getQuantidade() + quantidade)
                    self.dinheiroEmCaixa -= self.estoque[idLivro].getValor() * quantidade
                    print(f'\nCompra de {quantidade} unidade(s) do livro {self.estoque[idLivro].getNome()} efetuada com sucesso\n')
        elif op == 2:
            nome = str(input("\nNome do livro: "))
            valor = float(input("Valor do livro: "))
            quantidade = int(input("Quantidade a ser comprada: "))

            if valor * quantidade > self.dinheiroEmCaixa:
                print(f'\nDinheiro insuficiente para realizar compra\n'
                      f'\tDinheiro em caixa: R$ {self.dinheiroEmCaixa}\n'
                      f'\tValor da compra dos livros: R$ {valor * quantidade}\n')
            else:
                tipo = int(input("TIPOS DOS LIVROS\n"
                                 "\t1 - Comedia\n"
                                 "\t2 - Drama\n"
                                 "\t3 - Aventura\n"
                                 "Tipo do livro: "))
                if tipo == 1:
                    self.estoque[self.id] = Comedia(self.id, nome, valor, quantidade)
                    self.id += 1
                    self.dinheiroEmCaixa -= valor * quantidade
                    print(f'\nCompra de {quantidade} unidades do livro {nome} efetuada com sucesso\n')
                elif tipo == 2:
                    self.estoque[self.id] = Drama(self.id, nome, valor, quantidade)
                    self.id += 1
                    self.dinheiroEmCaixa -= valor * quantidade
                    print(f'\nCompra de {quantidade} unidades do livro {nome} efetuada com sucesso\n')
                elif tipo == 3:
                    self.estoque[self.id] = Aventura(self.id, nome, valor, quantidade)
                    self.id += 1
                    self.dinheiroEmCaixa -= valor * quantidade
                    print(f'\nCompra de {quantidade} unidades do livro {nome} efetuada com sucesso\n')
                else:
                    print("\nTipo inválido\n")
        else:
            print(f'Opção {op} inválida')

    def consultarVendas(self):
        print(f'\nHá {len(self.venda)} vendas realizadas')
        for venda in self.venda:
            print(f'\t{venda}')
        print()
