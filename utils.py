# utils.py
import time
import os

def linha():
    """Imprime uma linha divisória para organizar a interface."""
    print("-" * 50)

def exibir_titulo(texto: str):
    """Exibe um texto formatado como um título destacado."""
    linha()
    print(f"{texto.center(46)}")
    linha()

def pausar(segundos: float = 1.0):
    """Pausa a execução do programa por um determinado número de segundos."""
    time.sleep(segundos)

def limpar_tela():
    """Limpa o console para uma melhor experiência de usuário entre os turnos."""
    # 'os.name' retorna 'nt' para Windows e 'posix' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')