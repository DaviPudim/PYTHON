blocks = int(input("Digite o número de blocos: "))

height = 0  # Altura inicial da pirâmide
total_blocks = 0  # Contador total de blocos utilizados

while total_blocks < blocks:
    height += 1  # Incrementa a altura da pirâmide
    layer_blocks = height**2  # Número de blocos na camada atual
    total_blocks += layer_blocks  # Atualiza o contador total de blocos

    if total_blocks > blocks:
        height -= 1  # Decrementa a altura se a última camada não for completa
        break

print("A altura da pirâmide:", height)

