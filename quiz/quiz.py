from typing import List
class Quiz:
    __acertos: int
    __erros: int

    def __init__(self, ac : int, er : int):
     self.__acertos = ac
     self.__erros = er

    def get_acertos(self):
        return self.__acertos
    def get_erros(self):
        return self.__erros
    def calcular_pontos(self):
        return self.__acertos - self.__erros
    def __str__(self):
        info = f'Acertos {self.__acertos} Erros: {self.__erros}\n'
        info += f'Total de Pontos: {self.calcular_pontos()}'
        return info

class Quiz2A(Quiz):

    def calcular_pontos(self):
        return self.get_acertos() - 4 * (self.get_erros())

class Quiz3A(Quiz):

    def calcular_pontos(self):
        return self.get_acertos() - 2 * (self.get_erros())

class Aluno:
    __matricula: int
    __nome : str
    __quizes: List[Quiz]

    def __init__(self, m : int, al : str, kahoot : List[Quiz]):
        self.__matricula = m
        self.__nome = al
        self.__quizes = kahoot

    def __str__(self):
        info = f'Nome do Aluno: {self.__nome}\n'
        info += f'Numero de Matricula: {self.__matricula}\n'
        soma = 0
        for q in self.__quizes:
            soma += q.calcular_pontos()
        info += f'Total de pontos: {soma}\n'
        return info

    def get_matricula(self):
        return self.__matricula
class Disciplina:
    __nome : str
    __professor : str
    __ano : int
    __semestre : int
    __alunos : List[Aluno] = []

    def __init__(self, n : str, p : str, a : int, sem : int):
        self.__nome = n
        self.__professor = p
        self._ano = a
        self.__semestre = sem

    def add_aluno(self, al: Aluno):
        for aluno in self.__alunos:
            if aluno.get_matricula() == al.get_matricula():
                raise Exception('Aluno ja existe')
        self.__alunos.append(al)

    def __str__(self):
        info = f'Disciplina: {self.__nome} Professor: {self.__professor}\n'
        info += f'Ano: {self._ano} Semestre: {self.__semestre}\n'
        for aluno in self.__alunos:
            info+= f'{aluno}'

        return info