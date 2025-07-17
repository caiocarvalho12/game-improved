# personagem.py
import random

class Personagem:
    # ... (nenhuma mudança no __init__ e nas propriedades) ...
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):
        self._status = {
            "nome": nome,
            "vida": vida,
            "vida_max": vida,
            "ataque": ataque,
            "defesa": defesa
        }
        self._log_acoes = []

    @property
    def nome(self) -> str:
        return self._status["nome"]

    @property
    def vida(self) -> int:
        return self._status["vida"]

    @property
    def ataque(self) -> int:
        return self._status["ataque"]

    @property
    def defesa(self) -> int:
        return self._status["defesa"]

    def esta_vivo(self) -> bool:
        return self.vida > 0

    # --- MUDANÇA AQUI ---
    def atacar(self, alvo: 'Personagem') -> bool:
        """
        Método de ataque universal.
        Calcula o dano, aplica no alvo e agora RETORNA True se o alvo foi derrotado.
        """
        fator_aleatorio = random.uniform(0.9, 1.1)
        dano_bruto = self.ataque * fator_aleatorio
        dano_efetivo = max(0, dano_bruto - alvo.defesa)
        dano_efetivo = round(dano_efetivo)

        alvo.receber_dano(dano_efetivo)
        
        msg = f"{self.nome} ataca {alvo.nome}, causando {dano_efetivo} de dano!"
        print(msg)
        self.registrar_acao(msg)
        alvo.registrar_acao(f"Recebeu {dano_efetivo} de dano de {self.nome}.")
        
        # Retorna True se o alvo não está mais vivo, False caso contrário.
        return not alvo.esta_vivo()

    def receber_dano(self, dano: int):
        self._status["vida"] = max(0, self.vida - dano)

    # ... (nenhuma outra mudança no resto do arquivo) ...
    def curar(self, quantidade: int):
        vida_maxima = self._status["vida_max"]
        self._status["vida"] = min(vida_maxima, self.vida + quantidade)

    def dialogar(self, frase: str):
        print(f"💬 {self.nome}: “{frase}”")
        self.registrar_acao(f"Disse: “{frase}”")

    def registrar_acao(self, acao: str):
        self._log_acoes.append(acao)

    def exibir_log(self):
        print(f"\n--- Log de Ações de {self.nome} ---")
        for acao in self._log_acoes:
            print(f"- {acao}")
        print("--------------------")

    def exibir_status(self):
        print(f"[{self.nome}] Vida: {self.vida}/{self._status['vida_max']} | Ataque: {self.ataque} | Defesa: {self.defesa}")