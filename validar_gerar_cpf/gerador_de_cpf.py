import re
import random

def gerar_cpf() -> str:
    """
    Gera um número de CPF brasileiro válido com formatação.
    
    Esta função cria um CPF válido gerando aleatoriamente os 9 primeiros dígitos
    e calculando os 2 dígitos verificadores usando o algoritmo oficial da Receita Federal.
    
    O CPF (Cadastro de Pessoas Físicas) é um documento brasileiro composto por 11 dígitos,
    onde os dois últimos são dígitos verificadores calculados com base nos 9 primeiros
    usando o algoritmo de módulo 11.
    
    Processo de geração:
    1. Gera 9 dígitos aleatórios (0-9)
    2. Calcula o primeiro dígito verificador
    3. Calcula o segundo dígito verificador
    4. Formata no padrão XXX.XXX.XXX-XX
    
    Args:
        Nenhum parâmetro necessário.
    
    Returns:
        str: CPF válido formatado no padrão XXX.XXX.XXX-XX (ex: "123.456.789-09")
    
    Raises:
        Não lança exceções. Sempre retorna um CPF válido.
    
    Examples:
        >>> cpf = gerar_cpf()
        >>> print(cpf)
        "123.456.789-09"
        
        >>> # Gerando múltiplos CPFs
        >>> for i in range(3):
        ...     print(gerar_cpf())
        "987.654.321-00"
        "456.789.123-45"
        "321.654.987-12"
    
    Note:
        - Os CPFs gerados são matematicamente válidos mas fictícios
        - Cada execução gera um CPF diferente (números aleatórios)
        - Implementa o algoritmo oficial de validação da Receita Federal
        - CPFs gerados NÃO devem ser usados para fins oficiais/legais
    """
    # GERAÇÃO DOS 9 PRIMEIROS DÍGITOS ALEATÓRIOS
    cpf = ""
    for i in range(9):
        cpf += str(random.randint(0, 9))  # Gera dígito aleatório de 0 a 9
    
    #### ALGORITMO DE VALIDAÇÃO DOS DÍGITOS VERIFICADORES ####
    # CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR
    # Multiplica cada um dos 9 primeiros dígitos por um peso decrescente (10 a 2)
    index = 10  # Peso inicial para o primeiro dígito
    soma = 0    # Acumulador da soma dos produtos
    
    for i in cpf[:9]:  # Itera pelos primeiros 9 dígitos
        soma += int(i) * index  # Multiplica dígito pelo peso e soma
        index -= 1              # Decrementa o peso para o próximo dígito
    
    # Calcula o primeiro dígito verificador usando módulo 11
    digito_um = 11 - (soma % 11)

    # CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR
    # Multiplica os 10 primeiros dígitos (incluindo o primeiro verificador) por pesos (11 a 2)
    index = 11  # Peso inicial para o segundo dígito
    soma = 0    # Reinicia o acumulador

    for i in cpf[:9]+str(digito_um):  # Itera pelos primeiros 10 dígitos (9 originais + 1º verificador)
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

    # FORMATAÇÃO FINAL DO CPF
    # Aplica a formatação padrão XXX.XXX.XXX-XX
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito_um}{digito_dois}"
    return cpf_formatado


if __name__ == "__main__":
    """
    Demonstração da função gerar_cpf com múltiplos exemplos.
    
    Este bloco de teste mostra a geração de vários CPFs válidos
    para demonstrar a funcionalidade da função.
    """
    
    print("=== GERADOR DE CPF VÁLIDO ===")
    print("Gerando CPFs válidos aleatórios:\n")
    
    # Gera e exibe um CPF
    novo_cpf = gerar_cpf()
    print(f"CPF gerado: {novo_cpf}")
    
    # Gera múltiplos CPFs para demonstrar a aleatoriedade
    print("\nGerando mais 5 CPFs para demonstrar aleatoriedade:")
    for i in range(5):
        cpf = gerar_cpf()
        print(f"CPF {i+1}: {cpf}")
    
    print("\nATENÇÃO: Estes CPFs são válidos matematicamente,")
    print("   mas são fictícios e NÃO devem ser usados para fins oficiais!")
    
    # Opcional: teste de integração com validador
    try:
        from app.utils.validador_cpf import validar_cpf
        print(f"\n=== TESTE DE INTEGRAÇÃO ===")
        cpf_teste = gerar_cpf()
        print(f"CPF gerado: {cpf_teste}")
        print("Validando com função validar_cpf():")
        validar_cpf(cpf_teste)
    except ImportError:
        print("\nPara testar a integração, execute ambos os arquivos (gerador + validador)")
  