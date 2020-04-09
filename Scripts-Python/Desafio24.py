cidade = input('Digite o nome da cidade que você nasceu: ').strip()
cidade = cidade.split()
cidade[0] = cidade[0].upper()
print('SANTOS' in cidade[0])