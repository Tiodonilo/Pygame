import random

class Pessoa:
    def __init__(self, nome = 'Inimigo'):
        self.nome = nome
        self.vida = 100
        self.ataque = 1
        self.defesa = 0
        self.nivel = 0
        self.gloria = 0
        self.total = {'vida': self.vida, 'ataque': self.ataque, 'defesa': self.defesa}

    def __sub__(self, inimigo):
        if inimigo.ataque == self.defesa: print('Ataque defendido totalmente')
        elif inimigo.ataque < self.defesa:
            inimigo - self
            print('Contra-ataque!')
        else:
            self.vida -= inimigo.ataque - self.defesa
            print(self.nome, 'recebeu',inimigo.ataque-self.defesa, 'de dano!')
        if 0 < self.vida < 10:
            print(self.nome, 'está muito ferido!')
            self.ataque = 1
            self.defesa = 0
        elif self.vida < 0:
            print(self.nome, 'morreu.')
            self.__del__()

    def __add__(self, pocao):
        try:
            pocao = pocao.eat()
            if pocao > 5: self.vida += pocao
            elif pocao == 5: self.ataque += pocao
            else: self.defesa += pocao
            if self.vida > self.total['vida']: self.vida = self.total['vida']
        except:
            self.gloria += pocao.tipo
        finally:
            print(self)

    def __str__(self):
        for i,o in self.__dict__.items():
            print(i+':',o)
        print()
        return str(self.__dict__)
    
    def __del__(self):
        print(self.nome,"morreu ao nível:",self.nivel)

    def up(self):
        self.gloria -= 100
        if self.gloria > 99: self.descansa()
        self.total['vida'] += 10
        self.vida = self.total['vida']
        self.total['ataque'] += 1
        self.ataque = self.total['ataque']
        self.total['defesa'] += 1
        self.defesa = self.total['defesa']
        self.nivel += 1
    
    def heal(self, quant):
        self.vida += quant
        if self.vida > self.total['vida']: self.vida = self.total['vida']

    def descansa(self):
        if self.gloria > 99: self.up()
        else:
            self.heal(10)
        
    def __call__(self):
        print("Ola")

class Supply:
    def __init__(self):
        self.tipo = random.randint(1,5)
    def eat(self):
        if self.tipo == 1:
            print("Poção Simples!")
            return 10
        elif self.tipo == 2:
            print("Poção Normal!")
            return 50
        elif self.tipo == 3:
            print("Poção Grande!")
            return 100
        elif self.tipo == 4:
            print("Mais força!")
            return 5
        else:
            print("Mais defesa!")
            return 3

class Xp:
    def __init__(self): 
        self.lista = [10, 50, 100]
        random.shuffle(self.lista)
        self.tipo = self.lista[0]