import sys
import os

class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    DIM     = "\033[2m"

# LÓGICA DE AUTÓMATAS (Figura 3.14)

def automata_then(cadena):
    # Basado en la Fig. 3.14 (Estados 12-17)
    # Añadimos un espacio para disparar la transición "otro" (Estado 17)
    temp = cadena + " "
    estado = 12
    for c in temp:
        if estado == 12:
            if c == 't': estado = 13
            else: return False
        elif estado == 13:
            if c == 'h': estado = 14
            else: return False
        elif estado == 14:
            if c == 'e': estado = 15
            else: return False
        elif estado == 15:
            if c == 'n': estado = 16
            else: return False
        elif estado == 16:
            # Si lo que sigue NO es letra/número, acepta (Estado 17)
            if not c.isalnum(): return True
            else: return False
    return False

def automata_id(cadena):
    temp = cadena + " "
    estado = 9
    for c in temp:
        if estado == 9:
            if c.isalpha(): estado = 10
            else: return False
        elif estado == 10:
            # Si encuentra algo que no es letra o número, pasa al estado 11 (Aceptación)
            if not c.isalnum(): return True
    return False

# FLUJO PRINCIPAL

def main():
    # Asegurar compatibilidad de colores en Windows
    if sys.platform == "win32":
        os.system('color')

    print(f"""
{C.BOLD}{C.MAGENTA}╔══════════════════════════════════════════════════════════╗
║      Analizador Léxico — Lenguajes Formales, EAFIT 2026  ║
║      Autómatas Finitos: Fig. 3.14 & 3.15, Dragon Book    ║
╚══════════════════════════════════════════════════════════╝{C.RESET}""")

    while True:
        print(f"{C.BOLD}{'═' * 60}{C.RESET}")
        try:
            cadena = input(f"  {C.BOLD}Ingrese una palabra (o 'salir'): {C.RESET}").strip()
        except EOFError:
            break

        if cadena.lower() == 'salir':
            print(f"\n  {C.CYAN}Saliendo del programa...{C.RESET}")
            break
        
        if not cadena:
            continue

        # Evaluación con prioridad (Palabra Reservada > Identificador)
        if automata_then(cadena):
            print(f"\n  {C.GREEN}{C.BOLD}✔  PALABRA RESERVADA (then){C.RESET}")
        elif automata_id(cadena):
            print(f"\n  {C.YELLOW}{C.BOLD}✔  IDENTIFICADOR{C.RESET}")
        else:
            print(f"\n  {C.RED}{C.BOLD}✘  NO VÁLIDA{C.RESET}")
        print("") # Espacio extra para que no se vea amontonado

if __name__ == "__main__":
    main()
