# =================================================================
# 1. IMPORTAÇÕES E CONFIGURAÇÕES INICIAIS
# =================================================================
import os
import random
from Player import player
from Classes import CLASSES, PROFISOES
from Itens import Equipamento, ITENS_BASICOS # Importamos a classe e o banco de dados

# =================================================================
# 2. FUNÇÕES DE UTILIDADE E INTERFACE
# =================================================================
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_ficha(p):
    """Exibe os atributos principais e HP do jogador."""
    print("\n" + "═"*45)
    print(f"   📜 FICHA DO JOGADOR: {p.nome.upper()}")
    print(f"   Classe: {p.classe} | Profissão: {p.profissao}")
    print(f"   HP: {p.hp_atual:.1f}/{p.hp_max} | Vidas: {p.vidas}")
    print("-" * 45)
    print(f" 💪 Força: {p.forca:<12} 🎯 Destreza: {p.destreza}")
    print(f" ⚡ Agilidade: {p.agilidade:<12} 🧠 Inteligência: {p.inteligencia}")
    print(f" 🩸 Vitalidade: {p.vitalidade:<12} 🗣️  Carisma: {p.carisma}")
    print(f" 🍀 Sorte: {p.sorte}")
    print("-" * 45)
    print(f" ✨ Prodígio: {'SIM (Bônus Ativo)' if p.is_prodigio else 'Não'}")
    print("═"*45)

def exibir_equipamento(p):
    """Exibe o que o jogador está vestindo em cada slot."""
    print("\n" + "🛡️  EQUIPAMENTOS ATUAIS".center(45))
    for slot, item in p.equipamento.items():
        if item:
            status = f"(Atq: +{item.bonus_ataque} | Def: +{item.bonus_defesa})"
            nome_exibir = f"{item.nome} {status}"
        else:
            nome_exibir = "Vazio"
        
        # Formata o nome do slot (ex: mao_principal -> Mão Principal)
        slot_nome = slot.replace("_", " ").capitalize()
        print(f" [{slot_nome}]: {nome_exibir}")
    print("═"*45)

# =================================================================
# 3. MENU DE CRIAÇÃO DE PERSONAGEM
# =================================================================
def menu_criacao():
    limpar_tela()
    print("=== ⚔️  SISTEMA DE DESPERTAR: REINOS DE PYTHONIA ⚔️  ===")
    nome = input("Qual é seu nome, caro viajante: ")

    # Validação de Classe
    while True:
        print("\n--- 🛡️  ESCOLHA SUA CLASSE ---")
        for c in CLASSES:
            print(f"[{c}] - {CLASSES[c]['descricao']}")
        escolha_c = input("\nDigite o nome da classe: ").strip().capitalize()
        if escolha_c in CLASSES:
            classe_escolhida = escolha_c
            break
        print(f"⚠️ Erro: '{escolha_c}' não existe!")

    # Validação de Profissão
    while True:
        print("\n--- 🛠️  ESCOLHA SUA PROFISSÃO ---")
        for p in PROFISOES:
            print(f"[{p}] - {PROFISOES[p]['passiva']}")
        escolha_p = input("\nDigite o nome da profissão: ").strip().capitalize()
        if escolha_p in PROFISOES:
            profissao_escolhida = escolha_p
            break
        print(f"⚠️ Erro: '{escolha_p}' é inválida!")

    return player(nome, classe_escolhida, "Vila Inicial", profissao_escolhida)

# =================================================================
# 4. EXECUÇÃO PRINCIPAL (MAIN)
# =================================================================
if __name__ == "__main__":
    # Passo 1: Criar o personagem
    p1 = menu_criacao()
    limpar_tela()
    print("\n[SISTEMA]: Personagem registrado com sucesso!")
    exibir_ficha(p1)

    # Passo 2: Simular teste de itens
    print("\n" + "🧪 INICIANDO TESTE DE ITENS... ".center(45))
    input(" Pressione Enter para receber itens básicos...")

    # Pegando itens do seu banco de dados ITENS_BASICOS
    arma_teste = ITENS_BASICOS["espada_ferro"]
    escudo_teste = ITENS_BASICOS["escudo_madeira"]

    # =================================================================
    # 5. LÓGICA DE INVENTÁRIO E EQUIPAMENTO
    # =================================================================
    # Adicionando ao inventário do player
    p1.adicionar_item(arma_teste)
    p1.adicionar_item(escudo_teste)

    print(f"\n📦 Itens adicionados: {arma_teste.nome} e {escudo_teste.nome}")
    
    # Equipando os itens
    p1.equipar_item(arma_teste)
    p1.equipar_item(escudo_teste)

    # =================================================================
    # 6. RESULTADO FINAL
    # =================================================================
    print("\n[SISTEMA]: Status atualizados após equipar!")
    exibir_ficha(p1)
    exibir_equipamento(p1)
    
    print("\n✅ Teste concluído com sucesso!")