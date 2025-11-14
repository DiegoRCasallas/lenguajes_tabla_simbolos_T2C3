import antlr4
from PythonGrammarLexer import PythonGrammarLexer
from PythonGrammarParser import PythonGrammarParser
from PythonGrammarVisitor import PythonGrammarVisitor

class Symbol:
    def __init__(self, name, type, scope, value=None):
        self.name = name
        self.type = type
        self.scope = scope
        self.value = value
        
    def __str__(self):
        return f"{self.name} ({self.type}) - Scope: {self.scope}"

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        self.scope_level = 0 if parent is None else parent.scope_level + 1
    
    def add_symbol(self, symbol):
        self.symbols[symbol.name] = symbol
    
    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        return None
    
    def __str__(self):
        result = f"\n=== TABLA DE SÍMBOLOS (Nivel {self.scope_level}) ===\n"
        for name, symbol in self.symbols.items():
            result += f"  {symbol}\n"
        
        if not self.symbols:
            result += "  (vacía)\n"
            
        return result

class ThreeAddressCode:
    def __init__(self):
        self.code = []
        self.temp_counter = 0
        self.label_counter = 0
    
    def new_temp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp
    
    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label
    
    def emit(self, op, arg1=None, arg2=None, result=None):
        if arg2 is not None:
            self.code.append(f"{result} = {arg1} {op} {arg2}")
        elif arg1 is not None and result is not None:
            self.code.append(f"{result} = {op} {arg1}")
        elif result is not None:
            self.code.append(f"{result} = {op}")
        elif arg1 is not None:
            self.code.append(f"{op} {arg1}")
        else:
            self.code.append(op)
    
    def get_code(self):
        return "\n".join(self.code)

class PythonVisitor(PythonGrammarVisitor):
    def __init__(self):
        global_symbol_table = SymbolTable()
        self.symbol_table = global_symbol_table
        self.tac = ThreeAddressCode()
        self.current_scope = global_symbol_table
        self.scopes = [global_symbol_table]
    
    def push_scope(self):
        new_scope = SymbolTable(self.current_scope)
        self.scopes.append(new_scope)
        self.current_scope = new_scope
        return new_scope
    
    def pop_scope(self):
        if len(self.scopes) > 1:
            old_scope = self.scopes.pop()
            self.current_scope = self.scopes[-1]
            return old_scope
        return self.current_scope
    
    def visitProgram(self, ctx):
        print("\n=== PROCESANDO PROGRAMA ===")
        results = []
        for child in ctx.getChildren():
            if not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
                result = self.visit(child)
                if result:
                    results.append(result)
        return results
    
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        expr_result = self.visit(ctx.expression())
        
        # Verificar si la variable ya existe
        existing_symbol = self.current_scope.lookup(var_name)
        if existing_symbol:
            symbol_type = existing_symbol.type
        else:
            symbol_type = 'variable'
        
        # Agregar/actualizar en tabla de símbolos
        symbol = Symbol(var_name, symbol_type, self.current_scope.scope_level)
        self.current_scope.add_symbol(symbol)
        
        # Generar código de tres direcciones
        self.tac.emit('=', expr_result, None, var_name)
        print(f"ASIGNACIÓN: {var_name} = {expr_result}")
        return var_name
    
    def visitExpression(self, ctx):
        # Número
        if ctx.NUMBER():
            num = ctx.NUMBER().getText()
            print(f"EXPRESIÓN: número {num}")
            return num
        
        # Identificador (variable)
        elif ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self.current_scope.lookup(var_name)
            if symbol:
                print(f"EXPRESIÓN: variable {var_name}")
                return var_name
            else:
                raise Exception(f"ERROR: Variable no declarada '{var_name}'")
        
        # String
        elif ctx.STRING():
            string_val = ctx.STRING().getText()
            print(f"EXPRESIÓN: string {string_val}")
            return string_val
        
        # Expresión entre paréntesis
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expression(0))
        
        # Operación binaria
        else:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = ctx.getChild(1).getText()
            
            temp = self.tac.new_temp()
            self.tac.emit(op, left, right, temp)
            print(f"EXPRESIÓN: {left} {op} {right} -> {temp}")
            return temp
    
    def visitIf_statement(self, ctx):
        print("\n=== PROCESANDO IF ===")
        condition_result = self.visit(ctx.expression(0))
        
        # Crear etiquetas
        else_label = self.tac.new_label()
        end_label = self.tac.new_label()
        
        # Generar código para condición
        self.tac.emit('ifFalse', condition_result, None, f"goto {else_label}")
        
        # Bloque then
        print("\n--- Bloque THEN ---")
        self.push_scope()
        self.visit(ctx.block(0))
        then_scope = self.pop_scope()
        print(then_scope)
        
        self.tac.emit('goto', None, None, end_label)
        
        # Etiqueta else
        self.tac.emit('label', None, None, else_label)
        
        # Bloques elif y else
        for i in range(1, len(ctx.block())):
            if i < len(ctx.expression()):
                # elif
                print(f"--- Bloque ELIF {i} ---")
                elif_condition = self.visit(ctx.expression(i))
                elif_label = self.tac.new_label()
                self.tac.emit('ifFalse', elif_condition, None, f"goto {elif_label}")
                
                self.push_scope()
                self.visit(ctx.block(i))
                elif_scope = self.pop_scope()
                print(elif_scope)
                
                self.tac.emit('goto', None, None, end_label)
                self.tac.emit('label', None, None, elif_label)
            else:
                # else
                print("--- Bloque ELSE ---")
                self.push_scope()
                self.visit(ctx.block(i))
                else_scope = self.pop_scope()
                print(else_scope)
        
        self.tac.emit('label', None, None, end_label)
        return "if_completed"
    
    def visitWhile_statement(self, ctx):
        print("\n=== PROCESANDO WHILE ===")
        start_label = self.tac.new_label()
        end_label = self.tac.new_label()
        
        self.tac.emit('label', None, None, start_label)
        condition_result = self.visit(ctx.expression())
        self.tac.emit('ifFalse', condition_result, None, f"goto {end_label}")
        
        print("--- Bloque WHILE ---")
        self.push_scope()
        self.visit(ctx.block())
        while_scope = self.pop_scope()
        print(while_scope)
        
        self.tac.emit('goto', None, None, start_label)
        self.tac.emit('label', None, None, end_label)
        return "while_completed"
    
    def visitFunction_def(self, ctx):
        func_name = ctx.ID().getText()
        print(f"\n=== PROCESANDO FUNCIÓN: {func_name} ===")
        
        # Agregar función a la tabla de símbolos global
        func_symbol = Symbol(func_name, 'function', self.current_scope.scope_level)
        self.current_scope.add_symbol(func_symbol)
        
        # Crear nuevo scope para la función
        self.push_scope()
        
        # Agregar parámetros a la tabla de símbolos
        if ctx.parameters():
            params = self.visit(ctx.parameters())
            for param in params:
                symbol = Symbol(param, 'parameter', self.current_scope.scope_level)
                self.current_scope.add_symbol(symbol)
        
        # Generar etiqueta para la función
        self.tac.emit('label', None, None, f"func_{func_name}")
        
        # Procesar el cuerpo de la función
        self.visit(ctx.block())
        
        # Si no hay return explícito dentro del bloque, agregar uno implícito
        has_return = False
        # Un bloque contiene varias sentencias; comprobar si alguna es un return
        try:
            for stmt in ctx.block().statement():
                if hasattr(stmt, 'return_statement') and stmt.return_statement() is not None:
                    has_return = True
                    break
        except Exception:
            # En caso de estructuras inesperadas, asumimos que no hay return
            has_return = False

        if not has_return:
            self.tac.emit('return', None, None, None)
        
        # Mostrar tabla de símbolos de la función y restaurar scope
        func_scope = self.pop_scope()
        print(func_scope)
        
        return func_name
    
    def visitParameters(self, ctx):
        params = []
        for param in ctx.ID():
            params.append(param.getText())
        print(f"PARÁMETROS: {params}")
        return params
    
    def visitReturn_statement(self, ctx):
        if ctx.expression():
            return_value = self.visit(ctx.expression())
            self.tac.emit('return', return_value, None, None)
            print(f"RETURN: {return_value}")
        else:
            self.tac.emit('return', None, None, None)
            print("RETURN: None")
        return "return"
    
    def visitBlock(self, ctx):
        results = []
        for stmt in ctx.statement():
            results.append(self.visit(stmt))
        return results


def compile_python_code(code):
    """Función principal para compilar código Python"""
    print("=" * 50)
    print("COMPILADOR PYTHON - ANTLR4")
    print("=" * 50)
    print("CÓDIGO FUENTE:")
    print(code)
    print("=" * 50)
    # Eliminar líneas en blanco iniciales y finales que pueden producir errores de parseo
    code = code.strip('\n')
    
    # Crear el lexer y parser
    input_stream = antlr4.InputStream(code)
    lexer = PythonGrammarLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = PythonGrammarParser(token_stream)
    
    # Parsear el código
    tree = parser.program()
    
    # Visitar el AST
    visitor = PythonVisitor()
    visitor.visit(tree)
    
    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESULTADOS FINALES")
    print("=" * 50)
    
    print(visitor.symbol_table)
    
    print("\n=== CÓDIGO DE TRES DIRECCIONES ===")
    tac_code = visitor.tac.get_code()
    print(tac_code)
    
    return visitor.symbol_table, tac_code

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Código simple
    with open("ejemplos/test2.py", "r") as file: 
        code = file.read()
        compile_python_code(code)   