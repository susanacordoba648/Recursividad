"""Tarea 4: Caminos en un tablero NxM (solo abajo o derecha)."""


class CaminosTablero:
    @staticmethod
    def contar(filas: int, columnas: int) -> int:
    
        if filas <= 0 or columnas <= 0:
            return 0
        
        if filas == 1 or columnas == 1:
            return 1
        
        return (CaminosTablero.contar(filas - 1, columnas)
                + CaminosTablero.contar(filas, columnas - 1))

    @staticmethod
    def contar_memo(filas: int, columnas: int, memo: dict = None) -> int:
    
        if memo is None:
            memo = {}
        if filas <= 0 or columnas <= 0:
            return 0
        if filas == 1 or columnas == 1:
            return 1
        clave = (filas, columnas)
        if clave in memo:
            return memo[clave]
        memo[clave] = (CaminosTablero.contar_memo(filas - 1, columnas, memo)
                       + CaminosTablero.contar_memo(filas, columnas - 1, memo))
        return memo[clave]
    
if __name__ == "__main__":
    assert CaminosTablero.contar(3, 3) == 6
    assert CaminosTablero.contar(3, 7) == 28
    assert CaminosTablero.contar_memo(3, 7) == 28
    assert CaminosTablero.contar_memo(18, 18) == 2333606220
    print("3x3 =", CaminosTablero.contar(3, 3))
    print("18x18 (memo) =", CaminosTablero.contar_memo(18, 18))
    print("Pruebas OK")
