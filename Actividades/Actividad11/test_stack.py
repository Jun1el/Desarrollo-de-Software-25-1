from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    """Casos de prueba para la Pila"""

    def setUp(self) -> None:
        """Configuración antes de cada prueba."""
        self.stack = Stack()

    def tearDown(self) -> None:
        """Limpieza después de cada prueba."""
        self.stack = None

    def test_push(self) -> None:
        """Prueba de insertar un elemento en la pila."""
        stack = Stack()
        stack.push(1)
        self.assertEqual(
            stack.peek(), 1,
            "El valor recién agregado debe estar en la parte superior"
        )
        stack.push(2)
        self.assertEqual(
            stack.peek(), 2,
            "Después de otro push, el valor superior debe ser el último agregado"
        )
    def test_push_with_setup(self) -> None:
        """Prueba de insertar elementos usando self.stack."""
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3, "El valor recién agregado debe ser 3")
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5, "El valor recién agregado debe ser 5")
    def test_pop(self) -> None:
        """Prueba de eliminar un elemento de la pila."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(
            stack.pop(), 2,
            "El valor superior (2) debe eliminarse y devolverse"
        )
        self.assertEqual(
            stack.peek(), 1,
            "Después de pop(), el valor superior debe ser 1"
        )
    def test_pop_with_setup(self) -> None:
        """Prueba de eliminar elementos usando self.stack."""
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5, "El valor superior debe ser 5")
        self.assertEqual(self.stack.peek(), 3, "Después de pop(), el valor superior debe ser 3")
        self.stack.pop()
        self.assertTrue(self.stack.is_empty(), "La pila debe estar vacía después de eliminar todos los elementos")

    def test_peek(self) -> None:
        """Prueba de observar el elemento superior de la pila."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(
            stack.peek(), 2,
            "El valor superior debe ser el último agregado (2)"
        )
        self.assertEqual(
            stack.peek(), 2,
            "La pila no debe cambiar después de peek()"
        )
    def test_peek_with_setup(self) -> None:
        """Prueba de observar el elemento superior usando self.stack."""
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5, "El valor superior debe ser 5")

    def test_is_empty(self) -> None:
        """Prueba de si la pila está vacía."""
        stack = Stack()
        self.assertTrue(
            stack.is_empty(),
            "La pila recién creada debe estar vacía"
        )
        stack.push(5)
        self.assertFalse(
            stack.is_empty(),
            "Después de agregar un elemento, la pila no debe estar vacía"
        )