def mayusculas(func):
    def envoltura(text):
        return func(text).upper()

    return envoltura

@mayusculas
def mensaje(name):
    return f'{name}, recibiste un mensaje'

def run():
    message = mayusculas(mensaje)

    print(message('axl'))

if __name__ == '__main__':
    run()