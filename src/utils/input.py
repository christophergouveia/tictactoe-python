import keyboard
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
        'up': Tecla.CIMA,
        'down': Tecla.BAIXO,
        'left': Tecla.ESQUERDA,
        'right': Tecla.DIREITA,
    }

    @classmethod
    def ler_tecla(cls) -> Tecla:
        """Lê uma tecla e retorna o mapeamento do jogo."""
        tecla = keyboard.read_event()
        
        if(tecla.event_type == keyboard.KEY_DOWN):
             return Tecla.INVALIDA
         
        if(tecla.name in cls.SETAS_MAPEAMENTO):
            return cls.SETAS_MAPEAMENTO[tecla.name]

        try:
            return cls._mapear_tecla(tecla.name)
        except (UnicodeDecodeError, ValueError, AttributeError):
            return Tecla.INVALIDA

    @classmethod
    def _mapear_tecla(cls, caractere: str) -> Tecla:
        """Mapeia um caractere para uma ação do jogo."""
        mapeamento = {
            'w': Tecla.CIMA,
            's': Tecla.BAIXO,
            'a': Tecla.ESQUERDA,
            'd': Tecla.DIREITA,
            'space': Tecla.MARCAR,
            'r': Tecla.REINICIAR,
            'q': Tecla.SAIR,
        }
        return mapeamento.get(caractere, Tecla.INVALIDA)
