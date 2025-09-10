import random
 
class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def atacar(self, alvo):
        print(f"\n{self.__nome} ataca o {alvo.get_nome()}!")

        if alvo.esquivar(self):
            print(f"{alvo.get_nome()} se esquiva do ataque de {self.get_nome()}")
            return

        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    def esquivar(self, atacante, modificador_chance=0):
        CHANCE_BASE = 25
        BONUS_POR_NIVEL = 5

        bonus_tipo = 0

        if hasattr(self, 'get_tipo') and self.get_tipo() == 'Voador':
            bonus_tipo = 20

        dif_nivel = self.get_nivel() - atacante.get_nivel()
        if dif_nivel <= 0:
            dif_nivel = 1
        chance_calculada = CHANCE_BASE + (dif_nivel * BONUS_POR_NIVEL) + modificador_chance + bonus_tipo
        chance_final = max(5, min(chance_calculada, 75))

        if random.randint(0, 100) <= chance_final:
            return True
        else:
            return False

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f"\nHabilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo):
        penalidade = -20
        if alvo.esquivar(self, modificador_chance = penalidade):
            print(f"O {alvo} conseguiu se esquivar do ataque de {self.get_nome()}")
            return
        
        dano = random.randint(self.get_nivel() * 4, self.get_nivel() * 20)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou o ataque especial e causou {dano} de dano!")


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return super().exibir_detalhes() + f"\nTipo: {self.get_tipo()}"

class Jogo:
    """
    Classe orquestradora do jogo
    """

    def __init__(self):
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=100, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        print("Iniciando a Batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print()
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = int(input("Escolha (1 - Atauqe Normal, 2 - Ataque Especial):)"))
            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print("\nParabéns! Você derrotou o inimigo!")
        else:
            print("\nInfelizmente, você foi derrotado pelo inimigo.")

jogo = Jogo()
jogo.iniciar_batalha()