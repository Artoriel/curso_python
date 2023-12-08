def master(funcao):
    def slave(*args, **kwargs):
        print("Agora estou decoarada.")
        funcao(*args, **kwargs)
    return slave


@master
def fala_oi():
    print('oi')

@master
def outra_func(msg):
    print(msg)


outra_func('ola')
fala_oi()