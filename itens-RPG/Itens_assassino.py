#arquivo dos itens de assasinos

from Itens import Equipamento


ITENS_ASSASSINO_COMUM = {
    "adaga_ferrugem": Equipamento("Adaga Enferrujada", "Arma", 15, bonus_ataque=3, peso=0.4, raridade="Comum"),
    "faca_arremesso_cega": Equipamento("Faca de Arremesso Cega", "Arma", 10, bonus_ataque=2, peso=0.2, raridade="Comum"),
    "punhal_madeira_treino": Equipamento("Punhal de Treino", "Arma", 8, bonus_ataque=2, peso=0.3, raridade="Comum"),

    "capuz_tecido_sujo": Equipamento("Capuz de Tecido Sujo", "Armadura", 12, bonus_defesa=1, peso=0.2, raridade="Comum"),
    "tunica_couro_fina": Equipamento("Túnica de Couro Fina", "Armadura", 50, bonus_defesa=3, peso=1.5, raridade="Comum"),
    "botas_pano_velhas": Equipamento("Botas de Pano Velhas", "Armadura", 20, bonus_defesa=1, peso=0.4, raridade="Comum"),
}

# --- ITENS ASSASSINO: INCOMUM (Rank D) ---
ITENS_ASSASSINO_INCOMUM = {
    "adaga_aço_negro": Equipamento("Adaga de Aço Negro", "Arma", 150, bonus_ataque=12, peso=0.4, raridade="Incomum"),
    "sai_ferro_polido": Equipamento("Sai de Ferro Polido", "Arma", 130, bonus_ataque=11, peso=0.6, raridade="Incomum"),
    "adaga_aprendiz_assassino": Equipamento("Adaga de Aprendiz (Rank D)", "Arma", 180, bonus_ataque=14, peso=0.4, raridade="Incomum"),

    "traje_couro_ajustado": Equipamento("Traje de Couro Ajustado", "Armadura", 220, bonus_defesa=8, peso=2.0, raridade="Incomum"),
    "capuz_assassino_d": Equipamento("Capuz de Assassino (Rank D)", "Armadura", 140, bonus_defesa=6, peso=0.3, raridade="Incomum"),
    "botas_passo_leve": Equipamento("Botas de Passo Leve", "Armadura", 130, bonus_defesa=5, peso=0.5, raridade="Incomum"),
}

# --- ITENS ASSASSINO: RARO (Rank C) (01-50) ---
# --- ITENS ASSASSINO: RARO (Rank C) ---
ITENS_ASSASSINO_RARO = {
    "adaga_ferro_negro": Equipamento("Adaga de Ferro Negro", "Arma", 450, bonus_ataque=28, peso=0.4, raridade="Raro"),
    "punhal_misericordia": Equipamento("Punhal da Misericórdia", "Arma", 480, bonus_ataque=31, peso=0.3, raridade="Raro"),
    "garra_pantera_negra": Equipamento("Garras de Pantera Negra", "Arma", 520, bonus_ataque=33, peso=0.7, raridade="Raro"),

    "traje_assassino_noturno": Equipamento("Traje do Assassino Noturno", "Armadura", 800, bonus_defesa=24, peso=2.2, raridade="Raro"),
    "capuz_executor_c": Equipamento("Capuz do Executor", "Armadura", 350, bonus_defesa=12, peso=0.4, raridade="Raro"),
    "botas_passada_silenciosa": Equipamento("Botas da Passada Silenciosa", "Armadura", 320, bonus_defesa=10, peso=0.5, raridade="Raro"),
}

# --- ITENS ASSASSINO: ÉPICO (Rank B) ---
ITENS_ASSASSINO_EPICO = {
    "lamina_presagista_noite": Equipamento("Lâmina Presagista da Noite", "Arma", 1600, bonus_ataque=55, peso=0.4, raridade="Epico"),
    "adaga_presa_hidra": Equipamento("Presa de Hidra Venenosa", "Arma", 1850, bonus_ataque=62, peso=0.3, raridade="Epico"),
    "punhal_beijo_viuva": Equipamento("Beijo da Viúva Negra", "Arma", 2100, bonus_ataque=68, peso=0.2, raridade="Epico"),

    "traje_espectro_noturno": Equipamento("Traje do Espectro Noturno", "Armadura", 2800, bonus_defesa=58, peso=1.8, raridade="Epico"),
    "mascara_sorriso_demoniaco": Equipamento("Máscara do Sorriso Demoníaco", "Armadura", 1400, bonus_defesa=30, peso=0.4, raridade="Epico"),
    "manto_nevoa_vazia": Equipamento("Manto da Névoa do Vazio", "Armadura", 3200, bonus_defesa=65, peso=1.0, raridade="Epico"),
}

# --- ITENS ASSASSINO: LENDÁRIO (Rank A) ---
ITENS_ASSASSINO_LENDARIO = {
    "adaga_monarca_sombras": Equipamento("Lâmina do Monarca das Sombras", "Arma", 9500, bonus_ataque=145, peso=0.3, raridade="Lendario"),
    "garra_fenris_lendaria": Equipamento("Garras de Fenris", "Arma", 9200, bonus_ataque=142, peso=0.6, raridade="Lendario"),
    "lamina_corte_espacial": Equipamento("Lâmina do Corte Espacial", "Arma", 10500, bonus_ataque=155, peso=0.4, raridade="Lendario"),

    "manto_soberano_sombras": Equipamento("Manto do Soberano das Sombras", "Armadura", 12500, bonus_defesa=115, peso=1.0, raridade="Lendario"),
    "traje_caçador_rank_s": Equipamento("Traje do Caçador Lendário", "Armadura", 14000, bonus_defesa=130, peso=2.0, raridade="Lendario"),
    "mascara_vulto_eterno": Equipamento("Máscara do Vulto Eterno", "Armadura", 6500, bonus_defesa=58, peso=0.3, raridade="Lendario"),
}

# --- ITENS ASSASSINO: MÍTICO (Rank S) ---
ITENS_ASSASSINO_MITICO = {
    "ira_de_kamish": Equipamento("Ira de Kamish", "Arma", 45000, bonus_ataque=310, peso=0.3, raridade="Mitico"),
    "lamina_deus_morte": Equipamento("Lâmina do Deus da Morte", "Arma", 50000, bonus_ataque=330, peso=0.2, raridade="Mitico"),
    "punhal_vazio_absoluto": Equipamento("Punhal do Vazio Absoluto", "Arma", 42000, bonus_ataque=295, peso=0.1, raridade="Mitico"),

    "manto_onipresença": Equipamento("Manto da Onipresença", "Armadura", 60000, bonus_defesa=220, peso=0.5, raridade="Mitico"),
    "traje_avatar_sombra": Equipamento("Avatar da Sombra Final", "Armadura", 65000, bonus_defesa=240, peso=1.5, raridade="Mitico"),
    "mascara_pesadelo_mitico": Equipamento("Máscara do Pesadelo Real", "Armadura", 35000, bonus_defesa=110, peso=0.3, raridade="Mitico"),
}