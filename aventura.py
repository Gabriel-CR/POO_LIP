from livro import Livro


class Aventura (Livro):
    def __init__(self, id: int, nome: str, valor: float, quantidade: int):
        super().__init__(id, nome, valor, quantidade)
        self.caracteristica = "Ilustrações"

    def __str__(self):
        return super(Aventura, self).__str__() + ", caracteristica: " + self.caracteristica
