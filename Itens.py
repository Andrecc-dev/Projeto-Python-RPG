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
    def __init__(self, nome, tipo, valor, bonus_ataque=0, bonus_defesa=0, peso=2):
        super().__init__(nome, tipo, valor, peso)
        self.bonus_ataque = bonus_ataque
        self.bonus_defesa = bonus_defesa

# --- BANCO DE DADOS DE ITENS INICIAIS ---
ITENS_BASICOS = {
    "pocao_pequena": Consumivel("Poção de Vida P", 10, cura_hp=20),
    "maca": Consumivel("Maçã", 2, cura_hp=5, reduz_fadiga=10),
    "espada_ferro": Equipamento("Espada de Ferro", "Arma", 50, bonus_ataque=5),
    "escudo_madeira": Equipamento("Escudo de Madeira", "Armadura", 30, bonus_defesa=3)
}