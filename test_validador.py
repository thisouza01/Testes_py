import pytest
from validador import *

# Parâmetros para testar função " nome "
@pytest.mark.parametrize('nome, esperado', [
    # tuplas com valores para teste
    ('', False),                        # Testa nome contendo string vazia
    ('aa', False),                      # Testa nome com menos de 3 caracteres
    ('aa1', False),                     # Testa nome contendo string numero
    ('@@@', False),                     # Testa nome contendo caracteres especiais
    (1111, False),                      # Testa nome contendo numeros
    ('aaaa aaaa', True),
    ('aaa', True)
])

def test_valida_nome(nome, esperado):
    assert valida_nome(nome) == esperado

# Parâmetros para testar função " preço "
@pytest.mark.parametrize('preco, esperado', [
    ('', False),                       # Testa preço contendo string vazia 
    ('aaa', False),                    # Testa preço contendo caracteres
    (-5, False),                       # Testa preço negativo
    ('10', False),                     # Testa preço em string
    ('$10', False),                    # Testa preço em string com caracter special
    (1000, True),
    (0, True)
])

def test_valida_preco(preco, esperado):
    assert valida_preco(preco) == esperado


# Parâmetros para testar função " preferencia "
@pytest.mark.parametrize('preferencia, esperado', [
    ('', False),                        # Testa preferencia com string vazia
    ('1111', False),                    # Testa preferencia com string contendo numeros
    ('@@@', False),                     # Testa preferencia contendo caracteres especiais
    (1111, False),                      # Testa preferencia contendo numeros
    ('    ', False),                    # Testa preferencia coantendo espaços vazios
    ('Sol', True),
    ('sol', True),
    ('Sombra', True),
    ('sombra', True)
])

def test_valida_preferencia(preferencia, esperado):
    assert valida_preferencia(preferencia) == esperado