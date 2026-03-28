from Itens import Equipamento

# --- ITENS LADINO: COMUM (Rank E) ---
ITENS_LADINO_COMUM = {
    "faca_serrilhada_rua": Equipamento("Faca Serrilhada de Rua", "Arma", 15, bonus_ataque=3, peso=0.5, raridade="Comum", classe_exclusiva="Ladino"),
    "porrete_taberna": Equipamento("Porrete de Taberna", "Arma", 12, bonus_ataque=4, peso=1.2, raridade="Comum", classe_exclusiva="Ladino"),
    "navalha_barbeiro": Equipamento("Navalha de Barbeiro Gasta", "Arma", 10, bonus_ataque=2, peso=0.2, raridade="Comum", classe_exclusiva="Ladino"),

    "jaqueta_couro_velha": Equipamento("Jaqueta de Couro Gasta", "Armadura", 25, bonus_defesa=3, peso=2.0, raridade="Comum", classe_exclusiva="Ladino"),
    "bandana_salteador": Equipamento("Bandana de Salteador", "Armadura", 10, bonus_defesa=1, peso=0.1, raridade="Comum", classe_exclusiva="Ladino"),
    "luvas_dedos_cortados": Equipamento("Luvas de Tecido sem Dedos", "Armadura", 15, bonus_defesa=1, peso=0.2, raridade="Comum", classe_exclusiva="Ladino"),
}

# --- ITENS LADINO: INCOMUM (Rank D) ---
ITENS_LADINO_INCOMUM = {
    "espada_curta_guarda": Equipamento("Espada Curta da Guarda", "Arma", 150, bonus_ataque=13, peso=1.5, raridade="Incomum", classe_exclusiva="Ladino"),
    "adaga_folha_carvalho": Equipamento("Adaga Folha de Carvalho", "Arma", 140, bonus_ataque=11, peso=0.4, raridade="Incomum", classe_exclusiva="Ladino"),
    "besta_mao_ladrao": Equipamento("Besta de Mão do Ladrão", "Arma", 180, bonus_ataque=15, peso=1.8, raridade="Incomum", classe_exclusiva="Ladino"),

    "gibao_couro_tachas": Equipamento("Gibão de Couro com Tachas", "Armadura", 200, bonus_defesa=9, peso=3.0, raridade="Incomum", classe_exclusiva="Ladino"),
    "capuz_espreitador": Equipamento("Capuz do Espreitador", "Armadura", 120, bonus_defesa=5, peso=0.3, raridade="Incomum", classe_exclusiva="Ladino"),
    "botas_silencio_couro": Equipamento("Botas de Solado de Camurça", "Armadura", 130, bonus_defesa=6, peso=0.6, raridade="Incomum", classe_exclusiva="Ladino"),
}

# --- ITENS LADINO: RARO (Rank C) ---
ITENS_LADINO_RARO = {
    "estoque_fura_malha": Equipamento("Estoque Fura-Malha", "Arma", 600, bonus_ataque=38, peso=1.2, raridade="Raro", classe_exclusiva="Ladino"),
    "adaga_veneno_negro": Equipamento("Adaga de Veneno Negro", "Arma", 650, bonus_ataque=42, peso=0.5, raridade="Raro", classe_exclusiva="Ladino"),
    "punhal_perfurante": Equipamento("Punhal Perfurante de Aço", "Arma", 580, bonus_ataque=40, peso=0.4, raridade="Raro", classe_exclusiva="Ladino"),

    "manto_nevoa_noturna": Equipamento("Manto da Névoa Noturna", "Armadura", 900, bonus_defesa=24, peso=1.0, raridade="Raro", classe_exclusiva="Ladino"),
    "cinto_utilidades": Equipamento("Cinto de Utilidades do Gatuno", "Armadura", 450, bonus_defesa=10, peso=1.5, raridade="Raro", classe_exclusiva="Ladino"),
    "mascara_sombria": Equipamento("Máscara de Tecido Sombrio", "Armadura", 400, bonus_defesa=12, peso=0.2, raridade="Raro", classe_exclusiva="Ladino"),
}

# --- ITENS LADINO: ÉPICO (Rank B) ---
ITENS_LADINO_EPICO = {
    "faca_estilhaço": Equipamento("Faca de Estilhaço Estelar", "Arma", 3200, bonus_ataque=88, peso=0.3, raridade="Epico", classe_exclusiva="Ladino"),
    "lamina_catarina": Equipamento("Catarina: A Lâmina do Ladrão", "Arma", 3500, bonus_ataque=95, peso=1.4, raridade="Epico", classe_exclusiva="Ladino"),
    "besta_vazio": Equipamento("Besta de Repetição do Vazio", "Arma", 3800, bonus_ataque=102, peso=3.5, raridade="Epico", classe_exclusiva="Ladino"),

    "colete_quimera": Equipamento("Colete de Couro de Quimera", "Armadura", 4500, bonus_defesa=62, peso=2.5, raridade="Epico", classe_exclusiva="Ladino"),
    "luvas_maos_leves": Equipamento("Luvas das Mãos Leves", "Armadura", 2500, bonus_defesa=32, peso=0.2, raridade="Epico", classe_exclusiva="Ladino"),
    "botas_espectrais": Equipamento("Botas do Passo Espectral", "Armadura", 2800, bonus_defesa=35, peso=0.5, raridade="Epico", classe_exclusiva="Ladino"),
}

# --- ITENS LADINO: LENDÁRIO (Rank A) ---
ITENS_LADINO_LENDARIO = {
    "adaga_monarca": Equipamento("Adaga do Monarca dos Gatunos", "Arma", 18000, bonus_ataque=175, peso=0.4, raridade="Lendario", classe_exclusiva="Ladino"),
    "lamina_crepusculo": Equipamento("Lâmina do Crepúsculo Eterno", "Arma", 20000, bonus_ataque=190, peso=1.2, raridade="Lendario", classe_exclusiva="Ladino"),
    "punhal_basilisco": Equipamento("Punhal de Presa de Basilisco", "Arma", 19000, bonus_ataque=185, peso=0.5, raridade="Lendario", classe_exclusiva="Ladino"),

    "manto_invisibilidade": Equipamento("Manto da Invisibilidade Real", "Armadura", 25000, bonus_defesa=115, peso=0.8, raridade="Lendario", classe_exclusiva="Ladino"),
    "armadura_sombra": Equipamento("Armadura da Sombra Viva", "Armadura", 22000, bonus_defesa=108, peso=1.8, raridade="Lendario", classe_exclusiva="Ladino"),
    "olho_noite_eterna": Equipamento("Elmo Olho da Noite Eterna", "Armadura", 15000, bonus_defesa=58, peso=0.4, raridade="Lendario", classe_exclusiva="Ladino"),
}

# --- ITENS LADINO: MÍTICO (Rank S) ---
ITENS_LADINO_MITICO = {
    "lamina_caos_ladino": Equipamento("Lâmina do Caos Primordial", "Arma", 130000, bonus_ataque=460, peso=0.3, raridade="Mitico", classe_exclusiva="Ladino"),
    "furto_existencia": Equipamento("O Furto da Existência", "Arma", 160000, bonus_ataque=510, peso=0.1, raridade="Mitico", classe_exclusiva="Ladino"),
    "presagio_morte": Equipamento("Preságio da Morte Silenciosa", "Arma", 140000, bonus_ataque=480, peso=0.5, raridade="Mitico", classe_exclusiva="Ladino"),

    "manto_onipotencia": Equipamento("Manto da Onipresença do Gatuno", "Armadura", 200000, bonus_defesa=245, peso=0.5, raridade="Mitico", classe_exclusiva="Ladino"),
    "traje_fantasma_vazio": Equipamento("Traje do Fantasma do Vazio", "Armadura", 180000, bonus_defesa=230, peso=1.0, raridade="Mitico", classe_exclusiva="Ladino"),
    "diadema_rei_gatuno": Equipamento("Diadema do Rei dos Gatunos", "Armadura", 120000, bonus_defesa=135, peso=0.2, raridade="Mitico", classe_exclusiva="Ladino"),
}