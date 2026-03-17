# arquivo para a criação de players
import random

class player:
    def __init__(self, nome, classe_escolhida, local_nasc, profissao):
        self.nome = nome
        self.classe = classe_escolhida
        self.local_nasc = local_nasc
        self.profissao = profissao

        # Atributos bases
        self.nivel = 1
        self.xp = 0
        self.xp_needed = 100
        self.gold = 50
        self.karma = 0
        self.alinhamento = "neutro"
        self.pontos_disp = 0

        # Status base do herói
        self.forca = 5
        self.agilidade = 5
        self.vitalidade = 5
        self.inteligencia = 5
        self.destreza = 5
        self.carisma = 5
        self.fadiga = 0
        self.inventario = [] # Inicializa o inventário vazio
        
        self.sorte_secreta = random.randint(1, 100)
        self.is_prodigio = True if random.randint(1, 100) <= 5 else False
        
        # Sistema de Nen
        self.possui_nen = False
        self.categoria_nen = None
        self.nen_pontos = 0
        self.nivel_despertar_nen = random.randint(8, 45)
        
        # Bônus de Prodígio
        if self.is_prodigio:
            self.forca += 2
            self.agilidade += 2
            self.vitalidade += 2
            self.inteligencia += 2
            self.destreza += 2
            self.carisma += 2
            self.nivel_despertar_nen = random.randint(5, 15)

        # Inicialização de Vida
        self.hp_max = 0
        self.calcular_hp_max()
        self.hp_atual = self.hp_max

    def calcular_hp_max(self):
        # Fórmula: Vitalidade * 10 (+ bônus de prodígio)
        bonus_prodigio = 20 if self.is_prodigio else 0
        self.hp_max = (self.vitalidade * 10) + bonus_prodigio

    def level_up(self):
        self.nivel += 1
        self.pontos_disp += 3
        self.xp -= self.xp_needed
        self.xp_needed = int(self.xp_needed * 1.5)

        # Atualiza o HP máximo conforme a nova Vitalidade
        self.calcular_hp_max()
        
        # Recupera um pouco de vida ao subir de nível (opcional, mude se preferir recuperar tudo)
        self.hp_atual = self.hp_max
        
        print(f"✨ NÍVEL UP! Você agora está no nível {self.nivel}.")
        print(f"🎯 Você tem {self.pontos_disp} pontos para distribuir!")

    def ganhar_fadiga(self, custo_base):
        # Redutor baseado na Vitalidade
        redutor = self.vitalidade / 10
        if redutor < 1: redutor = 1 
        
        impacto_real = custo_base / redutor
        self.fadiga += impacto_real

        if self.fadiga >= 100:
            self.fadiga = 100
            self.aplicar_penalidade_desmaio()

    def aplicar_penalidade_desmaio(self):
        dano = self.hp_atual * 0.25
        self.hp_atual -= dano
        self.fadiga = 0 # O jogador descansa após desmaiar
        print(f"🚨 FADIGA CRÍTICA! {self.nome} desmaiou de exaustão e perdeu {dano:.1f} de HP.")

    def caminhar(self, distancia):
        custo_base = distancia * 5
        
        # Calcula o peso total dos itens no inventário
        # (Supõe que cada item tenha um atributo .peso)
        peso_mochila = sum(item.peso for item in self.inventario) if self.inventario else 0
    
        # Penalidade por sobrecarga
        if peso_mochila > (self.forca * 2):
            print("⚠️ Você está sobrecarregado! O cansaço será maior.")
            custo_base *= 2
        
        self.ganhar_fadiga(custo_base)