def cpf_invalido(cpf):
    return not len(cpf) == 11


def nome_invalido(nome):
    return not nome.isalpha()


def celular_invalido(celular):
    # vamos melhorar essa validação com regex abaixo
    # return not len(celular) == 13

    # padrão ==> XX XXXXX-XXXX
    modelo = r'\d{2} \d{5}-\d{4}'
    resposta = re.findall(modelo, celular)
    return not len(celular) == 13 or not resposta
