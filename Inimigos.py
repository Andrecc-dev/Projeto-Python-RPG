import random
import copy

# Geração dos inimigos 

# Definição da classe inimigos
class inimigo:
    def __init__(self, nome, nivel, hp, dano, xp_adquirido, gold_adquirido, categoria="Normal"):
        self.nome = nome
        self.nivel = nivel
        self.hp_max = hp
        self.hp_atual = hp
        self.dano_base = dano
        self.xp_adquirido = xp_adquirido
        self.gold_adquirido = gold_adquirido
        self.categoria = categoria

    def __repr__(self):
        return f"{self.nome} (nivel {self.nivel}) - {self.categoria}"

# --- CATEGORIA: TREINO ---
INIMIGOS_TREINO = {
    "boneco_madeira": inimigo("Boneco de Treino", 1, 100, 0, 5, 0, categoria="Treino"),
    "espantalho_velho": inimigo("Espantalho de Palha", 1, 50, 1, 10, 0, categoria="Treino")
}

# --- CATEGORIA: NORMAIS ---
INIMIGOS_NORMAIS = {
    "slime_gelatinoso": inimigo("Slime Azul", 1, 30, 3, 20, 5),
    "goblin_saqueador": inimigo("Goblin Saqueador", 3, 60, 8, 45, 15),
    "lobo_faminto": inimigo("Lobo Faminto", 5, 100, 12, 70, 2)
}

# --- CATEGORIA: BOSS ---
BOSS_DUNGEON = {
    "rei_goblin": inimigo("Rei Goblin", 10, 500, 25, 500, 200, categoria="Boss"),
    "dragao_filhote": inimigo("Filhote de Dragão", 15, 1200, 45, 1500, 1000, categoria="Boss")
}

# =================================================================
# O GERADOR DE ENCONTROS (A FÁBRICA DE CLONES)
# =================================================================
def gerar_inimigo(categoria="Normal", nome_especifico=None):
    """
    Seleciona um inimigo da base de dados e retorna uma cópia independente para a luta.
    """
    # 1. Seleciona a tabela correta
    if categoria == "Treino":
        tabela = INIMIGOS_TREINO
    elif categoria == "Boss":
        tabela = BOSS_DUNGEON
    else:
        tabela = INIMIGOS_NORMAIS

    # 2. Escolhe o inimigo (por nome ou aleatório)
    if nome_especifico and nome_especifico in tabela:
        modelo = tabela[nome_especifico]
    else:
        # Sorteia um dos monstros disponíveis na categoria
        modelo = random.choice(list(tabela.values()))

    # 3. Retorna uma CÓPIA profunda para que o original não seja alterado na luta
    return copy.deepcopy(modelo)