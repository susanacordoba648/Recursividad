"""Tarea 3: Imprimir patrón de asteriscos con recursividad."""


class Patron:
    @staticmethod
    def _linea(k: int) -> str:
        
        if k <= 0:
            return ""
        
        return "*" + Patron._linea(k - 1)

    @staticmethod
    def imprimir(n: int) -> None:
        
        if n <= 0:
            return
        
        Patron.imprimir(n - 1)
        print(Patron._linea(n))


if __name__ == "__main__":
    Patron.imprimir(3)
