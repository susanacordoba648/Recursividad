"""Tarea 2: Conteo de vocales recursivo."""


class ContadorVocales:

    @staticmethod
    def contar(texto: str) -> int:
    
        if texto == "":
            return 0
        
        es_vocal = 1 if texto[0] in ContadorVocales.VOCALES else 0
        return es_vocal + ContadorVocales.contar(texto[1:])


if __name__ == "__main__":
    assert ContadorVocales.contar("") == 0
    assert ContadorVocales.contar("Recursividad") == 5
    assert ContadorVocales.contar("Murciélago") == 5
    assert ContadorVocales.contar("xyz") == 0
    print("Recursividad ->", ContadorVocales.contar("Recursividad"))
    print("Pruebas OK")
