
#impor da pasta itens pra pode ter um arquvio só de itens do guerreiro
from Itens import Equipamento

#itens do guerreiro
# --- ITENS GUERREIRO: COMUM (Rank E) ---
ITENS_GUERREIRO_COMUM = {
    "espada_treino": Equipamento("Espada de Treino", "Arma", 10, bonus_ataque=2, peso=1.5, raridade="Comum"),
    "machado_ferrugem": Equipamento("Machado Enferrujado", "Arma", 15, bonus_ataque=4, peso=4.0, raridade="Comum"),
    "clava_madeira": Equipamento("Clava de Madeira", "Arma", 8, bonus_ataque=3, peso=3.0, raridade="Comum"),

    "gibao_couro_velho": Equipamento("Gibão de Couro Velho", "Armadura", 15, bonus_defesa=2, peso=3.0, raridade="Comum"),
    "peitoral_ferro_trincado": Equipamento("Peitoral de Ferro Trincado", "Armadura", 50, bonus_defesa=5, peso=8.0, raridade="Comum"),
    "elmo_aberto": Equipamento("Elmo de Ferro Aberto", "Armadura", 20, bonus_defesa=2, peso=2.0, raridade="Comum"),
}

# --- ITENS GUERREIRO: INCOMUM (Rank D) ---
ITENS_GUERREIRO_INCOMUM = {
    "espada_aço_guarda": Equipamento("Espada de Aço da Guarda", "Arma", 150, bonus_ataque=14, peso=2.5, raridade="Incomum"),
    "machado_batalha_duplo": Equipamento("Machado de Batalha Duplo", "Arma", 180, bonus_ataque=16, peso=5.0, raridade="Incomum"),
    "espada_larga_mercenario": Equipamento("Espada Larga de Mercenário", "Arma", 200, bonus_ataque=18, peso=4.5, raridade="Incomum"),

    "peitoral_aço_recrutamento": Equipamento("Peitoral de Aço de Recrutamento", "Armadura", 250, bonus_defesa=12, peso=10.0, raridade="Incomum"),
    "elmo_aço_fechado": Equipamento("Elmo de Aço Fechado", "Armadura", 120, bonus_defesa=6, peso=3.5, raridade="Incomum"),
    "escudo_aço_redondo": Equipamento("Escudo de Aço Redondo", "Armadura", 150, bonus_defesa=9, peso=6.0, raridade="Incomum"),
}

# --- ITENS GUERREIRO: RARO (Rank C) (01-50) ---
# --- ITENS GUERREIRO: RARO (Rank C) ---
ITENS_GUERREIRO_RARO = {
    "espada_aço_valiriano": Equipamento("Espada de Aço Valiriano", "Arma", 500, bonus_ataque=35, peso=2.2, raridade="Raro"),
    "machado_corta_rocha": Equipamento("Machado Corta-Rocha", "Arma", 550, bonus_ataque=38, peso=6.0, raridade="Raro"),
    "martelo_guerra_pesado": Equipamento("Martelo de Guerra Pesado", "Arma", 600, bonus_ataque=42, peso=8.5, raridade="Raro"),

    "armadura_placas_completa": Equipamento("Armadura de Placas Completa", "Armadura", 800, bonus_defesa=30, peso=20.0, raridade="Raro"),
    "escudo_torre_aço": Equipamento("Escudo Torre de Aço", "Armadura", 450, bonus_defesa=18, peso=12.0, raridade="Raro"),
    "elmo_crina_leao": Equipamento("Elmo Crina de Leão", "Armadura", 300, bonus_defesa=12, peso=4.5, raridade="Raro"),
}

# --- ITENS GUERREIRO: ÉPICO (Rank B) ---
ITENS_GUERREIRO_EPICO = {
    "montante_chamas_eternas": Equipamento("Montante das Chamas Eternas", "Arma", 2500, bonus_ataque=75, peso=7.0, raridade="Epico"),
    "lança_trovao_azul": Equipamento("Lança do Trovão Azul", "Arma", 2200, bonus_ataque=68, peso=4.5, raridade="Epico"),
    "machado_barbaro_ancestral": Equipamento("Machado Bárbaro Ancestral", "Arma", 2800, bonus_ataque=82, peso=9.0, raridade="Epico"),

    "coraca_ouro_escuro": Equipamento("Couraça de Ouro Escuro", "Armadura", 3500, bonus_defesa=65, peso=18.0, raridade="Epico"),
    "escudo_espelhado": Equipamento("Escudo Espelhado", "Armadura", 1800, bonus_defesa=35, peso=10.0, raridade="Epico"),
    "manoplas_força_titan": Equipamento("Manoplas da Força Titã", "Armadura", 1200, bonus_defesa=22, peso=3.5, raridade="Epico"),
}

# --- ITENS GUERREIRO: LENDÁRIO (Rank A) ---
ITENS_GUERREIRO_LENDARIO = {
    "excalibur_falsa": Equipamento("Fragmento da Excalibur", "Arma", 12000, bonus_ataque=150, peso=4.0, raridade="Lendario"),
    "martelo_mjolnir_imitacao": Equipamento("Martelo do Esmagador de Estrelas", "Arma", 15000, bonus_ataque=165, peso=15.0, raridade="Lendario"),
    "lança_longinus_quebrada": Equipamento("Lança do Julgamento", "Arma", 13500, bonus_ataque=158, peso=5.5, raridade="Lendario"),

    "armadura_soberano_aço": Equipamento("Armadura do Soberano de Aço", "Armadura", 18000, bonus_defesa=130, peso=25.0, raridade="Lendario"),
    "escudo_egide_dragao": Equipamento("Escudo Égide de Dragão", "Armadura", 9000, bonus_defesa=75, peso=14.0, raridade="Lendario"),
    "elmo_imperador_guerra": Equipamento("Elmo do Imperador da Guerra", "Armadura", 7500, bonus_defesa=55, peso=5.0, raridade="Lendario"),
}

# --- ITENS GUERREIRO: MÍTICO (Rank S) ---
ITENS_GUERREIRO_MITICO = {
    "matadora_de_deuses": Equipamento("A Matadora de Deuses", "Arma", 60000, bonus_ataque=350, peso=6.0, raridade="Mitico"),
    "destruidora_mundos": Equipamento("Destruidora de Mundos", "Arma", 65000, bonus_ataque=380, peso=20.0, raridade="Mitico"),
    "espada_genesis": Equipamento("Espada do Gênese", "Arma", 70000, bonus_ataque=400, peso=5.0, raridade="Mitico"),

    "armadura_eternidade": Equipamento("Armadura da Eternidade Absoluta", "Armadura", 85000, bonus_defesa=280, peso=30.0, raridade="Mitico"),
    "escudo_vazio_infinito": Equipamento("Escudo do Vazio Infinito", "Armadura", 40000, bonus_defesa=150, peso=18.0, raridade="Mitico"),
    "elmo_panteao": Equipamento("Elmo do Panteão Divino", "Armadura", 35000, bonus_defesa=120, peso=6.0, raridade="Mitico"),
}