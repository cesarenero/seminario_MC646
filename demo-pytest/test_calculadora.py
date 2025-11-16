# test_calculadora.py

import pytest
from calculadora import calcular_preco_total, eh_pedido_grande


def test_preco_total_sem_desconto():
    total = calcular_preco_total(valor_unitario=10.0, quantidade=2)
    # subtotal = 20, frete = 20 -> total = 40
    assert total == 40.0


def test_preco_total_com_desconto_por_quantidade():
    total = calcular_preco_total(valor_unitario=10.0, quantidade=10)
    # subtotal = 100, desconto 10% -> 90, frete 20 -> 110
    assert total == 110.0


def test_preco_total_com_cupom_desc10():
    total = calcular_preco_total(valor_unitario=50.0, quantidade=2, cupom="DESC10")
    # subtotal = 100, desc10% -> 90, frete 20 -> 110
    assert total == 110.0


def test_preco_total_com_frete_gratis():
    total = calcular_preco_total(valor_unitario=50.0, quantidade=2, cupom="FRETEGRATIS")
    # subtotal = 100, frete grátis -> 100
    assert total == 100.0


def test_preco_total_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_preco_total(valor_unitario=-1.0, quantidade=5)


def test_eh_pedido_grande_true():
    assert eh_pedido_grande(quantidade=20, valor_unitario=30.0) is True


def test_eh_pedido_grande_false():
    assert eh_pedido_grande(quantidade=5, valor_unitario=10.0) is False


def test_eh_pedido_grande_valor_invalido():
    with pytest.raises(ValueError):
        eh_pedido_grande(quantidade=-1, valor_unitario=10.0)
