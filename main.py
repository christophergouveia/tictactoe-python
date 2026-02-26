from src.models import Tabuleiro
from src.utils import LeitorTeclado
from src.ui import Renderizador


class Jogo:
    """Controla o loop principal e a lógica do jogo."""

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.renderizador = Renderizador(self.tabuleiro)
        self.rodando = True

    def processar_tecla(self, tecla) -> None:
        """Processa uma entrada de tecla e executa a ação correspondente."""
        from src.utils.input import Tecla

        if tecla == Tecla.CIMA:
            self.tabuleiro.mover_cursor(-1, 0)
        elif tecla == Tecla.BAIXO:
            self.tabuleiro.mover_cursor(1, 0)
        elif tecla == Tecla.ESQUERDA:
            self.tabuleiro.mover_cursor(0, -1)
        elif tecla == Tecla.DIREITA:
            self.tabuleiro.mover_cursor(0, 1)
        elif tecla == Tecla.MARCAR:
            self.tabuleiro.marcar_posicao()
            self._verificar_estado_jogo()
        elif tecla == Tecla.REINICIAR:
            self.tabuleiro.limpar()
        elif tecla == Tecla.SAIR:
            self.rodando = False

    def _verificar_estado_jogo(self) -> None:
        """Verifica se há vencedor ou empate após uma jogada."""
        vencedor = self.tabuleiro.verificar_vitoria()
        if vencedor:
            self.renderizador.desenhar()
            self.renderizador.mostrar_mensagem(f"🎉 Jogador {vencedor.value} venceu!")
            input("\n    Pressione ENTER para reiniciar o jogo...")
            self.tabuleiro.limpar()
            return

        if self.tabuleiro.verificar_empate():
            self.renderizador.desenhar()
            self.renderizador.mostrar_mensagem("Deu velha!")
            input("\n    Pressione ENTER para reiniciar o jogo...")
            self.tabuleiro.limpar()

    def executar(self) -> None:
        """Inicia o loop principal do jogo."""
        try:
            while self.rodando:
                self.renderizador.desenhar()
                tecla = LeitorTeclado.ler_tecla()
                self.processar_tecla(tecla)
        except KeyboardInterrupt:
            print("\n\n    Jogo interrompido!")
        except Exception as e:
            print(f"\n    Erro: {e}")


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
