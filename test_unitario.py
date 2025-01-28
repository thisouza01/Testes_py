


def valida_nome(nome):
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




def test_valida_nome():
    assert valida_nome('') == False         # Testa nome contendo string vazia
    assert valida_nome('aa') == False       # Testa nome com menos de 3 caracteres
    assert valida_nome('aa1') == False      # Testa nome contendo string numero
    assert valida_nome('@@@') == False      # Testa nome contendo caracteres especiais
    assert valida_nome(1111) == False       # Testa nome contendo numeros
    assert valida_nome('aaa aa') == True
    assert valida_nome('aaa') == True 

def test_valida_preco():
    assert valida_preco('') == False        # Testa preço contendo string vazia
    assert valida_preco('aaa') ==  False    # Testa preço contendo caracteres
    assert valida_preco(-5) == False        # Testa preço negativo
    assert valida_preco('10') == False      # Testa preço em string
    assert valida_preco('$10') == False     # Testa preço em string com caracter special
    assert valida_preco(1000) == True
    assert valida_preco(0) == True 

def test_valida_preferencia():
    assert valida_preferencia('') == False      # Testa preferencia com string vazia
    assert valida_preferencia('1111') == False  # Testa preferencia com string contendo numeros
    assert valida_preferencia('@@@') == False   # Testa preferencia contendo caracteres especiais
    assert valida_preferencia(1111) == False    # Testa preferencia contendo numeros
    assert valida_preferencia('   ') == False   # Testa preferencia coantendo espaços vazios
    assert valida_preferencia('Sol') == True
    assert valida_preferencia('Sombra') == True
    assert valida_preferencia('sol') == True
    assert valida_preferencia('sombra') == True