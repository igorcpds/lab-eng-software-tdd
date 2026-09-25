import unittest
from livraria import filtrar_livros

class TestFiltroLivraria(unittest.TestCase):

    def setUp(self):
        # Base de dados simulada em memória para os testes
        self.livros = [
            {'titulo': '1984', 'autor': 'George Orwell', 'genero': 'Ficção'},
            {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia'},
            {'titulo': 'A Revolução dos Bichos', 'autor': 'George Orwell', 'genero': 'Ficção'},
            {'titulo': 'Fundação', 'autor': 'Isaac Asimov', 'genero': 'Ficção Científica'}
        ]

    def test_filtrar_por_autor(self):
        # Deve retornar 2 livros do George Orwell
        resultado = filtrar_livros(self.livros, autor='George Orwell')
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]['titulo'], '1984')
        self.assertEqual(resultado[1]['titulo'], 'A Revolução dos Bichos')

    def test_filtrar_por_genero(self):
        # Deve retornar 1 livro de Fantasia
        resultado = filtrar_livros(self.livros, genero='Fantasia')
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], 'O Senhor dos Anéis')

    def test_filtrar_multiplos_criterios(self):
        # Deve retornar livros que sejam do Isaac Asimov E de Ficção Científica
        resultado = filtrar_livros(self.livros, autor='Isaac Asimov', genero='Ficção Científica')
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], 'Fundação')

    def test_filtrar_sem_resultados(self):
        # Deve retornar uma lista vazia se nenhum livro corresponder
        resultado = filtrar_livros(self.livros, autor='J.K. Rowling')
        self.assertEqual(len(resultado), 0)

if __name__ == '__main__':
    unittest.main()
