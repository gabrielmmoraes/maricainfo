import requests
import json

# Código que pega a Atividade da empresa de acordo com seu CNPJ.

def pegaAtividade(cnpj):
    cnpj = str(cnpj)
    url = "http://receitaws.com.br/v1/cnpj/" + cnpj
    r = requests.get(url)
    json = r.json()
    atividade = json['atividade_principal'][0]['text']
    atividade = atividade.encode('ascii','ignore')
    return atividade