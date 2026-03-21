#agora vamos começar as classes

#definição das classes com bonus/penalidades

CLASSES = {
    "Guerreiro": {
        "forca": 2, "vitalidade": 1, "carisma": -1,
        "descricao": "Dano físico e resistência."
    },
    "Assassino": {
        "agilidade": 2, "destreza": 1, "forca": -1,
        "descricao": "Esquiva e ataques críticos."
    },
    "Mago": {
        "inteligencia": 3, "vitalidade": -1,
        "descricao": "Poder de Nen e magias futuras."
    },
    "Arqueiro": {
        "destreza": 2, "agilidade": 1, "carisma": -1,
        "descricao": "Precisão à distância."
    },
    "Paladino": {
        "vitalidade": 2, "carisma": 1, "destreza": -1,
        "descricao": "Tanque e bom com NPCs."
    },
    "Ladino": {
        "carisma": 2, "destreza": 1, "vitalidade": -1,
        "descricao": "Lábia, furtos e economia."
    },
    "Barbaro": {
        "forca": 3, "inteligencia": -1,
        "descricao": "Dano bruto e fúria."
    }
}

PROFISOES = {
    "Ferreiro": {"forca": 2, "destreza": 1, "agilidade": -1, "passiva": "Melhora dano de armas de metal."},

    "Alquimista": {"inteligencia": 2, "sorte": 1, "vitalidade": -1, "passiva": "Chance de dobrar cura de poções."},

    "Cozinheiro": {"vitalidade": 2, "carisma": 1, "agilidade": -1, "passiva": "Comidas recuperam +50% de Fadiga."},

    "Herborista": {"inteligencia": 2, "destreza": 1, "forca": -1, "passiva": "Encontra mais itens em florestas."},

    "Mercador": {"carisma": 3, "forca": -1, "passiva": "Vende itens por +20% de Gold."},

    "Ladrão": {"agilidade": 2, "sorte": 1, "carisma": -1, "passiva": "Chance de furtar Gold de inimigos."},

    "Caçador": {"destreza": 2, "agilidade": 1, "carisma": -1, "passiva": "Maior drop de itens de animais."},

    "Mineiro": {"vitalidade": 2, "forca": 1, "inteligencia": -1, "passiva": "Gold extra em cavernas."},

    "Alfaiate": {"destreza": 2, "carisma": 1, "vitalidade": -1, "passiva": "Melhora defesa de armaduras leves."},

    "Bibliotecário": {"inteligencia": 3, "forca": -1, "passiva": "Ganha +10% de XP."},

    "Jogador": {"sorte": 3, "inteligencia": -1, "passiva": "Eventos aleatórios favoráveis."},

    "Guarda": {"forca": 1, "vitalidade": 2, "sorte": -1, "passiva": "Reduz fadiga ao viajar."},

    "Bardo": {"carisma": 2, "agilidade": 1, "destreza": -1, "passiva": "Taverna grátis."},

    "Carpinteiro": {"destreza": 2, "forca": 1, "sorte": -1, "passiva": "Itens de madeira mais baratos."},
    
    "Coveiro": {"vitalidade": 2, "sorte": 1, "carisma": -1, "passiva": "Acha itens raros em corpos."}
}