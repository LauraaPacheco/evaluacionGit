"""Algoritmo básico de ordenamiento: método burbuja (bubble sort)."""


def ordenamiento_burbuja(lista):
    """Devuelve una copia de la lista ordenada de menor a mayor."""
    datos = list(lista)
    n = len(datos)
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return datos


if __name__ == "__main__":
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", numeros)
    print("Lista ordenada:", ordenamiento_burbuja(numeros))

    assert ordenamiento_burbuja([]) == []
    assert ordenamiento_burbuja([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert ordenamiento_burbuja([3, 3, 1]) == [1, 3, 3]
    print("Todas las pruebas pasaron.")
