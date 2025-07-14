import requests
from pprint import pprint

cnpj = "33592510000154"

url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

requisicao = requests.get(url)

pprint(requisicao.json())

atividade_princiapl = requisicao.json()["estabelecimento"]["atividade_principal"]["descricao"]
print(atividade_princiapl)