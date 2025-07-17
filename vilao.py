# vilao.py
from personagem import Personagem
import random
class Vilao(Personagem):
    """
    Vilão herda de Personagem e tem um nível de maldade que afeta seu ataque.
    """
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int, maldade: str):
        super().__init__(nome, vida, ataque, defesa)
        self.maldade_nivel = {"Baixa": 1.1, "Média": 1.2, "Alta": 1.3}
        if maldade not in self.maldade_nivel:
            raise ValueError(f"Nível de maldade inválido! Use: {list(self.maldade_nivel.keys())}")
        self.maldade = maldade

    def atacar(self, alvo: 'Personagem'):
        """
        Sobrescreve o método atacar para adicionar um multiplicador de dano
        com base no nível de maldade.
        """
        print(f"A maldade de {self.nome} intensifica o ataque!")
        
        # Guardamos o ataque original
        ataque_original = self.ataque
        # Aumentamos o ataque temporariamente
        self._status["ataque"] = round(ataque_original * self.maldade_nivel[self.maldade])
        
        # Chamamos o método atacar da classe pai com o ataque modificado
        super().atacar(alvo)
        
        # Restauramos o ataque original
        self._status["ataque"] = ataque_original

    def provocar(self, heroi: Personagem):
        """Método de diálogo especial para o vilão."""
        frases = [
            f"Sua jornada termina aqui, {heroi.nome}!",
            "Você não é páreo para o meu poder!",
            "Tudo pelo que você luta será destruído!"
        ]
        self.dialogar(random.choice(frases))