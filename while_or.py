# A estrutura de repetição while é mais adequada para situações onde não 
# sabemos exatamente quantas vezes o bloco de código deve ser repetido, ou quando 
# queremos repetir o bloco de código enquanto uma determinada condição for verdadeira. O código acima 
# pode ser simplificado usando um loop while, como mostrado abaixo:

numero = int(input("Digite um número para ver a Tabuada:"))

contador = 1

while contador <= 10: 
    print(numero, "x", contador, "=", numero * contador) 
    contador += 1 


