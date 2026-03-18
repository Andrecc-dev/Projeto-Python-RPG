#arquivo para finalmente dar vida ao RPG
import os
import random
from Player import player
from Classes import CLASSES, PROFISOES

def limpar_tela():
    #essa função vai limpar o termial, super util
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_criacao():
    limpar_tela()
    print("=== ⚔️  SISTEMA DE DESPERTAR: REINOS DE PYTHONIA ⚔️  ===")

    nome = input("Qual é seu nome, caro viajante: ")

    # Inicializamos as variáveis como vazias
    classe_escolhida = ""
    profissao_escolhida = ""

    # --- VALIDAÇÃO DA CLASSE ---
    while True:
        print("\n--- 🛡️  ESCOLHA SUA CLASSE ---")
        for c in CLASSES:
            print(f"[{c}] - {CLASSES[c]['descricao']}")
        
        escolha_c = input("\nDigite o nome da classe: ").strip().capitalize()
        
        if escolha_c in CLASSES:
            classe_escolhida = escolha_c
            break
        else:
            limpar_tela()
            print(f"⚠️ Erro: '{escolha_c}' não existe! Escolha uma das opções da lista.")

    # --- VALIDAÇÃO DA PROFISSÃO ---
    while True:
        print("\n--- 🛠️  ESCOLHA SUA PROFISSÃO ---")
        for p in PROFISOES:
            print(f"[{p}] - {PROFISOES[p]['passiva']}")
            
        escolha_p = input("\nDigite o nome da profissão: ").strip().capitalize()
        
        if escolha_p in PROFISOES:
            profissao_escolhida = escolha_p
            break
        else:
            # Importante: Limpar a tela aqui também ajuda a não poluir o terminal
            limpar_tela() 
            print(f"⚠️ Erro: '{escolha_p}' é inválida! O Sistema não reconhece esse registro.")

    # Agora sim, as duas variáveis COM CERTEZA existem aqui
    heroi = player(nome, classe_escolhida, "Vila Inicial", profissao_escolhida)
    
    return heroi
def exibir_ficha(p):
    limpar_tela()
    print("\n")
    print(f"=== 📜 FICHA DO JOGADOR: {p.nome.upper()} ===")
    print(f"Classe: {p.classe} | Profissão: {p.profissao}")
    print(f"HP: {p.hp_atual:.1f}/{p.hp_max} | Vidas: {p.vidas}")
    print(f"Nível: {p.nivel} | Gold: {p.gold}")
    print("-" * 40)
    print(f"💪 Força: {p.forca}        🎯 Destreza: {p.destreza}")
    print(f"⚡ Agilidade: {p.agilidade}    🧠 Inteligência: {p.inteligencia}")
    print(f"🩸 Vitalidade: {p.vitalidade}   🗣️  Carisma: {p.carisma}")
    print(f"🍀 Sorte: {p.sorte}")
    print("-" * 40)
    print(f"✨ Prodígio: {'SIM (Bônus Ativo)' if p.is_prodigio else 'Não'}")
    print("-" * 40)
    print("\n[Sistema]: Personagem criado com sucesso. O destino o aguarda.")

if __name__ == "__main__":
    p1 = menu_criacao()
    exibir_ficha(p1)