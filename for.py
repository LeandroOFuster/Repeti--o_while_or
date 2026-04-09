# A estrutura de repetição for é mais adequada para esse tipo de situação, onde queremos repetir um bloco 
# de código um número específico de vezes. O código acima pode ser simplificado usando um loop for, como mostrado abaixo:

numero = int(input("Digite um número para ver a tabuada: "))

for multiplicador in range (1,11):
    print(numero, "x", multiplicador, "=", numero * multiplicador)