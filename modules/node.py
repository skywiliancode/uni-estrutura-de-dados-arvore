class Node:
    # Define a classe Node, que representa um nó em uma árvore binária

    def __init__(self, value):
        # Método especial __init__ é chamado quando um novo objeto Node é criado
        # 'value' é o valor que o nó irá armazenar

        # Define o valor do nó como o valor passado como argumento
        self.value = value

        # Inicializa os ponteiros para os filhos do nó como None, indicando que inicialmente não tem filhos
        self.left = None  # Ponteiro para o filho à esquerda
        self.right = None  # Ponteiro para o filho à direita
