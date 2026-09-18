from datetime import datetime, date, timedelta
import holidays

#feriados_brasileiro = holidays.BR()
feriados_df = holidays.BR(subdiv="DF")

# Função do Gemini
# Ajusta a data para datetime independente se a entrada chega como string ou datetime
def normalizar_data(data, formato="%d/%m/%Y"):
    if isinstance(data, str):
        return datetime.strptime(data, formato).date()
    elif isinstance(data, datetime):
        return data.date()
    elif isinstance(data, date):
        return data
    else:
        raise TypeError("O formato precisa ser string, date ou datetime.")
    
# Verifica se o dia e util
# Dia util -> dia da semana sem ser feriado
def dia_util(dia):
    
    dia = normalizar_data(dia)
    
    if dia.weekday() > 4:
        return False
    
    if dia in feriados_df:
        return False
    
    return True

def soma_dias(data,dias):
    
    data = normalizar_data(data)
    return data + timedelta(days=dias)

# Função do Gemini
def soma_dias_uteis(data_inicial, dias_uteis):
    data_atual = normalizar_data(data_inicial)
    dias_adicionados = 0
    
    while dias_adicionados < dias_uteis:
        data_atual += timedelta(days=1)
        if dia_util(data_atual):
            dias_adicionados += 1
            
    return data_atual

# Testes
datas_teste = [
        '25/12/2025',
        '21/04/2025',
        '30/11/2026',
        '05/09/2026',
        '06/09/2026',
        '27/11/2025', 
        '23/10/2025', 
        '28/08/2024', 
        '24/10/2025', 
        '07/10/2025', 
        '19/11/2025', 
        '17/10/2025', 
        '26/11/2025', 
        '14/10/2025', 
        '15/09/2025', 
        '06/11/2025', 
        '28/11/2025', 
        '18/08/2025',
        '02/11/2025',
        '31/10/2025',
        '27/11/2025'
    ]

for data in datas_teste:

    print(data, dia_util(data))
    print(soma_dias(data, 7))
    print(soma_dias_uteis(data,7))
    
