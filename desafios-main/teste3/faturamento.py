import json

# Exemplo de dados de faturamento em formato JSON
faturamento_json = '''{
    "dias": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 26742.6612},
        {"dia": 7, "valor": 0.0}
    ]
}'''

faturamento = json.loads(faturamento_json)
valores = [dia['valor'] for dia in faturamento['dias'] if dia['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = len([v for v in valores if v > media_mensal])

print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
