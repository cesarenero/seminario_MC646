def calcular_preco_total(valor_unitario, quantidade, cupom=None, frete=20.0):
    """
    Calcula o preço total de um pedido com as seguintes regras:
    - valor_unitario e quantidade devem ser positivos.
    - Se quantidade >= 10, aplica 10% de desconto em cima do subtotal.
    - Cupom "DESC10" dá mais 10% de desconto.
    - Cupom "FRETEGRATIS" zera o frete.
    - Frete só é cobrado se o subtotal > 0.
    """

    if valor_unitario < 0 or quantidade < 0:
        raise ValueError("valor_unitario e quantidade devem ser não negativos")

    subtotal = valor_unitario * quantidade

    # Desconto por quantidade
    if quantidade >= 10:
        subtotal *= 0.9  # 10% de desconto

    # Desconto por cupom
    if cupom == "DESC10":
        subtotal *= 0.9  # mais 10% de desconto
    elif cupom is not None and cupom != "FRETEGRATIS":
        # Cupom inválido não dá desconto
        pass

    # Cálculo de frete
    custo_frete = 0.0
    if subtotal > 0:
        if cupom == "FRETEGRATIS":
            custo_frete = 0.0
        else:
            custo_frete = frete

    total = subtotal + custo_frete
    return round(total, 2)


def eh_pedido_grande(quantidade, valor_unitario, limite=500.0):
    """
    Considera um pedido "grande" se o total bruto (sem desconto) >= limite.
    """
    if quantidade < 0 or valor_unitario < 0:
        raise ValueError("quantidade e valor_unitario devem ser não negativos")

    total_bruto = quantidade * valor_unitario
    return total_bruto >= limite
