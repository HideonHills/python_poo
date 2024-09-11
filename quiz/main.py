from quiz import *

if __name__ == '__main__':
    q1 = Quiz2A(5, 4)
    q2 = Quiz3A(10, 7)

    print(q1)
    print(q2)

    lista_qs = [q1,q2]
    a1 = Aluno(1, "Jorge", lista_qs)
    a2 = Aluno(2, "Cleyton", lista_qs)

    d = Disciplina("POO", "FERAUCHE", 2024, 4)
    d.add_aluno(a1)
    d.add_aluno(a2)
    print(d)