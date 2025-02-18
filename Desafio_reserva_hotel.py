print('SEJA BEM VINDO AO HOTEL!!!') 

qrtdade_hospides = int(input('Digite para quantos hospides é a reserva: '))

nomes = []
idades = []

for i in range(0,qrtdade_hospides):
    nome1 = input('Digite o nome: ')
    nomes.append(nome1)
    idade1 = input('Digite a idade: ')
    idades.append(idade1)

print('Tipos de dormitorios disponiveis:')
print('Dormitorio - Simples R$100,00\nDormitorio - Duplo R$150,00\nDormitorio - Luxo R$250,00')

tipos_quartos = ["", "", ""]
dias_estadia = [0, 0, 0]
valores_estadia = [0, 0, 0]

for i in range(qrtdade_hospides):
    tipos_quartos[i] = input("Digite o tipo de quarto escolhido: ")
    dias_estadia[i] = int(input("Digite os dias de estadia: "))

    if tipos_quartos[i] == "Simples":
        valores_estadia[i] = 100 * dias_estadia[i]
    elif tipos_quartos[i] == "Duplo":
        valores_estadia[i] = 150 * dias_estadia[i]
    elif tipos_quartos[i] == "Luxo":
        valores_estadia[i] = 250 * dias_estadia[i]

print("\n--- Resultados ---")

for i in range(qrtdade_hospides):
    print(f"\nCliente {i+1}:")
    print("Nome:", nomes[i])
    print("Quarto:", tipos_quartos[i])
    print("Dias:", dias_estadia[i])
    print("Valor: R$", valores_estadia[i])