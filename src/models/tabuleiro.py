from enum import Enum
from typing import List, Optional, Tuple


class Jogador(Enum):
    """Representa os jogadores do jogo."""
    X = "X"
    O = "O"


class Tabuleiro:
    """Gerencia o estado e as regras do jogo da velha."""

    def __init__(self, tamanho: int = 3):
        self.tamanho = tamanho
        self.tabuleiro: List[List[Optional[Jogador]]] = [
            [None for _ in range(tamanho)] for _ in range(tamanho)
        ]
        self.jogador_atual = Jogador.X
        self.cursor: Tuple[int, int] = (0, 0)

    def limpar(self) -> None:
        """Reinicia o tabuleiro para o estado inicial."""
        self.tabuleiro = [
            [None for _ in range(self.tamanho)] for _ in range(self.tamanho)
        ]
        self.cursor = (0, 0)
        self.jogador_atual = Jogador.X

    def mover_cursor(self, delta_linha: int, delta_coluna: int) -> None:
        """Move o cursor dentro dos limites do tabuleiro."""
        linha, coluna = self.cursor
        nova_linha = linha + delta_linha
        nova_coluna = coluna + delta_coluna

        if 0 <= nova_linha < self.tamanho:
            self.cursor = (nova_linha, self.cursor[1])

        if 0 <= nova_coluna < self.tamanho:
            self.cursor = (self.cursor[0], nova_coluna)

    def marcar_posicao(self) -> bool:
        """Marca a posição atual. Retorna True se bem-sucedida."""
        linha, coluna = self.cursor
        if self.tabuleiro[linha][coluna] is None:
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogador_atual = Jogador.O if self.jogador_atual == Jogador.X else Jogador.X
            return True
        return False

    def verificar_vitoria(self) -> Optional[Jogador]:
        """Verifica se há um vencedor no tabuleiro."""
        tamanho = self.tamanho

        for linha in range(tamanho):
            if self._tudo_igual(linha, 0, 0, 1):
                return self.tabuleiro[linha][0]

        for coluna in range(tamanho):
            if self._tudo_igual(0, coluna, 1, 0):
                return self.tabuleiro[0][coluna]

        if self._tudo_igual(0, 0, 1, 1):
            return self.tabuleiro[0][0]

        if self._tudo_igual(0, tamanho - 1, 1, -1):
            return self.tabuleiro[0][tamanho - 1]

        return None

    def _tudo_igual(self, linha_inicio: int, col_inicio: int,
                    delta_linha: int, delta_coluna: int) -> bool:
        """Verifica se todas as células em uma direção são iguais e não vazias."""
        primeira = self.tabuleiro[linha_inicio][col_inicio]
        if primeira is None:
            return False

        for i in range(1, self.tamanho):
            linha = linha_inicio + i * delta_linha
            coluna = col_inicio + i * delta_coluna
            if self.tabuleiro[linha][coluna] != primeira:
                return False

        return True

    def verificar_empate(self) -> bool:
        """Verifica se o jogo terminou em empate."""
        if self.verificar_vitoria() is not None:
            return False

        for linha in self.tabuleiro:
            if None in linha:
                return False

        return True

    def posicao_disponivel(self, linha: int, coluna: int) -> bool:
        """Verifica se uma posição está disponível."""
        return self.tabuleiro[linha][coluna] is None

    def get_linha_cursor(self) -> int:
        """Retorna a linha atual do cursor."""
        return self.cursor[0]

    def get_coluna_cursor(self) -> int:
        """Retorna a coluna atual do cursor."""
        return self.cursor[1]
