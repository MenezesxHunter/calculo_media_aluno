nome = input("Digite o seu Nome:")
numero_da_matricula = input("Digite o número da sua Matrícula:")
nota_do_trabalho = float(input("Digite a nota do seu trabalho:"))
nota_de_exercicios = float(input("Digite a nota de exercícios:"))
nota_de_prova = float(input("Digite a nota de prova:"))
media = (nota_do_trabalho * 0.3 + nota_de_exercicios * 0.2 + nota_de_prova * 0.5)

if 6 <= media <= 10:
    print(f" Parabéns {nome} N° de Matrícula {numero_da_matricula} Aluno Aprovado -  a sua nota é : {media}")
else:
    print(f"Que pena ! {nome}  - Aluno Reprovado")