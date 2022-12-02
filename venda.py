from livro import Livro


class Venda:
    def __init__(self, livroVendido: Livro, quantidadeVendida: int):
        self.livroVendido = livroVendido
        self.quantidadeVendida = quantidadeVendida
        self.valorVenda = quantidadeVendida * livroVendido.getValor()

    def __str__(self):
        return f'Livro: {self.livroVendido.getNome()}, quantidade: {self.quantidadeVendida}, valor: {self.valorVenda}'
