# arquivo para a criação de players
import random
from Classes import CLASSES, PROFISOES 

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
        
        # Atributos fixos/especiais
        self.sorte = 0

        # 1. Bônus de PROFISSÃO
        if self.profissao in PROFISOES:
            BonusP = PROFISOES[self.profissao]
            self.forca += BonusP.get("forca", 0)
            self.agilidade += BonusP.get("agilidade", 0)
            self.vitalidade += BonusP.get("vitalidade", 0)
            self.inteligencia += BonusP.get("inteligencia", 0)
            self.destreza += BonusP.get("destreza", 0)
            self.carisma += BonusP.get("carisma", 0)
            self.sorte += BonusP.get("sorte", 0)

        # 2. Bônus de CLASSE
        if self.classe in CLASSES:
            BonusC = CLASSES[self.classe]
            self.forca += BonusC.get("forca", 0)
            self.agilidade += BonusC.get("agilidade", 0)
            self.vitalidade += BonusC.get("vitalidade", 0)
            self.inteligencia += BonusC.get("inteligencia", 0)
            self.destreza += BonusC.get("destreza", 0)
            self.carisma += BonusC.get("carisma", 0)
            self.sorte += BonusC.get("sorte", 0)

        self.fadiga = 0
        self.inventario = []
        
        # --- SISTEMA DE EQUIPAMENTO ---
        self.equipamento = {
            "mao_principal": None,
            "cabeca": None,
            "corpo": None,
            "pernas": None
        }

        self.vidas = 3
        self.morto_permanentemente = False
        
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

    # --- MÉTODOS DE STATUS ---
    def calcular_hp_max(self):
        bonus_prodigio = 20 if self.is_prodigio else 0
        self.hp_max = (self.vitalidade * 10) + bonus_prodigio

    def level_up(self):
        self.nivel += 1
        self.pontos_disp += 3
        self.xp -= self.xp_needed
        self.xp_needed = int(self.xp_needed * 1.5)
        self.calcular_hp_max()
        self.hp_atual = self.hp_max
        print(f"✨ NÍVEL UP! Nível {self.nivel}. Você tem {self.pontos_disp} pontos!")

    # --- MÉTODOS DE SOBREVIVÊNCIA ---
    def ganhar_fadiga(self, custo_base):
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
        self.fadiga = 0 
        print(f"🚨 FADIGA CRÍTICA! {self.nome} desmaiou e perdeu {dano:.1f} de HP.")

    def caminhar(self, distancia):
        custo_base = distancia * 5
        peso_mochila = sum(item.peso for item in self.inventario) if self.inventario else 0
        if peso_mochila > (self.forca * 2):
            custo_base *= 2
        self.ganhar_fadiga(custo_base)

    def morrer(self):
        self.vidas -= 1
        if self.vidas > 0:
            print(f"💀 Morte evitada! Vidas restantes: {self.vidas}")
            self.hp_atual = self.hp_max 
            self.fadiga = 0
        else:
            self.morto_permanentemente = True
            print(f"🚫 GAME OVER PERMANENTE para {self.nome}.")

    # --- SISTEMA DE ITENS E EQUIPAMENTOS ---
    
    def descobrir_slot(self, item):
        nome_low = item.nome.lower()
        
        if item.tipo == "Arma":
            return "mao_principal"
            
        elif item.tipo == "Armadura":
            # Listas de palavras-chave baseadas no seu banco de dados
            termos_cabeca = ["elmo", "capacete", "capuz", "mascara", "máscara", "bandana"]
            termos_pernas = ["bota", "perneira", "sapato", "greva"]
            termos_corpo = ["túnica", "tunica", "colete", "manto", "peitoral", "traje", "armadura", "capa"]
            
            if any(t in nome_low for t in termos_cabeca): return "cabeca"
            if any(t in nome_low for t in termos_pernas): return "pernas"
            return "corpo" # Padrão para armaduras
        return None

    def adicionar_item(self, item):
        limite = self.vitalidade * 2
        peso_atual = sum(i.peso for i in self.inventario)
        if peso_atual + item.peso <= limite:
            self.inventario.append(item)
            return True
        print(f"📦 {item.nome} é pesado demais!")
        return False

    def equipar_item(self, item):
        if item not in self.inventario:
            print("❌ Você não tem esse item!")
            return

        slot = self.descobrir_slot(item)
        if not slot:
            print("🚫 Esse item não pode ser equipado.")
            return

        # Desequipar o atual se existir para não acumular bônus infinitos
        if self.equipamento[slot]:
            antigo = self.equipamento[slot]
            self.forca -= antigo.bonus_ataque
            self.vitalidade -= antigo.bonus_defesa

        # Equipar novo
        self.equipamento[slot] = item
        self.forca += item.bonus_ataque
        self.vitalidade += item.bonus_defesa
        
        self.calcular_hp_max() # Atualiza o HP se a Vitalidade mudou
        print(f"✅ {item.nome} equipado em {slot}!")