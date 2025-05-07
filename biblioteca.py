class Pessoa():
    def __init__(self, user, eight, age):
        self.nome = user
        self.peso = eight
        self.idade = age
        self.dormindo = False
        self.comendo = False
        self.falando = False

    def falar(self, falando):
        if falando == True:
            print(f'{self.nome} está falando!')
        elif falando == falando:
            print(f'{self.nome} ele já está falando...')
        else:
            print(f'{self.nome} está calado!')

    def comer(self, comendo):
        if comendo == True:
            print(f'{self.nome} está comendo!')
        elif comendo == True:
            print(f'{self.nome} tá comendo de novo é?')
        else:
            print(f'{self.nome} não está comendo!')

    def dormir(self, dormindo):
        if dormindo == True:
            print(f'{self.nome} está dormindo! Zzzz')
        elif dormindo == True:
                print(f'{self.nome} já está dormindo!')
        else:
            print(f'{self.nome} está acordado!')