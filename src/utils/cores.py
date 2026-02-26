class Cores:
    """Fornece códigos de cores ANSI para formatação do terminal."""

    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    DESTAQUE = '\033[43m\033[30m'
    RESET = '\033[0m'

    @classmethod
    def cor_jogador(cls, jogador: str) -> str:
        """Retorna a cor associada a um jogador."""
        if jogador == 'X':
            return cls.VERMELHO
        elif jogador == 'O':
            return cls.AZUL
        return cls.RESET

    @classmethod
    def remover_cores(cls, texto: str) -> str:
        """Remove todos os códigos ANSI de um texto."""
        import re
        return re.sub(r'\033\[[0-9;]*m', '', texto)
