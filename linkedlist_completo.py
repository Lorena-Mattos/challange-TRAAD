#!/usr/bin/python
# -*- coding: utf-8 -*

"""
Para implementar os métodos da classe `LinkedList`, é importante entender o que cada método deve fazer com base na descrição fornecida no exercício.

1. O método `__init__` é responsável por inicializar a lista ligada vazia. Nesse caso, basta definir os atributos `_head` e `_tail` como `None` e o atributo `_len` como 0.

2. O método `__len__` deve retornar o comprimento da lista ligada, ou seja, o número de elementos presentes nela. Nesse caso, basta retornar o valor do atributo `_len`.

3. O método `head` deve retornar o valor do primeiro nó da lista ligada. Para isso, podemos simplesmente retornar o valor do atributo `_head`.

4. O método `tail` deve retornar o valor do último nó da lista ligada. Para isso, podemos retornar o valor do atributo `_tail`.

5. O método `append` deve inserir um novo nó no final da lista ligada com o valor fornecido. Para fazer isso, precisamos criar um novo nó com o valor fornecido e atualizar os ponteiros `_next` para garantir que o último nó aponte para o novo nó inserido. Além disso, também precisamos atualizar o atributo `_tail` para o novo nó inserido e incrementar o valor de `_len`.

6. O método `insert` deve inserir um novo nó no início da lista ligada com o valor fornecido. Isso requer a criação de um novo nó e a atualização dos ponteiros `_next` para garantir que o novo nó aponte para o nó anteriormente no início da lista. Além disso, precisamos atualizar o atributo `_head` para o novo nó inserido e incrementar o valor de `_len`.

7. O método `removeFirst` deve remover o primeiro elemento da lista ligada e retornar o seu valor. Para fazer isso, precisamos atualizar os ponteiros `_next` para garantir que o segundo nó na lista seja o novo primeiro nó. Além disso, precisamos decrementar o valor de `_len` e retornar o valor removido.

8. O método `getValueAt` deve retornar o valor de um nó na posição definida pelo índice. Se o índice for maior do que o tamanho da lista, devemos lançar uma exceção `OutOfBoundsException`. Para fazer isso, precisamos percorrer a lista até o nó na posição especificada pelo índice e retornar o seu valor. Se o índice for maior do que o tamanho da lista, lançamos a exceção `OutOfBoundsException`.

9. O método `toList` deve retornar uma representação em forma de lista ([1, 2, 3, ...]) da lista ligada. Para fazer isso, precisamos percorrer a lista e armazenar os valores dos nós em uma lista Python, que será retornada no final.

Com base nessas informações e no código fornecido, podemos implementar os métodos necessários para que a lista ligada funcione corretamente."""


class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        if self._head is None:
            return None
        return self._head.value

    @property
    def tail(self):
        if self._tail is None:
            return None
        return self._tail.value

    def append(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._len += 1

    def insert(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._len += 1

    def removeFirst(self):
        if self._head is None:
            raise OutOfBoundsException("List is empty")
        value = self._head.value
        if self._head == self._tail:
            self._tail = None
        self._head = self._head.next
        self._len -= 1
        return value

    def getValueAt(self, index):
        if index >= self._len:
            raise OutOfBoundsException("Index out of bounds")
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value

    def toList(self):
        current_node = self._head
        result = []
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return result


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert (ll.head is None)
    assert (ll.tail is None)
    assert (ll.toList() == [])
    ll.append(1)
    assert (ll.head == 1)
    assert (ll.tail == 1)
    assert (len(ll) == 1)
    assert (ll.toList() == [1])
    ll.append(2)
    assert (ll.head == 1)
    assert (ll.tail == 2)
    assert (len(ll) == 2)
    assert (ll.toList() == [1, 2])
    ll.append(3)
    assert (ll.head == 1)
    assert (ll.tail == 3)
    assert (len(ll) == 3)
    assert (ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert (ll.head == 0)
    assert (ll.tail == 3)
    assert (len(ll) == 4)
    assert (ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert (ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert (v == -1)
    assert (ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert (v == 0)
    assert (ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert (v == 1)
    assert (ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert (v == 2)
    assert (ll.toList() == [3])
    v = ll.removeFirst()
    assert (v == 3)
    assert (ll.toList() == [])
    assert (len(ll) == 0)
    print("100%")
