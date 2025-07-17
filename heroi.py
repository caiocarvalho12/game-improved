# heroi.py
from personagem import Personagem
import random

class Heroi(Personagem):
    """
    Herói herda de Personagem. Suas ações são controladas pelo jogador.
    """
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        super().__init__(nome, vida, ataque, defesa)
        # O inventário agora é um dicionário, mais flexível para adicionar outros itens.
        self.inventario = {"Poção de Cura": 2}
        self.refens_salvos = 0

    def usar_pocao(self) -> bool:
        """
        Usa uma poção do inventário para curar o herói.
        A cura agora é variável e usa o método curar da classe base.
        """
        if self.inventario.get("Poção de Cura", 0) > 0:
            cura = random.randint(20, 35)
            self.curar(cura)
            self.inventario["Poção de Cura"] -= 1
            msg = f"{self.nome} usou uma Poção e recuperou {cura} de vida!"
            print(msg)
            self.registrar_acao(msg)
            return True
        print("Sem Poções de Cura restantes!")
        return False

    def salvar_refem(self):
        """Incrementa o contador de reféns salvos."""
        self.refens_salvos += 1
        msg = f"{self.nome} salvou um refém! Total: {self.refens_salvos}."
        print(msg)
        self.registrar_acao(msg)

    def exibir_status(self):
        """Sobrescreve o status para mostrar itens e reféns."""
        super().exibir_status()
        pocoes = self.inventario.get('Poção de Cura', 0)
        print(f"   Inventário: {pocoes} Poções | Reféns Salvos: {self.refens_salvos}")