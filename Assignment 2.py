class Assigment2:

    def __init__(self):
        # TEORÍA (Enfoque 1): "Install the reserved words in the symbol table initially."
        # Inicializamos la tabla de símbolos con nuestras palabras reservadas.
        self.symbol_table = {
            'if': 'KEYWORD_IF',
            'then': 'KEYWORD_THEN',
            'else': 'KEYWORD_ELSE'
        }
        print("[INIT] Palabras reservadas cargadas en la tabla de símbolos:", self.symbol_table)

    def is_letter(self, char):
        return char.isalpha()

    def is_digit(self, char):
        return char.isdigit()

    def get_token(self, lexeme):
        # TEORÍA: "The function getToken examines the symbol table entry... 
        # returns either 'id' or one of the keyword tokens"
        if lexeme in self.symbol_table:
            return self.symbol_table[lexeme]
        else:
            # Si no es reservada, es un identificador. Lo agregamos a la tabla (installID).
            self.symbol_table[lexeme] = 'id'
            return 'id'

    def scan(self, input_string):
        print(f"\n--- Iniciando escaneo léxico de: '{input_string}' ---")
        tokens = []
        i = 0
        n = len(input_string)

        while i < n:
            char = input_string[i]

            # Omitir espacios en blanco
            if char.isspace():
                i += 1
                continue

            # Simulación del Diagrama de Transición - Figura 3.14
            state = 9
            lexeme = ""
            print(f"\n[ESTADO 9] Analizando nuevo lexema...")

            while i < n:
                char = input_string[i]

                if state == 9:
                    if self.is_letter(char):
                        # Transición de 9 a 10 leyendo una letra
                        state = 10
                        lexeme += char
                        print(f"  ├─ Lee letra '{char}' -> Transición al [ESTADO 10]")
                        i += 1
                    else:
                        # Si no es letra, rompemos (no es ni id ni keyword válido para este autómata)
                        print(f"  ├─ Carácter inválido '{char}' en Estado 9.")
                        i += 1
                        break

                elif state == 10:
                    if self.is_letter(char) or self.is_digit(char):
                        # Bucle en el Estado 10 (letter or digit)
                        lexeme += char
                        print(f"  ├─ Lee '{char}' -> Se mantiene en el [ESTADO 10]")
                        i += 1
                    else:
                        # TEORÍA: Lee "other" (un espacio u otro símbolo). 
                        # Transición al estado 11. El asterisco (*) indica que NO consumimos el carácter.
                        state = 11
                        print(f"  ├─ Lee 'other' (ej. espacio/símbolo) -> Transición al [ESTADO 11]")
                        break 
            
            # Condición de aceptación (llegamos al final de la cadena o al estado 11)
            if state == 10 or state == 11:
                # TEORÍA: "return(getToken(), installID())"
                token_type = self.get_token(lexeme)
                print(f"[ESTADO 11 - ACEPTACIÓN] Lexema encontrado: '{lexeme}'. Tipo de Token: {token_type}")
                tokens.append((lexeme, token_type))

        return tokens

# PRUEBA DEL CÓDIGO 

if __name__ == "__main__":
    scanner = Assigment2()

    codigo_fuente = "if thenextvalue then else"
    
    resultados = scanner.scan(codigo_fuente)
    
    print("\n--- RESULTADO FINAL: LISTA DE TOKENS ---")
    for lexema, tipo in resultados:
        print(f"Lexema: {lexema:<15} | Token: {tipo}")
    
    print("\n--- ESTADO FINAL DE LA TABLA DE SÍMBOLOS ---")
    print(scanner.symbol_table)