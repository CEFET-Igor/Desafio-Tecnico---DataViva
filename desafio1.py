LIMITE = 100
def fizzbuzz():
    """
    Para cada inteiro i no intervalo 1...LIMITE (100), faca o seguinte:
    - se i for divisível por 3 e 5, imprima "FizzBuzz".
    - se i for divisível apenas por 3, imprima "Fizz".
    - se i for divisível apenas por 5, imprima "Buzz".
    - se nao for divisível por nenhum dos dois, imprima o número i.
    """
    for i in range(1, LIMITE + 1): # Loop de 1 a 100
        # Verificação de divisibilidade.
        if i % 3 == 0 and i % 5 == 0: # Verificar divisibilidade por 3 e 5
            s = "FizzBuzz"
        elif i % 3 == 0: # Verificar divisibilidade por 3
            s = "Fizz"
        elif i % 5 == 0: # Verificar divisibilidade por 5
            s = "Buzz"
        else: # Se nenhuma das condições acima for verdadeira, imprimir o número
            s = f"{i}"

        # Formatação
        if i != LIMITE:
            print(s, end=", ") # Separar numeros por vírgula e espaço.
        else:
            print(s, end=".\n") # Ultimo numero.

if __name__ == "__main__":
    fizzbuzz()