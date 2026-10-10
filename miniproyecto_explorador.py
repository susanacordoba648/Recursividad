
class ExploradorRecursivo:
    @staticmethod
    def imprimir_arbol(sistema: dict, nivel: int = 0) -> None:
        """Muestra la estructura con indentacion segun el nivel."""
        sangria = "    " * nivel
        
        for nombre, contenido in sistema.items():
            if isinstance(contenido, dict):
                print(f"{sangria}[+] {nombre}/")
                ExploradorRecursivo.imprimir_arbol(contenido, nivel + 1)
            else:
                print(f"{sangria}|-- {nombre} ({contenido})")

    @staticmethod
    def buscar_archivo(sistema: dict, nombre: str, ruta: str = ""):
        """Devuelve la ruta del archivo o None si no existe."""
        for clave, contenido in sistema.items():
            ruta_actual = f"{ruta}/{clave}" if ruta else clave
            if isinstance(contenido, dict):
                resultado = ExploradorRecursivo.buscar_archivo(
                    contenido, nombre, ruta_actual)
                if resultado is not None:
                    return resultado
            elif clave == nombre:
                return ruta_actual
        return None

    @staticmethod
    def contar_archivos(sistema: dict) -> int:
        """Cuenta archivos (las carpetas no cuentan)."""
        total = 0
        for contenido in sistema.values():
            if isinstance(contenido, dict):
                total += ExploradorRecursivo.contar_archivos(contenido)
            else:
                total += 1
        return total

if __name__ == "__main__":
    sistema_archivos = {
        "Documentos": {
            "apuntes.txt": "10kb",
            "fotos": {
                "vacaciones.png": "2mb",
                "perro.jpg": "1mb",
            },
        },
        "sistema.dll": "500kb",
    }
    ExploradorRecursivo.imprimir_arbol(sistema_archivos)
    ruta = ExploradorRecursivo.buscar_archivo(sistema_archivos, "perro.jpg")
    assert ruta == "Documentos/fotos/perro.jpg"
    assert ExploradorRecursivo.buscar_archivo(
        sistema_archivos, "sistema.dll") == "sistema.dll"
    assert ExploradorRecursivo.buscar_archivo(
        sistema_archivos, "no_existe.txt") is None
    assert ExploradorRecursivo.contar_archivos(sistema_archivos) == 4
    assert ExploradorRecursivo.contar_archivos({}) == 0
    assert ExploradorRecursivo.contar_archivos({"vacia": {}}) == 0
    print("perro.jpg ->", ruta)
    print("Total de archivos:",
          ExploradorRecursivo.contar_archivos(sistema_archivos))
    print("Pruebas OK")
