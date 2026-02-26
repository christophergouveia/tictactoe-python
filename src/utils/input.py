import msvcrt
from enum import Enum


class Tecla(Enum):
    """Mapeamento das teclas do jogo."""
    CIMA = 'w'
    BAIXO = 's'
    ESQUERDA = 'a'
    DIREITA = 'd'
    MARCAR = ' '
    REINICIAR = 'r'
    SAIR = 'q'
    INVALIDA = None


class LeitorTeclado:
    """Lê e interpreta entradas do teclado no Windows."""

    SETAS_MAPEAMENTO = {
        b'H': Tecla.CIMA,
        b'P': Tecla.BAIXO,
        b'K': Tecla.ESQUERDA,
        b'M': Tecla.DIREITA,
    }

    @classmethod
    def ler_tecla(cls) -> Tecla:
        """Lê uma tecla e retorna o mapeamento do jogo."""
        tecla = msvcrt.getch()

        if tecla == b'\xe0':
            tecla = msvcrt.getch()
            return cls.SETAS_MAPEAMENTO.get(tecla, Tecla.INVALIDA)

        try:
            caractere = tecla.decode('latin-1').lower()
            return cls._mapear_tecla(caractere)
        except (UnicodeDecodeError, ValueError):
            return Tecla.INVALIDA

    @classmethod
    def _mapear_tecla(cls, caractere: str) -> Tecla:
        """Mapeia um caractere para uma ação do jogo."""
        mapeamento = {
            'w': Tecla.CIMA,
            's': Tecla.BAIXO,
            'a': Tecla.ESQUERDA,
            'd': Tecla.DIREITA,
            ' ': Tecla.MARCAR,
            'r': Tecla.REINICIAR,
            'q': Tecla.SAIR,
        }
        return mapeamento.get(caractere, Tecla.INVALIDA)
