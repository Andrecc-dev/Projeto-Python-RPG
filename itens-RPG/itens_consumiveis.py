# --- CONSUMÍVEIS: POÇÕES, ELIXIRES E COMIDAS ---

ITENS_CONSUMIVEIS_COMUM = {
    "poçao_vida_p": {"nome": "Poção de Vida Menor", "tipo": "Cura", "valor": 20, "preço": 10, "raridade": "Comum"},
    "poçao_mana_p": {"nome": "Poção de Mana Menor", "tipo": "Energia", "valor": 15, "preço": 12, "raridade": "Comum"},
    "erva_medicinal": {"nome": "Erva Medicinal", "tipo": "Cura", "valor": 10, "preço": 5, "raridade": "Comum"},
    "pao_velho": {"nome": "Pão Amanhecido", "tipo": "Comida", "valor": 5, "preço": 2, "raridade": "Comum"},
    "agua_poço": {"nome": "Água de Poço", "tipo": "Energia", "valor": 5, "preço": 1, "raridade": "Comum"},
    "fruta_silvestre": {"nome": "Fruta Silvestre", "tipo": "Cura", "valor": 8, "preço": 3, "raridade": "Comum"},
}

ITENS_CONSUMIVEIS_INCOMUM = {
    "poçao_vida_m": {"nome": "Poção de Vida Média", "tipo": "Cura", "valor": 50, "preço": 40, "raridade": "Incomum"},
    "poçao_mana_m": {"nome": "Poção de Mana Média", "tipo": "Energia", "valor": 40, "preço": 45, "raridade": "Incomum"},
    "tonico_força": {"nome": "Tônico de Força", "tipo": "Buff", "atributo": "forca", "bonus": 2, "preço": 60, "raridade": "Incomum"},
    "elixir_agilidade": {"nome": "Elixir de Agilidade", "tipo": "Buff", "atributo": "agilidade", "bonus": 2, "preço": 60, "raridade": "Incomum"},
    "carne_assada": {"nome": "Carne de Caça Assada", "tipo": "Comida", "valor": 25, "preço": 20, "raridade": "Incomum"},
    "cha_calmante": {"nome": "Chá de Ervas Calmante", "tipo": "Energia", "valor": 25, "preço": 15, "raridade": "Incomum"},
}

ITENS_CONSUMIVEIS_RARO = {
    "poçao_vida_g": {"nome": "Poção de Vida Maior", "tipo": "Cura", "valor": 120, "preço": 150, "raridade": "Raro"},
    "poçao_mana_g": {"nome": "Poção de Mana Maior", "tipo": "Energia", "valor": 100, "preço": 160, "raridade": "Raro"},
    "elixir_foco": {"nome": "Elixir de Foco Mental", "tipo": "Buff", "atributo": "inteligencia", "bonus": 5, "preço": 200, "raridade": "Raro"},
    "perfume_carisma": {"nome": "Perfume de Magnata", "tipo": "Buff", "atributo": "carisma", "bonus": 5, "preço": 300, "raridade": "Raro"},
    "oleo_afiador": {"nome": "Óleo de Afiar Raro", "tipo": "Buff_Dano", "bonus": 10, "preço": 250, "raridade": "Raro"},
    "vinho_encantado": {"nome": "Vinho Encantado", "tipo": "Cura/Energia", "valor": 70, "preço": 220, "raridade": "Raro"},
}

ITENS_CONSUMIVEIS_EPICO = {
    "elixir_rejuvenescimento": {"nome": "Elixir de Rejuvenescimento", "tipo": "Cura_Alta", "valor": 300, "preço": 800, "raridade": "Epico"},
    "extrato_nen_puro": {"nome": "Extrato de Nen Puro", "tipo": "Energia_Alta", "valor": 250, "preço": 900, "raridade": "Epico"},
    "banquete_rei": {"nome": "Banquete Real Portátil", "tipo": "Cura_Total", "valor": 999, "preço": 2000, "raridade": "Epico"},
    "sangue_dragao_vial": {"nome": "Vial de Sangue de Dragão", "tipo": "Buff_Atributos", "bonus": 10, "preço": 1500, "raridade": "Epico"},
    "cristal_mana_instavel": {"nome": "Cristal de Mana Instável", "tipo": "Energia_Imediata", "valor": 500, "preço": 1800, "raridade": "Epico"},
    "po_diamante": {"nome": "Pó de Diamante", "tipo": "Buff_Defesa", "bonus": 20, "preço": 1200, "raridade": "Epico"},
}

ITENS_CONSUMIVEIS_LENDARIO = {
    "ambrosia_celestial": {"nome": "Ambrósia Celestial", "tipo": "Cura_Full", "valor": 9999, "preço": 5000, "raridade": "Lendario"},
    "essencia_estelar": {"nome": "Essência Estelar", "tipo": "Energia_Full", "valor": 9999, "preço": 5500, "raridade": "Lendario"},
    "elixir_titan": {"nome": "Elixir do Titã Inabalável", "tipo": "Buff_HP_Max", "bonus": 100, "preço": 7000, "raridade": "Lendario"},
    "orvalho_yggdrasil": {"nome": "Orvalho de Yggdrasil", "tipo": "Cura/Energia_Full", "valor": 9999, "preço": 10000, "raridade": "Lendario"},
    "extrato_vazio": {"nome": "Extrato do Vazio", "tipo": "Invisibilidade_Temp", "preço": 8000, "raridade": "Lendario"},
    "fruta_eden": {"nome": "Fruta do Éden", "tipo": "Buff_Todos_Status", "bonus": 15, "preço": 15000, "raridade": "Lendario"},
}

ITENS_CONSUMIVEIS_MITICO = {
    "sangue_de_deus": {"nome": "Ichor: Sangue dos Deuses", "tipo": "Super_Buff", "bonus": 50, "preço": 50000, "raridade": "Mitico"},
    "mana_original": {"nome": "Mana das Origens", "tipo": "Custo_Zero_Mana", "preço": 45000, "raridade": "Mitico"},
    "pêlo_fenrir": {"nome": "Pêlo de Fenrir", "tipo": "Buff_Agilidade_Extremo", "bonus": 100, "preço": 40000, "raridade": "Mitico"},
    "lágrima_gais": {"nome": "Lágrima de Gaia", "tipo": "Invulnerabilidade_Curta", "preço": 60000, "raridade": "Mitico"},
    "coraçao_vulcao": {"nome": "Coração de Vulcão", "tipo": "Dano_Fogo_Passivo", "preço": 55000, "raridade": "Mitico"},
    "olho_providencia": {"nome": "Olho da Providência", "tipo": "Revelar_Fraqueza", "preço": 70000, "raridade": "Mitico"},
}