from livro import Livro


class Comedia(Livro):
    def __init__(self, id: int, nome: str, valor: float, quantidade: int):
        super().__init__(id, nome, valor, quantidade)
        self.caracteristica = "Capa Brochura"

    def __str__(self):
        return super(Comedia, self).__str__() + ", caracteristica: " + self.caracteristica
