from Itens import Equipamento

# --- ITENS MAGO: COMUM (Rank E) ---
ITENS_MAGO_COMUM = {
    # ARMAS (Cajados/Grimórios)
    "graveto_encantado": Equipamento("Graveto de Carvalho Encantado", "Arma", 15, bonus_ataque=4, peso=1.0, raridade="Comum"),
    "grimorio_mofado": Equipamento("Grimório Mofado", "Arma", 20, bonus_ataque=3, peso=0.8, raridade="Comum"),
    "cristal_focado_lascado": Equipamento("Cristal de Foco Lascado", "Arma", 25, bonus_ataque=5, peso=0.4, raridade="Comum"),

    # ARMADURAS (Mantos/Chapéus)
    "manto_aprendiz_velho": Equipamento("Manto de Aprendiz Velho", "Armadura", 30, bonus_defesa=2, peso=1.0, raridade="Comum"),
    "chapeu_pontudo_trapos": Equipamento("Chapéu Pontudo de Trapos", "Armadura", 15, bonus_defesa=1, peso=0.3, raridade="Comum"),
    "sandalias_tecido": Equipamento("Sandálias de Tecido Simples", "Armadura", 10, bonus_defesa=1, peso=0.2, raridade="Comum"),
}

# --- ITENS MAGO: INCOMUM (Rank D) ---
ITENS_MAGO_INCOMUM = {
    "cajado_freixo_polido": Equipamento("Cajado de Freixo Polido", "Arma", 160, bonus_ataque=15, peso=1.5, raridade="Incomum"),
    "orbe_vidro_marinho": Equipamento("Orbe de Vidro Marinho", "Arma", 140, bonus_ataque=13, peso=0.6, raridade="Incomum"),
    "grimorio_elemental_rasgado": Equipamento("Grimório Elemental Rasgado", "Arma", 180, bonus_ataque=17, peso=1.0, raridade="Incomum"),

    "veste_linho_mago": Equipamento("Veste de Linho de Mago", "Armadura", 150, bonus_defesa=8, peso=1.2, raridade="Incomum"),
    "amuleto_protecao_menor": Equipamento("Amuleto de Proteção Menor", "Armadura", 110, bonus_defesa=4, peso=0.2, raridade="Incomum"),
    "luvas_seda_arcana": Equipamento("Luvas de Seda Arcana", "Armadura", 90, bonus_defesa=3, peso=0.3, raridade="Incomum"),
}

# --- ITENS MAGO: RARO (Rank C) ---
ITENS_MAGO_RARO = {
    "cajado_cristal_mana": Equipamento("Cajado de Cristal de Mana", "Arma", 600, bonus_ataque=40, peso=1.8, raridade="Raro"),
    "grimorio_chamas_vivas": Equipamento("Grimório das Chamas Vivas", "Arma", 650, bonus_ataque=45, peso=1.2, raridade="Raro"),
    "cetro_nevoa_gelida": Equipamento("Cetro da Névoa Gélida", "Arma", 580, bonus_ataque=42, peso=1.4, raridade="Raro"),

    "toga_tecido_estelar": Equipamento("Toga de Tecido Estelar", "Armadura", 750, bonus_defesa=22, peso=1.5, raridade="Raro"),
    "tiara_foco_mental": Equipamento("Tiara de Foco Mental", "Armadura", 400, bonus_defesa=10, peso=0.4, raridade="Raro"),
    "botas_levitacao_leve": Equipamento("Botas de Levitação Leve", "Armadura", 350, bonus_defesa=12, peso=0.6, raridade="Raro"),
}

# --- ITENS MAGO: ÉPICO (Rank B) ---
ITENS_MAGO_EPICO = {
    "cajado_arquimago_merlin": Equipamento("Cajado do Arquimago Ancião", "Arma", 3200, bonus_ataque=90, peso=2.0, raridade="Epico"),
    "codice_vazio_profundo": Equipamento("Códice do Vazio Profundo", "Arma", 3500, bonus_ataque=98, peso=1.5, raridade="Epico"),
    "orbe_olho_do_dragao": Equipamento("Orbe do Olho do Dragão", "Arma", 3000, bonus_ataque=92, peso=1.0, raridade="Epico"),

    "manto_fuga_dimensional": Equipamento("Manto da Fuga Dimensional", "Armadura", 4200, bonus_defesa=55, peso=1.5, raridade="Epico"),
    "capuz_silencio_arcano": Equipamento("Capuz do Silêncio Arcano", "Armadura", 2100, bonus_defesa=30, peso=0.5, raridade="Epico"),
    "cinto_alquimista_mestre": Equipamento("Cinto do Alquimista Mestre", "Armadura", 1800, bonus_defesa=25, peso=0.8, raridade="Epico"),
}

# --- ITENS MAGO: LENDÁRIO (Rank A) ---
ITENS_MAGO_LENDARIO = {
    "baculo_eterno_aeon": Equipamento("Báculo Eterno de Aeon", "Arma", 18000, bonus_ataque=180, peso=2.5, raridade="Lendario"),
    "grimorio_pecados_originais": Equipamento("Grimório dos Pecados Originais", "Arma", 20000, bonus_ataque=195, peso=2.0, raridade="Lendario"),
    "cetro_soberano_raio": Equipamento("Cetro do Soberano do Trovão", "Arma", 17000, bonus_ataque=175, peso=1.8, raridade="Lendario"),

    "veste_fenix_sagrada": Equipamento("Veste da Fênix Sagrada", "Armadura", 25000, bonus_defesa=110, peso=1.0, raridade="Lendario"),
    "coroa_rei_feiticeiro": Equipamento("Coroa do Rei Feiticeiro", "Armadura", 15000, bonus_defesa=60, peso=0.8, raridade="Lendario"),
    "bracelete_supernova": Equipamento("Bracelete da Supernova", "Armadura", 12000, bonus_defesa=50, peso=0.3, raridade="Lendario"),
}

# --- ITENS MAGO: MÍTICO (Rank S) ---
ITENS_MAGO_MITICO = {
    "cajado_genesis_omega": Equipamento("Cajado Gênese & Ômega", "Arma", 120000, bonus_ataque=450, peso=2.0, raridade="Mitico"),
    "olho_da_providencia": Equipamento("O Olho da Providência Cósmica", "Arma", 150000, bonus_ataque=520, peso=0.5, raridade="Mitico"),
    "livro_realidade_escrita": Equipamento("Manuscrito da Realidade Escrita", "Arma", 110000, bonus_ataque=430, peso=1.2, raridade="Mitico"),

    "manto_deus_arcano": Equipamento("Manto da Singularidade Divina", "Armadura", 200000, bonus_defesa=250, peso=0.0, raridade="Mitico"),
    "aura_protecao_absoluta": Equipamento("Aura da Proteção Absoluta", "Armadura", 180000, bonus_defesa=220, peso=0.0, raridade="Mitico"),
    "diadema_onisciente": Equipamento("Diadema do Observador Onisciente", "Armadura", 100000, bonus_defesa=130, peso=0.1, raridade="Mitico"),
}