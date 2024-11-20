#Objetivos:
    #1)Criar filtros de cada região
    #Segundo teste de git

#Packs
import pandas as pd



#Import
data_df = pd.read_excel("Tabela 1.xlsx")    #Tabela versão 1

#Const
preco_df = data_df['Preço']
devolucao = data_df['Devoluções']

data_df['Perdas'] = (preco_df * devolucao) * (-1)

#VAR



#functions
def dados_RJ():
    data_rj = data_df.loc[data_df['Local'] == 'Unidade RJ']

    print(data_rj)

def dados_SP():
    data_sp = data_df.loc[data_df['Local'] == 'Unidade SP']
    
    print(data_sp)

def dados_MG():
    data_mg = data_df.loc[data_df['Local'] == 'Unidade MG']
    
    print(data_mg)


#Main
print(data_df)
visual = str(input('Qual tabela deseja ver?(RIO DE JANEIRO/SÃO PAULO/MINAS GERAIS/TODAS): '))
if visual.lower() in ['rj','rio de janeiro','rio']:
    dados_RJ()
elif visual.lower() in ['sp','são paulo','sao paulo']:
    dados_SP()
elif visual.lower() in ['mg','minas gerais','minas']:
    dados_MG()
elif visual.lower() in ['todas']:
    dados_RJ()
    dados_SP()
    dados_MG()
else:
    dados_RJ()
    dados_SP()
    dados_MG()