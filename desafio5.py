def somar_valores_por_categoria(dados: list) -> dict:
    resultado = {}

    for registro in dados:                  # Percorre cada registro na lista
        categoria = registro["categoria"]   # Obtém a categoria do registro
        valor = registro["valor"]           # Obtém o valor do registro

        if categoria in resultado:          # Verifica se a categoria já está no resultado
            resultado[categoria] += valor
        else:                               # Se não estiver, inicializa com o valor atual 
            resultado[categoria] = valor

    return resultado


if __name__ == "__main__":
    dados_teste = [
        {"categoria": "Alimentação", "valor": 10},
        {"categoria": "Transporte", "valor": 5},
        {"categoria": "Alimentação", "valor": 20},
        {"categoria": "Lazer", "valor": 50},
    ]

    print(somar_valores_por_categoria(dados_teste))
