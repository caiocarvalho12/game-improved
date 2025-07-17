# main.py
# (nenhuma mudança nas importações)
from heroi import Heroi
from vilao import Vilao
from utils import exibir_titulo, linha, pausar
import random

# --- MUDANÇA DE LÓGICA AQUI ---
def turno_herois(herois: list[Heroi], viloes: list[Vilao]):
    """Função reestruturada para um fluxo de ação mais lógico."""
    for heroi in herois:
        if heroi.esta_vivo():
            linha()
            print(f"Turno de {heroi.nome}:")
            heroi.exibir_status()
            
            # 1. PERGUNTA A AÇÃO PRIMEIRO
            escolha = input("\nEscolha sua ação: [1] Atacar [2] Usar Poção [3] Salvar Refém\n> ")

            # 2. SE A AÇÃO FOR ATACAR, AGORA SIM PEDE O ALVO
            if escolha == "1":
                viloes_vivos = [v for v in viloes if v.esta_vivo()]
                if not viloes_vivos:
                    print("Não há mais vilões para atacar!")
                    break
                
                alvo = viloes_vivos[0]
                if len(viloes_vivos) > 1:
                    print("Escolha seu alvo:")
                    for i, v in enumerate(viloes_vivos):
                        print(f"[{i+1}] {v.nome}")
                    while True:
                        try:
                            escolha_alvo = int(input("> ")) - 1
                            if 0 <= escolha_alvo < len(viloes_vivos):
                                alvo = viloes_vivos[escolha_alvo]
                                break
                            else: 
                                print("Alvo inválido.")
                        except ValueError: 
                            print("Entrada inválida.")
                
                # Executa o ataque e dá o feedback
                alvo_derrotado = heroi.atacar(alvo)
                pausar(0.5)

                if alvo_derrotado:
                    print(f"💥 {alvo.nome} foi derrotado! 💥")
                else:
                    alvo.exibir_status()

            # 3. AÇÕES SEM ALVO SÃO TRATADAS DIRETAMENTE
            elif escolha == "2":
                heroi.usar_pocao()

            elif escolha == "3":
                heroi.salvar_refem()
                
            else:
                print("Opção inválida, você hesitou e perdeu o turno!")
                heroi.registrar_acao("Hesitou e perdeu o turno.")
            
            pausar()

# (Nenhuma mudança necessária na função turno_viloes ou no resto do arquivo)
def turno_viloes(viloes: list[Vilao], herois: list[Heroi]):
    for vilao in viloes:
        if vilao.esta_vivo():
            linha()
            print(f"Turno de {vilao.nome}:")
            
            herois_vivos = [h for h in herois if h.esta_vivo()]
            if not herois_vivos: break
                
            alvo = random.choice(herois_vivos)
            
            if random.random() < 0.4:
                vilao.provocar(alvo)
            else:
                alvo_derrotado = vilao.atacar(alvo)
                pausar(0.5)

                if alvo_derrotado:
                    print(f"💀 {alvo.nome} foi derrotado! 💀")
                else:
                    alvo.exibir_status()
            pausar()


def main():
    exibir_titulo("🕹️ Batalha Épica em Python POO 🕹️")

    herois = [Heroi(nome="Aragorn", vida=120, ataque=18, defesa=10)]
    viloes = [Vilao(nome="Lurtz", vida=90, ataque=15, defesa=5, maldade="Média"),
              Vilao(nome="Orque Batedor", vida=50, ataque=12, defesa=3, maldade="Baixa")]

    print("--- EQUIPE DE HERÓIS ---")
    for h in herois: h.exibir_status()
    print("\n--- HORDA DE VILÕES ---")
    for v in viloes: v.exibir_status()
    
    pausar(2)

    herois[0].dialogar("Pelos Povos Livres da Terra-média, vocês não passarão!")
    viloes[0].dialogar("O mundo dos homens vai queimar!")
    pausar(2)

    while any(h.esta_vivo() for h in herois) and any(v.esta_vivo() for v in viloes):
        turno_herois(herois, viloes)
        
        if not any(v.esta_vivo() for v in viloes):
            break
            
        turno_viloes(viloes, herois)

    linha()
    if any(h.esta_vivo() for h in herois):
        exibir_titulo("🏆 VITÓRIA DOS HERÓIS! 🏆")
    else:
        exibir_titulo("💀 OS VILÕES TRIUNFARAM... 💀")
    linha()

    print("\n📜 Histórico da Batalha:")
    for heroi in herois:
        heroi.exibir_log()
    for vilao in viloes:
        vilao.exibir_log()


if __name__ == "__main__":
    main()