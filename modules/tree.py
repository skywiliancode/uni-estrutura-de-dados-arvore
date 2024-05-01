def tree(node, level=0, prefix="Root: "):
    # Verifica se o nó não é nulo
    if node is not None:
        # Se o nível for 0, indica que é o nó raiz
        if level == 0:
            # Imprime o valor do nó raiz com o prefixo "Root:"
            print(prefix + str(node.value))
            print()  # Imprime uma linha em branco para separar os nós
        else:
            # Se não for o nó raiz, imprime o valor do nó com uma representação gráfica de sua posição na árvore
            print(" " * (level - 1) * 4 + "|_ " + str(node.value))
        # Verifica se o nó possui filhos (nós à esquerda ou à direita)
        if node.left is not None or node.right is not None:
            # Chama recursivamente a função 'tree' para imprimir os filhos do nó atual
            tree(node.left, level + 1)  # Imprime a subárvore à esquerda
            tree(node.right, level + 1)  # Imprime a subárvore à direita
