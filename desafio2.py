def palindromo(s):
    """
    Verifica se a string s é um palíndromo.
    
    Parâmetros:
    s (str): A string a ser verificada.
    
    Retorna:
    bool: True se s for um palíndromo, False caso contrário.
    """
    # Remover espaços e converter para minúsculas
    s = s.replace(" ", "").lower()
    
    # Verificar se a string é igual à sua reversa
    return s == s[::-1]

if __name__ == "__main__":
    string = input("Digite uma string para verificar se é um palíndromo: ")
    if palindromo(string):
        print(f'"{string}" é um palíndromo.')
    else:
        print(f'"{string}" não é um palíndromo.')