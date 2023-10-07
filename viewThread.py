import json

with open('data.txt', 'r') as file:
    data = file.read()

blocks = data.split('}{')  # разбиваем данные на блоки

for block in blocks:
    if block[0] != '{':  # если блок начинается не с '{', то добавляем его
        block = '{' + block
    if block[-1] != '}':  # если блок заканчивается не '}', то добавляем его
        block += '}'

    block_data = json.loads(block)  # преобразуем блок в словарь

    print('Block index:', block_data['index'])
    print('Timestamp:', block_data['timestamp'])
    print('Transactions:')
    for tx in block_data['transaction']:
        print('  ', tx['sender'], '->', tx['receiver'], '(', tx['amount'], ')')
    print('Previous hash:', block_data['previous_hash'])
    print('Hash:', block_data['hash'])
    print('Nonce:', block_data['nonce'])
    print()