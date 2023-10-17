import unittest


# Classe para representar os nós da árvore
class TreeNode:
  
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


# Classe para representar a árvore
class Tree:
    def __init__(self):
        self.root = None

    # Método para inserir um elemento na árvore
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursively(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursively(current_node.right, value)
    
    # Método para buscar um elemento na árvore
    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursively(current_node.left, value)
        else:
            return self._search_recursively(current_node.right, value)
    
    # Método para realizar uma travessia em ordem na árvore
    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursively(self.root, result)
        return result

    def _in_order_traversal_recursively(self, current_node, result):
        if current_node is not None:
            self._in_order_traversal_recursively(current_node.left, result)
            result.append(current_node.value)
            self._in_order_traversal_recursively(current_node.right, result)
    
    # Método para remover um elemento da árvore
    def remove(self, value):
        self.root = self._remove_recursively(self.root, value)

    def _remove_recursively(self, current_node, value):
        if current_node is None:
            return current_node

        # Caso o valor a ser removido seja menor que o valor atual, procure na subárvore esquerda
        if value < current_node.value:
            current_node.left = self._remove_recursively(current_node.left, value)
        # Caso o valor a ser removido seja maior que o valor atual, procure na subárvore direita
        elif value > current_node.value:
            current_node.right = self._remove_recursively(current_node.right, value)
        # Se o valor a ser removido for igual ao valor atual, este é o nó a ser removido
        else:
            # Caso 1: Nó com apenas um filho ou nenhum filho
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Caso 2: Nó com dois filhos
            # Encontre o nó sucessor (menor valor na subárvore direita)
            current_node.value = self._min_value_node(current_node.right).value
            # Remova o nó sucessor
            current_node.right = self._remove_recursively(current_node.right, current_node.value)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


# Testes unitários para demonstrar a construção da árvore e suas operações
class TestTree(unittest.TestCase):
    def test_insert_and_search(self):
        tree = Tree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(2)
        tree.insert(7)

        # Verificando se os elementos foram inseridos corretamente
        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(2))
        self.assertTrue(tree.search(15))
        self.assertFalse(tree.search(20))

    def test_traversal(self):
        tree = Tree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(2)
        tree.insert(7)

        # Verificando a travessia em ordem
        in_order = tree.in_order_traversal()
        self.assertEqual(in_order, [2, 5, 7, 10, 15])
    
    def test_remove(self):
        tree = Tree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(2)
        tree.insert(7)

        # Removendo elementos e verificando a remoção
        tree.remove(5)
        self.assertFalse(tree.search(5))

        tree.remove(15)
        self.assertFalse(tree.search(15))

if __name__ == '__main__':
    unittest.main()
