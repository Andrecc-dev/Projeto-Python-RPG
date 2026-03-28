#aqui vai ser a parte responsavel pelos itens do jogo
class Item:
    def __init__(self, nome, tipo, valor, peso=1, raridade="Comum"):
        self.nome = nome
        self.tipo = tipo # "Consumivel", "Arma", "Armadura"
        self.valor = valor
        self.peso = peso
        self.raridade = raridade

    def __repr__(self):
        return f"{self.nome} ({self.raridade})"

class Consumivel(Item):
    def __init__(self, nome, valor, cura_hp=0, reduz_fadiga=0, peso=0.5):
        super().__init__(nome, "Consumivel", valor, peso)
        self.cura_hp = cura_hp
        self.reduz_fadiga = reduz_fadiga

class Equipamento(Item):
    # ADICIONADO: classe_exclusiva=None no final dos parênteses
    def __init__(self, nome, tipo, valor, bonus_ataque=0, bonus_defesa=0, peso=2, classe_exclusiva=None):
        super().__init__(nome, tipo, valor, peso)
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa
        # CORRIGIDO: recebe o valor que vem do argumento
        self.classe_exclusiva = classe_exclusiva 

# --- BANCO DE DADOS DE ITENS INICIAIS ---
ITENS_BASICOS = {
    "pocao_pequena": Consumivel("Poção de Vida P", 10, cura_hp=20),
    "maca": Consumivel("Maçã", 2, cura_hp=5, reduz_fadiga=10),
}

ARMAS_INICIAIS = {
    "Guerreiro": Equipamento("Espada de Treino", "Arma", 0, bonus_ataque=1, classe_exclusiva="Guerreiro"),
    "Arqueiro": Equipamento("Arco Básico", "Arma", 0, bonus_ataque=2, classe_exclusiva="Arqueiro"),
    "Assassino": Equipamento("Adaga Básica", "Arma", 0, bonus_ataque=1, classe_exclusiva="Assassino"),
    "Clerigo": Equipamento("Mangual de Treino", "Arma", 0, bonus_ataque=2, classe_exclusiva="Clerigo"),
    "Ladino": Equipamento("Faca de Serra", "Arma", 0, bonus_ataque=1, classe_exclusiva="Ladino"), 
    "Mago": Equipamento("Cajado Velho", "Arma", 0, bonus_ataque=3, classe_exclusiva="Mago"), 
    "Paladino": Equipamento("Martelo do Aspirante", "Arma", 0, bonus_ataque=3, classe_exclusiva="Paladino") 
}

ARMADURAS_INICIAIS = {
    "Guerreiro": Equipamento("Camisa de Linho", "Armadura", 0, bonus_defesa=1, classe_exclusiva="Guerreiro"),
    "Arqueiro": Equipamento("Traje de Pano de Saco", "Armadura", 0, bonus_defesa=1, classe_exclusiva="Arqueiro"),
    "Assassino": Equipamento("Capuz de Farrapos", "Armadura", 0, bonus_defesa=1, classe_exclusiva="Assassino"), 
    "Paladino": Equipamento("Peitoral de Couro Remendado", "Armadura", 0, bonus_defesa=2, classe_exclusiva="Paladino"),
    "Clerigo": Equipamento("Sandalias de Palha", "Armadura", 0, bonus_defesa=1, classe_exclusiva="Clerigo"), 
    "Ladino": Equipamento("Bandana Suja", "Armadura", 0, bonus_defesa=1, classe_exclusiva="Ladino"),
    "Mago": Equipamento("Chapeu Amassado", "Armadura", 0, bonus_defesa=1, classe_exclusiva="Mago")
}