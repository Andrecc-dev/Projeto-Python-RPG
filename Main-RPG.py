# =================================================================
# 1. IMPORTAÇÕES E CONFIGURAÇÕES INICIAIS
# =================================================================
import os
import random
from Player import player
from Classes import CLASSES, PROFISOES
# Importamos apenas o necessário para o funcionamento real agora
from Itens import ARMAS_INICIAIS, ARMADURAS_INICIAIS 

# =================================================================
# 2. FUNÇÕES DE UTILIDADE E INTERFACE
# =================================================================
def limpar_tela():
    """Limpa o terminal de acordo com o Sistema Operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_ficha(p):
    """Exibe os atributos principais e HP atualizado do jogador."""
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
    """Exibe os itens equipados em cada slot e seus bônus."""
    print("\n" + "🛡️  EQUIPAMENTOS ATUAIS".center(45))
    for slot, item in p.equipamento.items():
        if item:
            status = f"(Atq: +{item.bonus_ataque} | Def: +{item.bonus_defesa})"
            nome_exibir = f"{item.nome} {status}"
        else:
            nome_exibir = "Vazio"
        
        slot_nome = slot.replace("_", " ").capitalize()
        print(f" [{slot_nome}]: {nome_exibir}")
    print("═"*45)

# =================================================================
# 3. MENU DE CRIAÇÃO DE PERSONAGEM
# =================================================================
def menu_criacao():
    """Gerencia a entrada de dados do usuário e retorna o objeto Player."""
    limpar_tela()
    print("=== ⚔️  SISTEMA DE DESPERTAR: REINOS DE PYTHONIA ⚔️  ===")
    nome = input("Qual é seu nome, caro viajante: ")

    # Escolha da Classe
    while True:
        print("\n--- 🛡️  ESCOLHA SUA CLASSE ---")
        for c in CLASSES:
            print(f"[{c}] - {CLASSES[c]['descricao']}")
        
        escolha_c = input("\nDigite o nome da classe: ").strip().capitalize()
        if escolha_c in CLASSES:
            classe_escolhida = escolha_c
            break
        print(f"⚠️ Erro: '{escolha_c}' não existe!")

    # Escolha da Profissão
    while True:
        print("\n--- 🛠️  ESCOLHA SUA PROFISSÃO ---")
        for p in PROFISOES:
            print(f"[{p}] - {PROFISOES[p]['passiva']}")
            
        escolha_p = input("\nDigite o nome da profissão: ").strip().capitalize()
        if escolha_p in PROFISOES:
            profissao_escolhida = escolha_p
            break
        print(f"⚠️ Erro: '{escolha_p}' é inválida!")

    # Retorna o objeto player já configurado
    return player(nome, classe_escolhida, "Vila Inicial", profissao_escolhida)

# =================================================================
# 4. EXECUÇÃO PRINCIPAL (MAIN LOOP)
# =================================================================
if __name__ == "__main__":
    # Passo 1: Iniciar criação
    p1 = menu_criacao()
    limpar_tela()
    
    # Passo 2: Boas-vindas
    print("\n" + "═"*45)
    print(f" ✨ O DESPERTAR COMEÇOU: {p1.nome.upper()} ✨")
    print(f" [SISTEMA]: Você inicia sua jornada em {p1.local_nasc}.")
    print("═"*45)

    # Passo 3: Exibir a Ficha Inicial 
    # (Como você colocou a entrega de itens no Player.py, os bônus já aparecem aqui!)
    exibir_ficha(p1)
    exibir_equipamento(p1)

    # Passo 4: Próximos Passos
    print("\n[SISTEMA]: Seu equipamento inicial foi entregue com base em sua classe.")
    input("\n[ENTER] Para começar a explorar...")
    
    # Futuramente aqui entrará o sistema de DROP e COMBATE
    print(f"\n[SISTEMA]: {p1.nome} entra na floresta em busca de desafios...")