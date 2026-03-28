from Itens import Equipamento

# --- ITENS PALADINO: COMUM (Rank E) ---
ITENS_PALADINO_COMUM = {
    "maca_madeira_pobre": Equipamento("Maça de Madeira Pobre", "Arma", 15, bonus_ataque=3, peso=3.5, raridade="Comum", classe_exclusiva="Paladino"),
    "martelo_ferreiro_velho": Equipamento("Martelo de Ferreiro Velho", "Arma", 20, bonus_ataque=5, peso=5.0, raridade="Comum", classe_exclusiva="Paladino"),
    "lança_guarda_recruta": Equipamento("Lança de Guarda Recruta", "Arma", 25, bonus_ataque=4, peso=4.0, raridade="Comum", classe_exclusiva="Paladino"),

    "peitoral_ferro_gasto": Equipamento("Peitoral de Ferro Gasto", "Armadura", 40, bonus_defesa=6, peso=12.0, raridade="Comum", classe_exclusiva="Paladino"),
    "escudo_carvalho_velho": Equipamento("Escudo de Carvalho Velho", "Armadura", 20, bonus_defesa=4, peso=6.0, raridade="Comum", classe_exclusiva="Paladino"),
    "elmo_aberto_ferro": Equipamento("Elmo Aberto de Ferro", "Armadura", 15, bonus_defesa=3, peso=3.0, raridade="Comum", classe_exclusiva="Paladino"),
}

# --- ITENS PALADINO: INCOMUM (Rank D) ---
ITENS_PALADINO_INCOMUM = {
    "maca_aço_polido": Equipamento("Maça de Aço Polido", "Arma", 150, bonus_ataque=14, peso=4.5, raridade="Incomum", classe_exclusiva="Paladino"),
    "martelo_guerra_padrao": Equipamento("Martelo de Guerra Padrão", "Arma", 180, bonus_ataque=18, peso=6.0, raridade="Incomum", classe_exclusiva="Paladino"),
    "mangual_ferro_pesado": Equipamento("Mangual de Ferro Pesado", "Arma", 170, bonus_ataque=16, peso=5.5, raridade="Incomum", classe_exclusiva="Paladino"),

    "armadura_placas_aço": Equipamento("Armadura de Placas de Aço", "Armadura", 250, bonus_defesa=15, peso=18.0, raridade="Incomum", classe_exclusiva="Paladino"),
    "escudo_aço_brasao": Equipamento("Escudo de Aço com Brasão", "Armadura", 150, bonus_defesa=10, peso=8.0, raridade="Incomum", classe_exclusiva="Paladino"),
    "ombreiras_ferro_reforçadas": Equipamento("Ombreiras de Ferro Reforçadas", "Armadura", 100, bonus_defesa=5, peso=4.0, raridade="Incomum", classe_exclusiva="Paladino"),
}

# --- ITENS PALADINO: RARO (Rank C) ---
ITENS_PALADINO_RARO = {
    "martelo_justiça_brilhante": Equipamento("Martelo da Justiça Brilhante", "Arma", 700, bonus_ataque=42, peso=7.5, raridade="Raro", classe_exclusiva="Paladino"),
    "espada_longa_templaria": Equipamento("Espada Longa do Templário", "Arma", 650, bonus_ataque=38, peso=3.0, raridade="Raro", classe_exclusiva="Paladino"),
    "maça_do_sol_nascente": Equipamento("Maça do Sol Nascente", "Arma", 680, bonus_ataque=40, peso=4.8, raridade="Raro", classe_exclusiva="Paladino"),

    "couraça_prateada": Equipamento("Couraça Prateada Purificada", "Armadura", 1200, bonus_defesa=35, peso=15.0, raridade="Raro", classe_exclusiva="Paladino"),
    "escudo_torre_fé": Equipamento("Escudo Torre da Fé", "Armadura", 800, bonus_defesa=22, peso=14.0, raridade="Raro", classe_exclusiva="Paladino"),
    "elmo_visão_sagrada": Equipamento("Elmo da Visão Sagrada", "Armadura", 500, bonus_defesa=12, peso=4.0, raridade="Raro", classe_exclusiva="Paladino"),
}

# --- ITENS PALADINO: ÉPICO (Rank B) ---
ITENS_PALADINO_EPICO = {
    "quebra_cranios_inquisidor": Equipamento("Quebra-Crânios do Inquisidor", "Arma", 3800, bonus_ataque=95, peso=8.5, raridade="Epico", classe_exclusiva="Paladino"),
    "martelo_punho_de_deus": Equipamento("Martelo Punho de Deus", "Arma", 4200, bonus_ataque=105, peso=10.0, raridade="Epico", classe_exclusiva="Paladino"),
    "lança_julgamento_luz": Equipamento("Lança do Julgamento de Luz", "Arma", 3500, bonus_ataque=90, peso=5.5, raridade="Epico", classe_exclusiva="Paladino"),

    "armadura_bastiao_divino": Equipamento("Armadura Bastião Divino", "Armadura", 5500, bonus_defesa=75, peso=22.0, raridade="Epico", classe_exclusiva="Paladino"),
    "escudo_espelho_sagrado": Equipamento("Escudo Espelho Sagrado", "Armadura", 3200, bonus_defesa=45, peso=12.0, raridade="Epico", classe_exclusiva="Paladino"),
    "manoplas_toque_de_luz": Equipamento("Manoplas do Toque de Luz", "Armadura", 2200, bonus_defesa=25, peso=3.0, raridade="Epico", classe_exclusiva="Paladino"),
}

# --- ITENS PALADINO: LENDÁRIO (Rank A) ---
ITENS_PALADINO_LENDARIO = {
    "martelo_titan_do_sol": Equipamento("Martelo Titã do Sol", "Arma", 22000, bonus_ataque=200, peso=15.0, raridade="Lendario", classe_exclusiva="Paladino"),
    "maça_estrela_da_manha_real": Equipamento("Estrela da Manhã Real", "Arma", 20000, bonus_ataque=190, peso=7.0, raridade="Lendario", classe_exclusiva="Paladino"),
    "espada_sagrada_durandal": Equipamento("Espada Sagrada Durandal", "Arma", 25000, bonus_ataque=215, peso=4.5, raridade="Lendario", classe_exclusiva="Paladino"),

    "armadura_paladino_eterno": Equipamento("Armadura do Paladino Eterno", "Armadura", 30000, bonus_defesa=145, peso=25.0, raridade="Lendario", classe_exclusiva="Paladino"),
    "escudo_egide_da_luz": Equipamento("Escudo Égide de Luz", "Armadura", 18000, bonus_defesa=90, peso=16.0, raridade="Lendario", classe_exclusiva="Paladino"),
    "elmo_coroa_do_santo": Equipamento("Elmo Coroa do Santo", "Armadura", 12000, bonus_defesa=60, peso=5.0, raridade="Lendario", classe_exclusiva="Paladino"),
}

# --- ITENS PALADINO: MÍTICO (Rank S) ---
ITENS_PALADINO_MITICO = {
    "martelo_do_genesis": Equipamento("Martelo do Gênese Cósmico", "Arma", 160000, bonus_ataque=520, peso=12.0, raridade="Mitico", classe_exclusiva="Paladino"),
    "maça_juizo_final": Equipamento("Maça do Juízo Final", "Arma", 145000, bonus_ataque=490, peso=9.0, raridade="Mitico", classe_exclusiva="Paladino"),
    "lamina_do_arcanjo_supremo": Equipamento("Lâmina do Arcanjo Supremo", "Arma", 180000, bonus_ataque=550, peso=5.0, raridade="Mitico", classe_exclusiva="Paladino"),

    "armadura_de_deus": Equipamento("A Armadura de Deus (Original)", "Armadura", 250000, bonus_defesa=320, peso=15.0, raridade="Mitico", classe_exclusiva="Paladino"),
    "escudo_fortaleza_absoluta": Equipamento("Escudo Fortaleza Absoluta", "Armadura", 150000, bonus_defesa=180, peso=20.0, raridade="Mitico", classe_exclusiva="Paladino"),
    "elmo_onipotencia_sacra": Equipamento("Elmo da Onipotência Sacra", "Armadura", 110000, bonus_defesa=140, peso=4.0, raridade="Mitico", classe_exclusiva="Paladino"),
}