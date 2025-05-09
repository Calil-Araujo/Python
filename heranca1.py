class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou aluno do curso de {self.curso}, matrícula {self.matricula}.")

    def estudar(self):
        print(f"O aluno {self.nome} de matrícula {self.matricula} está estudando {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou professor de {self.disciplina}.")

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.disciplina}.")

aluno1 = Aluno("Calil Matos", 24, 2025.05, "Programando com Python")
professor1 = Professor("J. Stalin", 88, "Conquistando o Mundo")

aluno1.apresentar()
aluno1.estudar()

professor1.apresentar()
professor1.dar_aula()

print(f"\nNome do aluno: {aluno1.nome}, matrícula: {aluno1.matricula}.")

print(f"Nome do professor: {professor1.nome}, disciplina: {professor1.disciplina}.")