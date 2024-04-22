def on_connect(client, userdate, flags, rc):
if rc == 0:
    print('Me conectei!!!')
else:
    print(f 'Erro ao me conectar codigo={rc}')
