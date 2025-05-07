class Pessoa():
    def __init__(self, user, eight, age):
        self.nome = user
        self.peso = eight
        self.idade = age

    def falar(self, fala):
        print(f'{self.nome} começou a falar {fala}')

    def comer(self):
        print(f'{self.nome} começou a comer!')

    def dormir(self):
        print(f'{self.nome} começou a dormir')