"""Este projeto será sobre a criação de um programa para ajudar pessoas a otimizarem a escolha de matérias
durante a graduação (por enquanto, só Software) levando em conta pré-requisitos e cadeias.

Talvez transformar em números a quantidade de matérias que trancam outra? Mostrar a ementa de cada disciplina?
Talvez mostrar a quantidade de créditos de cada disciplina? Contabilizar pesquisa e extensão também?

O que deve ter em cada classe: quantidade de disciplinas que trancam, lista de disciplinas que trancam"""

#Classes maiores
class Materia: 
    def __init__(self, nome, codigo, creditos, pre_requisito, status):
        self.nome = nome
        self.codigo = codigo #código da matéria
        self.creditos = creditos
        self.pre_requisito = pre_requisito #numero de creditos de materias que ela desbloqueia  
        self.status = status #0 para não cursada, 1 para cursada ou cursando

#Dicionário com as matérias já cursadas ou que o usuário está cursando
materias = {
    "C1": Materia("Cálculo 1", "MAT113034", 6, 22, 0),
    #"APC": Materia("Algoritmos e Programação de Computadores", "CIC113476", 6, X, 0), 
    "DIAC": Materia("Desenho Industrial Assistido por Computador", "FGA199176", 6, 0, 0), 
    "EA": Materia("Engenharia e Ambiente", "FGA198005", 4, 0, 0), 
    "IE": Materia("Introdução à Engenharia", "FGA198013", 2, 0, 0), 
    "C2": Materia("Cálculo 2", "MAT113042", 6, 4, 0),
    "F1": Materia("Física 1", "IFD118001", 4, 0, 0),
    "F1E": Materia("Física 1 Experimental", "IFD118010", 2, 0, 0),
    "IAL": Materia("Introdução à Álgebra Linear", "MAT113093", 4, 26, 0),
    "PE": Materia("Probabilidade e Estatística Aplicada à Engenharia", "FGA195332", 4, 0, 0),
    "MNE": Materia("Métodos Numéricos para Engenharia", "FGA195413", 4, 0, 0),
    "EE": Materia("Engenharia Econômica", "FGA193321", 4, 8, 0),
    "H": Materia("Humanidades e Cidadania", "FGA198021", 2, 0, 0),
    "TED1": Materia("TED1", "FGA119482", 4, 20, 0),
    "PED1": Materia("PED1", "FGA119466", 2, 0, 0),
    #"OO": Materia("Orientação a Objetos", "FGA195341", 4, X, 0),

}

"""Criar menu para a pessoa colocar quais matérias já cursou, ainda vai cursar ou está cursando - implementar
com interface gráfica se possível. Talvez criar um sistema de login para salvar as informações do aluno?
Talvez criar um sistema de recomendação de matérias baseado no que o aluno já cursou? Conversar com o pessoal do MinhaGrade?"""

#Criar um menu para a pessoa escolher o que quer fazer
def menu():
    print("1 - Cadastrar matérias obrigatórias cursadas ou cursando")
    print("2 - Sair")

menu()
opcao = int(input("\nDigite a opção desejada: "))

while opcao != 2:
    if opcao == 1:
        print("\nQuais matérias obrigatórias você já cursou ou está cursando?")
        materias_cursadas_ou_cursando = input("\nQuais matérias obrigatórias você está cursando ou já cursou? (separe por vírgulas): ").split(',')
    else:
        print("\nOpção inválida. Por favor, digite 1 para cadastro ou 2 para sair do programa")
    
    print()
    menu()
    opcao = int(input("\nDigite a opção desejada: "))

print("\nPrograma encerrado")


        

        





#Criar um dicionário com as matérias 

#Criar um dicionário com as matérias que trancam outras matérias

"""
*** Matérias de Engenharia de Software ***
Cálculo 1[3]: Cálculo 2; Probabilidade e Estatística Aplicada à Engenharia; Métodos Numéricos para Engenharia; 
Algoritmos e Programação de Dados[3]: Orientação a Objetos; Estrutura de Dados; Projeto e Análise de Algoritmos;
Orientação a Objetos[4]: Paradigmas de Programação; Métodos de Desenvolvimento de Software; Projeto Integrador de Engenharia 1; Projeto Integrador de Engenharia 2; 
Métodos de Desenvolvimento de Software[9]: Interação Humano Computador; Qualidade de Software 1; Requisitos de Software; Arquitetura e Desenho de Software; Técnicas de Programação em Plataformas Emergentes; Engenharia de Produto de Software; Testes de Software; Gerência de Configuração e Evolução de Software; Projeto Integrador de Engenharia 2; 
Estrutura de Dados[5]: Compiladores 1; Paradigmas de Programação; Estrutura de Dados 2; Programação para Sistemas Paralelos e Distribuídos; Projeto e Análise de Algoritmos;
Desenho Industrial Assistido por Computador[1]
Engenharia e Ambiente[1]
Estágio Supervisionado[1]
Trabalho de Conclusão de Curso 1[2]: Trabalho de Conclusão de Curso 2;
Física 1[1]
Física 1 Experimental[1]
Humanidades e Cidadania[1]
Introdução à Engenharia[1]
Engenharia Econômica[2]: Gestão da Produção e Qualidade; Qualidade de Software 1;
Matemática Discreta 1[3]: Matemática Discreta 2; Sistemas de Banco de Dados 1; Sistemas de Banco de Dados 2;
Introdução à Álgebra Linear[6]: TED/PED1; Fundamentos de Arquitetura de Computadores; Fundamentos de Sistemas Operacionais; Fundamentos de Redes de Computadores; Programação para Sistemas Paralelos e Distribuídos [sequência acaba aqui]; Fundamentos de Sistemas Embarcados.
"""