"""
Para esse projeto, o interesse está sobre a base de dados denominada IMP_COMPLETA.zip, que contém histórico mensal das importações detalhadas por produto (código NCM), Unidade Federativa importadora, ano, mês, país de origem, quilograma líquido, valor dólar FOB (US$) e outras.

A classificação de produto mais abrangente disponível é a SH2 (Sistema Harmonizado) e no nome dela se buscará identificar palavras como "fertilizantes" ou "adubo".
"""

import os
import time
import numpy as np

# Baixa zip

# Check if running in an IPython environment



try:
    get_ipython().run_line_magic('run', "/home/andre301267/git/Pricing-Fertilizer/codes/extração/Comexstat/IMP_NCM/Baixa_Extrai.py")
except NameError:
    # Alternative approach if not in IPython environment
    exec(open('/home/andre301267/git/Pricing-Fertilizer/codes/extração/Comexstat/IMP_NCM/Baixa_Extrai.py').read())

url = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_COMPLETA.zip'
local_filename = '/home/andre301267/git/pricing-Fertilizer/BD/Comexstat/temp/IMP_COMPLETA.zip'
baixa_zip(url,local_filename)


# Carrega tabelas complementares

get_ipython().run_line_magic('run', "'~/git/BD/Comexstat/function/Extrai-tab_complementares.ipynb'")

"""
Reconhecer os códigos mais abrangentes dos produtos de interesse no sistema internacional SH:
"""

# Identifica código foco

co_sh2_fert=ncm_sh[ncm_sh.NO_SH2_POR.str.lower().str.contains('fertilizante')]['CO_SH2'].unique()
co_sh2_fert

"""
Lista os códigos SH6 contidos no código SH2 de fertilizantes:
"""

ncm_sh_list=ncm_sh[ncm_sh.CO_SH2.isin(co_sh2_fert)]['CO_SH6'].unique()
ncm_sh_list

"""
Lê tabela com código comum ao Mercosul, que é o de maior especificação de produto.
"""

"""
Na última tabela de NCM, localizamos os códigos NCM que se relacionam aos SH6 de fertilizantes.
"""

list_ncm_fert=ncm[ncm.CO_SH6.isin(ncm_sh_list)].CO_NCM.unique()
list_ncm_fert

"""
Identificando os nomes dos arquivos no interior do IMP_COMPLETA.zip
"""

get_ipython().run_line_magic('run', "'/home/andre301267/git/BD/Comexstat/function/Id_internal_zipfile.ipynb'")

internal_zipfile=id_internal_zipfile(local_filename)

# Visualiza primeiras linhas do interno

get_ipython().run_line_magic('run', "'/home/andre301267/git/BD/Comexstat/function/vslz_primeiras_linhas.ipynb'")

vslz_primeiras_linhas(local_filename,internal_zipfile)

# Extrai filtrando

get_ipython().run_line_magic('run', "'/home/andre301267/git/BD/Comexstat/function/extrai_filtrando_ncm.ipynb'")

imp_fert=extrai_filtrando_ncm(local_filename,internal_zipfile)

# Corrige Columns Name

imp_fert=imp_fert.rename(columns={'SG_UF_NCM':'UF'})

# Salva arquivo extraído e filtrado

imp_fert.to_csv('~/git/BD/temp/imp_fert_ncm.csv', index=False)


# Verificar se o arquivo existe antes de tentar excluí-lo
if os.path.exists(local_filename):
    os.remove(local_filename)
    print(f'O arquivo {local_filename} foi excluído com sucesso.')
else:
    print(f'O arquivo {local_filename} não foi encontrado.')

imp_fert

f=time.time()
print(f"Tempo de execução: {round((f-i)/60,1)} minutos.")

