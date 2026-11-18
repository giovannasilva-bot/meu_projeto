from.livros import livro
from.usuarios import usuario


class emprestimos:
    def __init__(self,livro: livro,usuario: usuario):
        if not livro.disponivel:
            raise ValueError
        self.livro = livro
        self.usuario = usuario
        self.ativo = True
        
        self.livro.disponivel = False

    def devolver(self):
        self.ativo == False
        self.livro.disponivel
            