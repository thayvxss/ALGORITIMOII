
def pontos_caracteres(senha):
    return len(senha) * 4

def pontos_maiusculas(senha):
    maiusculas = sum(1 for c in senha if c.isupper())
    return (len(senha) - maiusculas) * 2

def pontos_minusculas(senha):
    minusculas = sum(1 for c in senha if c.islower())
    return (len(senha) - minusculas) * 2

def pontos_numeros(senha):
    numeros = sum(1 for c in senha if c.isdigit())
    return numeros * 4

def pontos_simbolos(senha):
    simbolos = sum(1 for c in senha if not c.isalnum())
    return simbolos * 6

def pontos_meio(senha):
    meio_senha = senha[1:-1]  
    numeros_e_simbolos_meio = sum(1 for c in meio_senha if not c.isalnum())
    return numeros_e_simbolos_meio * 2

def verificar_letras_sequenciais(senha):
    sequencias = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
    senha_lower = senha.lower()
    pontos = 0
    for seq in sequencias:
        if seq in senha_lower:
            pontos += (len(seq) - 2) * 3  
    return pontos

def verificar_numeros_sequenciais(senha):
    sequencias = ['123', '234', '345', '456', '567', '678', '789']
    pontos = 0
    for seq in sequencias:
        if seq in senha:
            pontos += (len(seq) - 2) * 3  
    return pontos

def verificar_simbolos_sequenciais(senha):
    sequencias = ['!@#', '#$%', '&*(', '()*']
    pontos = 0
    for seq in sequencias:
        if seq in senha:
            pontos += (len(seq) - 2) * 3  
    return pontos

def deduzir_pontos(senha):
    pontos_deducoes = 0
        
    pontos_deducoes += verificar_letras_sequenciais(senha)
        
    pontos_deducoes += verificar_numeros_sequenciais(senha)
        
    pontos_deducoes += verificar_simbolos_sequenciais(senha)

    return pontos_deducoes

def regras_atingidas(senha):
    regras = 0
        
    maiusculas = sum(1 for c in senha if c.isupper())
    minusculas = sum(1 for c in senha if c.islower())
    
    if len(senha) >= 8:
        regras += 1
    if maiusculas >= len(senha) * 0.75 or minusculas >= len(senha) * 0.75 or \
       sum(1 for c in senha if c.isdigit()) >= len(senha) * 0.75 or \
       sum(1 for c in senha if not c.isalnum()) >= len(senha) * 0.75:
        regras += 1
    return regras * 2

def calcular_pontuacao(senha):
    pontos = 0
    pontos += pontos_caracteres(senha)
    pontos += pontos_maiusculas(senha)
    pontos += pontos_minusculas(senha)
    pontos += pontos_numeros(senha)
    pontos += pontos_simbolos(senha)
    pontos += pontos_meio(senha)
    pontos += regras_atingidas(senha)
    pontos -= deduzir_pontos(senha)
    return pontos

def avaliar_senha(senha):
    pontos = calcular_pontuacao(senha)
    
    if pontos < 20:
        return "Muito fraca"
    elif 20 <= pontos < 40:
        return "Fraca"
    elif 40 <= pontos < 60:
        return "Boa"
    elif 60 <= pontos < 80:
        return "Forte"
    else:
        return "Muito forte"

senha = input("Digite sua senha para avaliação: ")
avaliacao = avaliar_senha(senha)
print(f"A avaliação da sua senha é: {avaliacao}")
