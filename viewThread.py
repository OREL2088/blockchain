import json
import os

def checkBlock(path):
    with open(path, 'r') as file:
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


while True:
    path = input('Enter path to chain: ')
    if os.path.isfile(path):
        try:
            checkBlock(path)
        except ValueError:
            print('Error! Invalid data in file.')
    else:
        print('Error! File not found at the specified path.')
    break