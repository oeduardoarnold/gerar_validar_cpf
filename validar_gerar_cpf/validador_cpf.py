import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um número de CPF brasileiro verificando formato e dígitos verificadores.
    
    O CPF (Cadastro de Pessoas Físicas) é um documento brasileiro composto por 11 dígitos,
    onde os dois últimos são dígitos verificadores calculados com base nos 9 primeiros.
    
    Formatos aceitos:
    - Com formatação: 123.456.789-10
    - Sem formatação: 12345678910
    - Com espaços extras (serão removidos)
    
    Args:
        cpf (str): String contendo o CPF a ser validado.
                  Pode estar formatado (com pontos e hífen) ou não.
    
    Returns:
        bool: True se o CPF for válido, False caso contrário.
    
    Raises:
        Não lança exceções, apenas retorna False para entradas inválidas.
    
    Examples:
        >>> validar_cpf("123.456.789-09")
        True
        >>> validar_cpf("12345678909")
        True
        >>> validar_cpf("123.456.789-10")
        False
        >>> validar_cpf("abc.def.ghi-jk")
        False
    
    Note:
        A função implementa o algoritmo oficial de validação do CPF usado pela
        Receita Federal do Brasil, que utiliza módulo 11 para calcular os
        dígitos verificadores.
    """
    # Remove espaços em branco no início, meio e fim da string
    cpf = cpf.replace(" ", "")
    
    # Expressões regulares para validar os formatos aceitos
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'           # Formato: 123.456.789-10
    padrao_cpf_sem_formatacao = r'^\d{11}$'                # Formato: 12345678910
    
    # Verifica se o CPF está em um dos formatos válidos
    if not re.match(padrao_cpf_sem_formatacao, cpf) and not re.match(padrao_cpf, cpf):
        print("CPF inválido: formato incorreto.")
        return False
    
    #### ALGORITMO DE VALIDAÇÃO DOS DÍGITOS VERIFICADORES ####
    
    # Remove pontos, hífens e espaços para trabalhar apenas com números
    cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
    
    # CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR
    # Multiplica cada um dos 9 primeiros dígitos por um peso decrescente (10 a 2)
    index = 10  # Peso inicial para o primeiro dígito
    soma = 0    # Acumulador da soma dos produtos
    
    for i in cpf_limpo[:9]:  # Itera pelos primeiros 9 dígitos
        soma += int(i) * index  # Multiplica dígito pelo peso e soma
        index -= 1              # Decrementa o peso para o próximo dígito
    
    # Calcula o primeiro dígito verificador usando módulo 11
    digito_um = 11 - (soma % 11)

    # CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR
    # Multiplica os 10 primeiros dígitos (incluindo o primeiro verificador) por pesos (11 a 2)
    index = 11  # Peso inicial para o segundo dígito
    soma = 0    # Reinicia o acumulador
    
    for i in cpf_limpo[:10]:  # Itera pelos primeiros 10 dígitos (9 originais + 1º verificador)
        soma += int(i) * index  # Multiplica dígito pelo peso e soma
        index -= 1              # Decrementa o peso
    
    # Calcula o segundo dígito verificador usando módulo 11
    digito_dois = 11 - (soma % 11)
   
    # AJUSTE DOS DÍGITOS VERIFICADORES
    # Se o resultado for maior que 9, o dígito verificador deve ser 0
    if digito_um > 9:
        digito_um = 0
    if digito_dois > 9:
        digito_dois = 0
    
    # VERIFICAÇÃO FINAL
    # Compara os dígitos calculados com os fornecidos no CPF
    if int(cpf_limpo[9]) == digito_um:       # Verifica o primeiro dígito verificador
        if int(cpf_limpo[10]) == digito_dois: # Verifica o segundo dígito verificador
            print("CPF válido.")
            return True
    
    # Se chegou até aqui, os dígitos verificadores não conferem
    print("CPF inválido: dígitos verificadores incorretos.")
    return False


if __name__ == "__main__":
    """
    Testes da função validar_cpf com diferentes formatos e casos.
    """
    
    # CPF da Maria com espaços extras e formatação
    maria = "614.826.255-02"
    print(f"Testando CPF da Maria: '{maria}'")
    validar_cpf(maria)
    
    # CPF do João sem formatação e com espaços
    joao = "  145 3822 0620"
    print(f"Testando CPF do João: '{joao}'")
    validar_cpf(joao)

    # Exemplos adicionais para demonstrar diferentes casos
    print("=== CASOS DE TESTE ADICIONAIS ===")
    
    # CPF válido formatado
    print("CPF válido formatado:")
    validar_cpf("123.456.789-09")

    # CPF válido sem formatação
    print("CPF válido sem formatação:")
    validar_cpf("12345678909")
    
    # CPF com formato inválido
    print("CPF com formato inválido:")
    validar_cpf("123.456.789")
    
    # CPF com letras
    print("CPF com caracteres inválidos:")
    validar_cpf("abc.def.ghi-jk")