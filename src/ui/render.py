import subprocess
from ..models.tabuleiro import Tabuleiro, Jogador
from ..utils.cores import Cores


class Renderizador:
    """Responsável por desenhar o tabuleiro e interface no terminal."""

    BORDA_SUPERIOR = "┌───┐"
    BORDA_INFERIOR = "└───┘"
    LATERAL = "│"
    VAZIO = "   "

    BORDA_SUPERIOR_DESTAQUE = "╔═══╗"
    BORDA_INFERIOR_DESTAQUE = "╚═══╝"

    TITULO = "╔══════════════════════════════╗\n    ║      JOGO DA VELHA           ║\n    ╚══════════════════════════════╝"
    CONTROLES = (
        "\n┌────────────────────────────────┐\n"
        "│  WASD ou Setas: Mover          │\n"
        "│  ESPACO: Marcar                │\n"
        "│  R: Reiniciar  Q: Sair         │\n"
        "└────────────────────────────────┘"
    )

    def __init__(self, tabuleiro: Tabuleiro):
        self.tabuleiro = tabuleiro

    def limpar_tela(self) -> None:
        """Limpa a tela do terminal."""
        subprocess.run("cls", shell=True)

    def desenhar(self) -> None:
        """Renderiza o tabuleiro completo com interface."""
        self.limpar_tela()

        print()
        print(f"    {self.TITULO}")
        print()

        tamanho = self.tabuleiro.tamanho
        linha_cursor = self.tabuleiro.get_linha_cursor()
        coluna_cursor = self.tabuleiro.get_coluna_cursor()

        for i in range(tamanho):
            self._imprimir_linha_borda(i, linha_cursor, coluna_cursor, superior=True)
            self._imprimir_linha_conteudo(i, linha_cursor, coluna_cursor)
            self._imprimir_linha_borda(i, linha_cursor, coluna_cursor, superior=False)

        print()
        self._imprimir_info_jogador()
        print()
        print(f"    {self.CONTROLES}")

    def _imprimir_linha_borda(self, linha: int, linha_cursor: int,
                               coluna_cursor: int, superior: bool) -> None:
        """Imprime uma linha de bordas do tabuleiro."""
        print("    ", end="")

        for j in range(self.tabuleiro.tamanho):
            com_cursor = (linha == linha_cursor and j == coluna_cursor)

            if superior:
                borda = self.BORDA_SUPERIOR_DESTAQUE if com_cursor else self.BORDA_SUPERIOR
            else:
                borda = self.BORDA_INFERIOR_DESTAQUE if com_cursor else self.BORDA_INFERIOR

            print(borda, end="")

        print()

    def _imprimir_linha_conteudo(self, linha: int, linha_cursor: int,
                                  coluna_cursor: int) -> None:
        """Imprime o conteúdo de uma linha do tabuleiro."""
        print("    ", end="")

        for j in range(self.tabuleiro.tamanho):
            com_cursor = (linha == linha_cursor and j == coluna_cursor)
            celula = self.tabuleiro.tabuleiro[linha][j]

            print(self.LATERAL, end="")

            if com_cursor:
                print(Cores.DESTAQUE, end="")
                conteudo = self._formatar_celula(celula, destacar=True)
            else:
                conteudo = self._formatar_celula(celula, destacar=False)

            print(conteudo, end="")
            print(f"{Cores.RESET}{self.LATERAL}", end="")

        print()

    def _formatar_celula(self, jogador: Jogador | None, destacar: bool) -> str:
        """Formata o conteúdo de uma célula com cores apropriadas."""
        if jogador is None:
            if destacar:
                return f" {self.tabuleiro.jogador_atual.value} "
            return self.VAZIO

        cor = Cores.cor_jogador(jogador.value)
        return f"{cor} {jogador.value} {Cores.RESET}"

    def _imprimir_info_jogador(self) -> None:
        """Imprime informações sobre o jogador atual."""
        jogador_atual = self.tabuleiro.jogador_atual.value
        cor_x = Cores.cor_jogador('X')
        cor_o = Cores.cor_jogador('O')
        cor_atual = Cores.cor_jogador(jogador_atual)

        print(f"    Jogador: {cor_x}X{Cores.RESET} ou {cor_o}O{Cores.RESET} | "
              f"Atual: {cor_atual}{jogador_atual}{Cores.RESET}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        """Exibe uma mensagem centralizada."""
        print()
        print(f"    {mensagem}")
