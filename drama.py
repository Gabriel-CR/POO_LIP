from livro import Livro


class Drama (Livro):
    def __init__(self, id: int, nome: str, valor: float, quantidade: int):
        super().__init__(id, nome, valor, quantidade)
        self.caracteristica = "Capa Dura"

    def __str__(self):
        return super(Drama, self).__str__() + ", caracteristica: " + self.caracteristica
