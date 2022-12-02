class Livro:
    def __init__(self, id: int, nome: str, valor: float, quantidade: int):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def __str__(self):
        return f'[{self.id}] : {self.nome}, valor: R$ {self.valor}, quantidade em estoque: {self.quantidade}'
