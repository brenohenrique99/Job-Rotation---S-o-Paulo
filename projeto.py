import json

with open('dados.json', 'r') as arquivo:
    conteudo = arquivo.read()

dados = json.loads(conteudo)
print(dados)