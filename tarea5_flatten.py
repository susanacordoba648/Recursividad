"""Tarea 5: Aplanar (flatten) una lista anidada."""


class ListaPlana:
    @staticmethod
    def flatten(lista: list) -> list:
        
        if not lista:
            return []
        primero, resto = lista[0], lista[1:]
        
        if isinstance(primero, list):
            return ListaPlana.flatten(primero) + ListaPlana.flatten(resto)
        
        return [primero] + ListaPlana.flatten(resto)


if __name__ == "__main__":
    assert ListaPlana.flatten([1, [2, [3, 4], 5]]) == [1, 2, 3, 4, 5]
    assert ListaPlana.flatten([]) == []
    assert ListaPlana.flatten([[], [[]], 1]) == [1]
    print(ListaPlana.flatten([1, [2, [3, 4], 5]]))
    print("Pruebas OK")
