from Itens import Equipamento

# --- ITENS ARQUEIRO: COMUM (Rank E) ---
ITENS_ARQUEIRO_COMUM = {
    # ARMAS (Arcos/Bestas)
    "arco_curto_madeira": Equipamento("Arco Curto de Madeira", "Arma", 15, bonus_ataque=4, peso=1.2, raridade="Comum"),
    "besta_mao_velha": Equipamento("Besta de Mão Velha", "Arma", 25, bonus_ataque=6, peso=2.0, raridade="Comum"),
    "arco_longo_caça": Equipamento("Arco Longo de Caça Gasto", "Arma", 20, bonus_ataque=5, peso=1.8, raridade="Comum"),

    # ARMADURAS (Couro Leve/Tecido)
    "colete_tecido_reforçado": Equipamento("Colete de Tecido Reforçado", "Armadura", 30, bonus_defesa=3, peso=1.0, raridade="Comum"),
    "luvas_arqueiro_gastas": Equipamento("Luvas de Arqueiro Gastas", "Armadura", 15, bonus_defesa=1, peso=0.2, raridade="Comum"),
    "botas_silenciosas_couro": Equipamento("Botas de Couro Simples", "Armadura", 20, bonus_defesa=2, peso=0.5, raridade="Comum"),
}

# --- ITENS ARQUEIRO: INCOMUM (Rank D) ---
ITENS_ARQUEIRO_INCOMUM = {
    "arco_composto_reforçado": Equipamento("Arco Composto Reforçado", "Arma", 160, bonus_ataque=16, peso=1.5, raridade="Incomum"),
    "besta_pesada_ferro": Equipamento("Besta Pesada de Ferro", "Arma", 190, bonus_ataque=20, peso=3.5, raridade="Incomum"),
    "arco_longo_teixo": Equipamento("Arco Longo de Teixo Polido", "Arma", 175, bonus_ataque=18, peso=1.6, raridade="Incomum"),

    "gibao_couro_batido": Equipamento("Gibão de Couro Batido", "Armadura", 200, bonus_defesa=10, peso=2.5, raridade="Incomum"),
    "braçadeiras_proteçao": Equipamento("Braçadeiras de Proteção", "Armadura", 120, bonus_defesa=5, peso=0.4, raridade="Incomum"),
    "aljava_reforçada": Equipamento("Aljava de Couro Reforçada", "Armadura", 100, bonus_defesa=3, peso=0.8, raridade="Incomum"),
}

# --- ITENS ARQUEIRO: RARO (Rank C) ---
ITENS_ARQUEIRO_RARO = {
    "arco_ventos_cortantes": Equipamento("Arco dos Ventos Cortantes", "Arma", 600, bonus_ataque=45, peso=1.3, raridade="Raro"),
    "arco_longo_carvalho_real": Equipamento("Arco Longo de Carvalho Real", "Arma", 580, bonus_ataque=42, peso=1.7, raridade="Raro"),
    "besta_repetição_mecanica": Equipamento("Besta de Repetição Mecânica", "Arma", 700, bonus_ataque=48, peso=4.0, raridade="Raro"),

    "armadura_couro_serpente": Equipamento("Couraça de Couro de Serpente", "Armadura", 850, bonus_defesa=25, peso=3.0, raridade="Raro"),
    "capuz_camuflagem_floresta": Equipamento("Capuz de Camuflagem", "Armadura", 400, bonus_defesa=12, peso=0.3, raridade="Raro"),
    "botas_passo_rapido": Equipamento("Botas do Passo Rápido", "Armadura", 380, bonus_defesa=14, peso=0.6, raridade="Raro"),
}

# --- ITENS ARQUEIRO: ÉPICO (Rank B) ---
ITENS_ARQUEIRO_EPICO = {
    "arco_gloria_elfica": Equipamento("Arco da Glória Élfica", "Arma", 3200, bonus_ataque=95, peso=1.2, raridade="Epico"),
    "besta_disparo_multiplo": Equipamento("Besta de Cerco do Vazio", "Arma", 3500, bonus_ataque=105, peso=5.0, raridade="Epico"),
    "arco_flecha_relampago": Equipamento("Arco Trovão Estriado", "Arma", 3100, bonus_ataque=92, peso=1.4, raridade="Epico"),

    "manto_sentinela_noite": Equipamento("Manto da Sentinela da Noite", "Armadura", 4000, bonus_defesa=60, peso=2.0, raridade="Epico"),
    "mascara_caçador_feras": Equipamento("Máscara do Caçador de Feras", "Armadura", 2200, bonus_defesa=35, peso=0.5, raridade="Epico"),
    "luvas_precisao_mestre": Equipamento("Luvas de Precisão do Mestre", "Armadura", 1900, bonus_defesa=28, peso=0.3, raridade="Epico"),
}

# --- ITENS ARQUEIRO: LENDÁRIO (Rank A) ---
ITENS_ARQUEIRO_LENDARIO = {
    "arco_artemis_sagrado": Equipamento("Arco Sagrado de Ártemis", "Arma", 18000, bonus_ataque=190, peso=1.5, raridade="Lendario"),
    "besta_destruidora_dragoes": Equipamento("Besta Matadora de Dragões", "Arma", 21000, bonus_ataque=210, peso=6.0, raridade="Lendario"),
    "arco_suspiro_celestial": Equipamento("Arco Suspiro Celestial", "Arma", 17500, bonus_ataque=185, peso=1.4, raridade="Lendario"),

    "traje_falcao_dourado": Equipamento("Traje do Falcão Dourado", "Armadura", 26000, bonus_defesa=120, peso=3.5, raridade="Lendario"),
    "elmo_visao_infinita": Equipamento("Elmo da Visão Infinita", "Armadura", 14000, bonus_defesa=65, peso=1.0, raridade="Lendario"),
    "aljava_mecanica_ancian": Equipamento("Aljava Mecânica Ancestral", "Armadura", 12000, bonus_defesa=55, peso=1.5, raridade="Lendario"),
}

# --- ITENS ARQUEIRO: MÍTICO (Rank S) ---
ITENS_ARQUEIRO_MITICO = {
    "arco_estrela_poente": Equipamento("Arco da Estrela Poente", "Arma", 130000, bonus_ataque=480, peso=1.0, raridade="Mitico"),
    "disparador_de_mundos": Equipamento("Besta do Juízo Final", "Arma", 155000, bonus_ataque=530, peso=4.5, raridade="Mitico"),
    "arco_zero_absoluto": Equipamento("O Arco do Zero Absoluto", "Arma", 120000, bonus_ataque=460, peso=1.2, raridade="Mitico"),

    "manto_onipresença_ventos": Equipamento("Manto da Onipresença dos Ventos", "Armadura", 210000, bonus_defesa=240, peso=0.5, raridade="Mitico"),
    "armadura_espectral_luz": Equipamento("Armadura Espectral da Luz", "Armadura", 190000, bonus_defesa=230, peso=2.0, raridade="Mitico"),
    "olho_do_observador_etereo": Equipamento("Olho do Observador Etéreo", "Armadura", 110000, bonus_defesa=140, peso=0.2, raridade="Mitico"),
}