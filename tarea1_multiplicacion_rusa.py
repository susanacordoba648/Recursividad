"""Tarea 1: Multiplicacion rusa recursiva (sin operador *)."""


class MultiplicacionRusa:
    @staticmethod
    def multiplicar(a: int, b: int) -> int:
        
        if b < 0:
            return -MultiplicacionRusa.multiplicar(a, -b)
        if b == 0:
            return 0

        mitad = MultiplicacionRusa.multiplicar(a + a, b // 2)
        if b % 2 == 0:
            return mitad
        return a + mitad


if __name__ == "__main__":
    assert MultiplicacionRusa.multiplicar(6, 7) == 42
    assert MultiplicacionRusa.multiplicar(0, 9) == 0
    assert MultiplicacionRusa.multiplicar(13, 0) == 0
    assert MultiplicacionRusa.multiplicar(-4, 5) == -20
    assert MultiplicacionRusa.multiplicar(4, -5) == -20
    assert MultiplicacionRusa.multiplicar(-4, -5) == 20
    print("6 x 7 =", MultiplicacionRusa.multiplicar(6, 7))
    print("Pruebas OK")
