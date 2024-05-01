from modules.node import Node  # Importa a classe Node do módulo 'node'
# Importa a biblioteca matplotlib para visualização de dados
import matplotlib.pyplot as plt
# Importa a função plot_tree do módulo 'plot_tree'
from modules.plot_tree import plot_tree

# Criação da árvore binária com valores para os nós
root = Node(10)
root.left = Node(20)
root.left.left = Node(12)
root.left.left.left = Node(15)
root.left.left.right = Node(11)
root.left.right = Node(8)
root.right = Node(12)
root.right.left = Node(5)
root.right.right = Node(7)

# Define o tamanho da figura para a visualização da árvore
plt.figure(figsize=(9, 5))
plt.axis("off")  # Remove os eixos da visualização
plot_tree(root)  # Chama a função plot_tree para desenhar a árvore binária
plt.show()  # Exibe a visualização da árvore
