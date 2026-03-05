# Script para anlizr abanono de cientes
# Todo por desarrolar

df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto'])