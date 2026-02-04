def encontrar_duplicatas(lista):
    """Recebe uma lista e retorna os elementos duplicados."""
    vistos = set()
    duplicatas = set()
    
    for item in lista:              # Percorre cada item na lista
        if item in vistos:          # Verifica se o item já foi visto
            duplicatas.add(item)
        else:                       # Se não foi visto, adiciona aos vistos
            vistos.add(item)
    
    return list(duplicatas)

if __name__ == "__main__":
    print(encontrar_duplicatas([1, 2, 3, 4, 2, 5]))