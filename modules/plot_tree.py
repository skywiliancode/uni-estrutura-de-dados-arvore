# Importa a biblioteca matplotlib para visualização de dados
import matplotlib.pyplot as plt

# Define a cor das linhas que conectam os nós da árvore (preto sólido)
row_color = "k-"
# Define a cor das figuras (círculos representando os nós) na árvore (azul)
figure_color = "b"
text_color = "w"  # Define a cor do texto dentro dos nós da árvore (branco)


def plot_tree(node, posX=0, posY=0, level=0):
    # Desenha um círculo representando o nó atual da árvore
    plt.scatter(posX, posY, s=500, c=figure_color, zorder=3)
    # Adiciona o valor do nó como texto dentro do círculo
    plt.text(posX, posY, str(node.value), fontsize=12,
             ha="center", va="center", color=text_color)

    # Calcula o deslocamento horizontal para os filhos do nó atual
    dx = 1 / (2 ** (level + 1))
    next_level = level + 1  # Incrementa o nível para os filhos do nó atual

    # Desenha uma linha para o filho esquerdo, se existir
    if node.left is not None:
        # Linha conectando o nó atual ao filho esquerdo
        plt.plot([posX, posX - dx], [posY, posY - 1], row_color)
        # Desenha a subárvore esquerda recursivamente
        plot_tree(node.left, posX - dx, posY - 1, next_level)

    # Desenha uma linha para o filho direito, se existir
    if node.right is not None:
        # Linha conectando o nó atual ao filho direito
        plt.plot([posX, posX + dx], [posY, posY - 1], row_color)
        # Desenha a subárvore direita recursivamente
        plot_tree(node.right, posX + dx, posY - 1, next_level)
