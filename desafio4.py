EXPRESSA0_ABERTURA = "({["
EXPRESSA0_FECHAMENTO = ")}]"
def validacao_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char in EXPRESSA0_ABERTURA:
            pilha.append(EXPRESSA0_ABERTURA.index(char))
        elif char in EXPRESSA0_FECHAMENTO:
            if pilha[-1] == EXPRESSA0_FECHAMENTO.index(char):
                pilha.pop()
            else:
                return False
    return len(pilha) == 0

if __name__ == "__main__":
    print("✅ Válido") if validacao_parenteses("{[()]}") else print("❌ Inválido")
    print("✅ Válido") if validacao_parenteses("{[(])}") else print("❌ Inválido")
    print("✅ Válido") if validacao_parenteses("{{[[(]]}}") else print("❌ Inválido")