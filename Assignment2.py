def automata_id(input_string):
    state = 9
    lexeme = ""
    i = 0
    
    while i < len(input_string):
        c = input_string[i]
        
        if state == 9:
            if c.isalpha():
                state = 10
                lexeme += c
                i += 1
            else:
                return None
                
        elif state == 10:
            if c.isalnum():
                state = 10
                lexeme += c
                i += 1
            else:
                state = 11
                
        elif state == 11:
            return ("obtenerToken()", "instalarID()")

    if state == 10:
        return ("obtenerToken()", "instalarID()")
        
    return None

def automata_then(input_string):
    state = 12
    i = 0
    
    while i < len(input_string):
        c = input_string[i]
        
        if state == 12:
            if c == 't': 
                state = 13
                i += 1
            else: 
                return None
                
        elif state == 13:
            if c == 'h': 
                state = 14
                i += 1
            else: 
                return None
                
        elif state == 14:
            if c == 'e': 
                state = 15
                i += 1
            else: 
                return None
                
        elif state == 15:
            if c == 'n': 
                state = 16
                i += 1
            else: 
                return None
                
        elif state == 16:
            if not c.isalnum(): 
                state = 17
            else: 
                return None
                
        elif state == 17:
            return True

    if state == 16:
        return True
        
    return None

if __name__ == '__main__':
    print("Testing ID Automaton (States 9-11):")
    print(f"Input 'variable1 ' -> {automata_id('variable1 ')}")
    print(f"Input '9bad' -> {automata_id('9bad')}\n")

    print("Testing 'then' Keyword Automaton (States 12-17):")
    print(f"Input 'then ' -> {automata_then('then ')}")
    print(f"Input 'then1' -> {automata_then('then1')}")
