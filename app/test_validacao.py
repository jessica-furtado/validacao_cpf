import pytest
from app.validacao import validar_cpf

def test_cpf_valido():
    assert validar_cpf("529.982.247-25") == True

def test_cpf_invalido_digitos_errados():
    assert validar_cpf("529.982.247-26") == False

def test_cpf_todos_iguais():
    assert validar_cpf("111.111.111-11") == False

def test_cpf_com_caracteres():
    assert validar_cpf("529a982b247c25") == True

def test_cpf_com_menos_digitos():
    assert validar_cpf("1234567890") == False

def test_cpf_vazio():
    assert validar_cpf("") == False
