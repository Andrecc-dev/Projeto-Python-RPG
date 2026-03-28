from Itens import Equipamento

# --- ITENS CLÉRIGO: COMUM (Rank E) ---
ITENS_CLERIGO_COMUM = {
    "maça_ferro_velha": Equipamento("Maça de Ferro Velha", "Arma", 15, bonus_ataque=3, peso=2.5, raridade="Comum", classe_exclusiva="Clérigo"),
    "cajado_peregrino": Equipamento("Cajado de Peregrino", "Arma", 12, bonus_ataque=2, peso=1.5, raridade="Comum", classe_exclusiva="Clérigo"),
    "simbolo_madeira": Equipamento("Símbolo Sagrado de Madeira", "Arma", 20, bonus_ataque=4, peso=0.5, raridade="Comum", classe_exclusiva="Clérigo"),

    "tunica_fiel": Equipamento("Túnica do Fiel", "Armadura", 30, bonus_defesa=3, peso=1.5, raridade="Comum", classe_exclusiva="Clérigo"),
    "capuz_linho": Equipamento("Capuz de Linho Bento", "Armadura", 15, bonus_defesa=1, peso=0.3, raridade="Comum", classe_exclusiva="Clérigo"),
    "sandalias_santo": Equipamento("Sandálias do Penitente", "Armadura", 10, bonus_defesa=2, peso=0.4, raridade="Comum", classe_exclusiva="Clérigo"),
}

# --- ITENS CLÉRIGO: INCOMUM (Rank D) ---
ITENS_CLERIGO_INCOMUM = {
    "maça_aço_batizado": Equipamento("Maça de Aço Batizado", "Arma", 160, bonus_ataque=12, peso=3.0, raridade="Incomum", classe_exclusiva="Clérigo"),
    "cajado_carvalho_abencoado": Equipamento("Cajado de Carvalho Abençoado", "Arma", 150, bonus_ataque=10, peso=1.8, raridade="Incomum", classe_exclusiva="Clérigo"),
    "mangual_penitencia": Equipamento("Mangual da Penitência", "Arma", 180, bonus_ataque=14, peso=3.5, raridade="Incomum", classe_exclusiva="Clérigo"),

    "cota_malha_leve": Equipamento("Cota de Malha Leve", "Armadura", 220, bonus_defesa=12, peso=8.0, raridade="Incomum", classe_exclusiva="Clérigo"),
    "ombreiras_ferro_sacro": Equipamento("Ombreiras de Ferro Sacro", "Armadura", 130, bonus_defesa=6, peso=3.0, raridade="Incomum", classe_exclusiva="Clérigo"),
    "livro_oraçoes_reforçado": Equipamento("Livro de Orações Reforçado", "Armadura", 100, bonus_defesa=4, peso=1.0, raridade="Incomum", classe_exclusiva="Clérigo"),
}

# --- ITENS CLÉRIGO: RARO (Rank C) ---
ITENS_CLERIGO_RARO = {
    "martelo_purificador": Equipamento("Martelo Purificador", "Arma", 650, bonus_ataque=35, peso=4.5, raridade="Raro", classe_exclusiva="Clérigo"),
    "cetro_luz_crepuscular": Equipamento("Cetro da Luz Crepuscular", "Arma", 700, bonus_ataque=40, peso=2.0, raridade="Raro", classe_exclusiva="Clérigo"),
    "maça_sol_eterno": Equipamento("Maça do Sol Eterno", "Arma", 600, bonus_ataque=38, peso=3.2, raridade="Raro", classe_exclusiva="Clérigo"),

    "manto_bispo_guerra": Equipamento("Manto do Bispo de Guerra", "Armadura", 1100, bonus_defesa=28, peso=4.0, raridade="Raro", classe_exclusiva="Clérigo"),
    "escudo_reliquia": Equipamento("Escudo de Relíquia Antiga", "Armadura", 800, bonus_defesa=20, peso=7.0, raridade="Raro", classe_exclusiva="Clérigo"),
    "mitra_foco_divino": Equipamento("Mitra de Foco Divino", "Armadura", 500, bonus_defesa=12, peso=0.8, raridade="Raro", classe_exclusiva="Clérigo"),
}

# --- ITENS CLÉRIGO: ÉPICO (Rank B) ---
ITENS_CLERIGO_EPICO = {
    "maça_quebra_demonios": Equipamento("Maça Quebra-Demônios", "Arma", 3500, bonus_ataque=85, peso=4.0, raridade="Epico", classe_exclusiva="Clérigo"),
    "cajado_vida_plena": Equipamento("Cajado da Vida Plena", "Arma", 4000, bonus_ataque=90, peso=2.5, raridade="Epico", classe_exclusiva="Clérigo"),
    "mangual_chamas_sagradas": Equipamento("Mangual das Chamas Sagradas", "Arma", 3800, bonus_ataque=95, peso=5.0, raridade="Epico", classe_exclusiva="Clérigo"),

    "armadura_santo_guerreiro": Equipamento("Placas do Santo Guerreiro", "Armadura", 5500, bonus_defesa=65, peso=14.0, raridade="Epico", classe_exclusiva="Clérigo"),
    "capa_serafim": Equipamento("Capa de Tecido de Serafim", "Armadura", 3200, bonus_defesa=40, peso=1.0, raridade="Epico", classe_exclusiva="Clérigo"),
    "luvas_toque_curativo": Equipamento("Luvas do Toque Curativo", "Armadura", 2200, bonus_defesa=25, peso=0.4, raridade="Epico", classe_exclusiva="Clérigo"),
}

# --- ITENS CLÉRIGO: LENDÁRIO (Rank A) ---
ITENS_CLERIGO_LENDARIO = {
    "maça_radiante_uriel": Equipamento("Maça Radiante de Uriel", "Arma", 20000, bonus_ataque=180, peso=3.5, raridade="Lendario", classe_exclusiva="Clérigo"),
    "cajado_eden_florido": Equipamento("Cajado do Éden Florido", "Arma", 18000, bonus_ataque=170, peso=2.0, raridade="Lendario", classe_exclusiva="Clérigo"),
    "relicario_almas_puras": Equipamento("Relicário das Almas Puras", "Arma", 25000, bonus_ataque=200, peso=1.5, raridade="Lendario", classe_exclusiva="Clérigo"),

    "veste_papa_imortal": Equipamento("Veste do Papa Imortal", "Armadura", 30000, bonus_defesa=120, peso=3.0, raridade="Lendario", classe_exclusiva="Clérigo"),
    "escudo_egide_celestial": Equipamento("Égide Celestial", "Armadura", 20000, bonus_defesa=100, peso=10.0, raridade="Lendario", classe_exclusiva="Clérigo"),
    "coroa_martires": Equipamento("Coroa dos Mártires", "Armadura", 15000, bonus_defesa=60, peso=0.6, raridade="Lendario", classe_exclusiva="Clérigo"),
}

# --- ITENS CLÉRIGO: MÍTICO (Rank S) ---
ITENS_CLERIGO_MITICO = {
    "esperança_humanidade": Equipamento("Esperança da Humanidade", "Arma", 150000, bonus_ataque=480, peso=3.0, raridade="Mitico", classe_exclusiva="Clérigo"),
    "cajado_arvore_vida": Equipamento("Cajado da Árvore da Vida", "Arma", 180000, bonus_ataque=520, peso=2.0, raridade="Mitico", classe_exclusiva="Clérigo"),
    "veredito_divino": Equipamento("O Veredito Divino", "Arma", 140000, bonus_ataque=450, peso=4.0, raridade="Mitico", classe_exclusiva="Clérigo"),

    "manto_criador": Equipamento("Manto Tecido pelo Criador", "Armadura", 250000, bonus_defesa=260, peso=0.5, raridade="Mitico", classe_exclusiva="Clérigo"),
    "aura_imortalidade": Equipamento("Aura da Imortalidade Absoluta", "Armadura", 200000, bonus_defesa=230, peso=0.0, raridade="Mitico", classe_exclusiva="Clérigo"),
    "halo_divino": Equipamento("Halo do Divino Eterno", "Armadura", 120000, bonus_defesa=130, peso=0.1, raridade="Mitico", classe_exclusiva="Clérigo"),
}