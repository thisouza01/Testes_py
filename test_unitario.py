import pytest

# função de receber dados

def recebe_nome(nome):
    return len(nome) > 2 and all(str(char).isalpha() or str(char).isspace() for char in nome)
# nome nao pode ser menor que 3 caracteres
# nome não pode conter numero
# nome pode conter espaços
def test_recebe_nome():
    assert recebe_nome('aaa') == True

# preço nao pode conter letras e caracteres especiais
# preço não pode ser negativo

# preferencia nao pode conter numeros
# tem que ser 'sol' ou 'sombra'
