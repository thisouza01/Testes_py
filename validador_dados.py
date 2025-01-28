
def valida_nome(nome):
    # verifica se nome é string
    if not isinstance(nome, str):
        return False
    # retorna se o nome for maior que 2 caracteres, nao conter numero ou caracter especial e pode conter espaço
    return len(nome) > 2 and all(str(char).isalpha() or str(char).isspace() for char in nome)


def valida_preco(preco):
    # retorna se o preço for uma instancia de int ou float e for maior que 0
    return isinstance(preco, (int, float)) and preco >= 0


def valida_preferencia(preferencia):
    # retorna se a preferencia for 'sol' ou 'sombra'
    return str(preferencia).lower() in ['sol', 'sombra']