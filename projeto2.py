import json

with open('dados.json') as f:
    dados = json.load(f)

# Obtendo uma lista de valores de faturamento diário diferentes de zero
valores = [d['valor'] for d in dados if d['valor'] != 0]

# Menor valor de faturamento diário
menor_valor = min(valores)

# Maior valor de faturamento diário
maior_valor = max(valores)

# Média de faturamento diário
media = sum(valores) / len(valores)

# Número de dias com faturamento diário superior à média
dias_acima_media = len([d for d in dados if d['valor'] > media])

print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias com faturamento diário superior à média: {dias_acima_media}")
