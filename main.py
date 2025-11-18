import antlr4
from PythonGrammarLexer import PythonGrammarLexer
from PythonGrammarParser import PythonGrammarParser
from PythonGrammarVisitor import PythonGrammarVisitor

class Simbolo:
    def __init__(self, nombre, tipo, ambito, valor=None):
        self.nombre = nombre
        self.tipo = tipo
        self.ambito = ambito
        self.valor = valor
        
    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Ámbito: {self.ambito}"

class TablaSimbolos:
    def __init__(self, padre=None):
        self.simbolos = {}
        self.padre = padre
        self.nivel_ambito = 0 if padre is None else padre.nivel_ambito + 1
    
    def agregar_simbolo(self, simbolo):
        self.simbolos[simbolo.nombre] = simbolo
    
    def buscar(self, nombre):
        if nombre in self.simbolos:
            return self.simbolos[nombre]
        elif self.padre:
            return self.padre.buscar(nombre)
        return None
    
    def __str__(self):
        resultado = f"\n=== TABLA DE SÍMBOLOS (Nivel {self.nivel_ambito}) ===\n"
        for nombre, simbolo in self.simbolos.items():
            resultado += f"  {simbolo}\n"
        
        if not self.simbolos:
            resultado += "  (vacía)\n"
            
        return resultado

class CodigoTresDirecciones:
    def __init__(self):
        self.codigo = []
        self.contador_temporales = 0
        self.contador_etiquetas = 0
    
    def nuevo_temporal(self):
        temp = f"t{self.contador_temporales}"
        self.contador_temporales += 1
        return temp
    
    def nueva_etiqueta(self):
        etiqueta = f"L{self.contador_etiquetas}"
        self.contador_etiquetas += 1
        return etiqueta
    
    def emitir(self, operador, arg1=None, arg2=None, resultado=None):
        if arg2 is not None:
            self.codigo.append(f"{resultado} = {arg1} {operador} {arg2}")
        elif arg1 is not None and resultado is not None:
            self.codigo.append(f"{resultado} = {operador} {arg1}")
        elif resultado is not None:
            self.codigo.append(f"{resultado} = {operador}")
        elif arg1 is not None:
            self.codigo.append(f"{operador} {arg1}")
        else:
            self.codigo.append(operador)
    
    def obtener_codigo(self):
        return "\n".join(self.codigo)

class VisitadorPython(PythonGrammarVisitor):
    def __init__(self):
        tabla_simbolos_global = TablaSimbolos()
        self.tabla_simbolos = tabla_simbolos_global
        self.cdt = CodigoTresDirecciones()
        self.ambito_actual = tabla_simbolos_global
        self.ambitos = [tabla_simbolos_global]
    
    def empujar_ambito(self):
        nuevo_ambito = TablaSimbolos(self.ambito_actual)
        self.ambitos.append(nuevo_ambito)
        self.ambito_actual = nuevo_ambito
        return nuevo_ambito
    
    def sacar_ambito(self):
        if len(self.ambitos) > 1:
            ambito_anterior = self.ambitos.pop()
            self.ambito_actual = self.ambitos[-1]
            return ambito_anterior
        return self.ambito_actual
    
    def visitProgram(self, ctx):
        print("\n=== PROCESANDO PROGRAMA ===")
        resultados = []
        for hijo in ctx.getChildren():
            if not isinstance(hijo, antlr4.tree.Tree.TerminalNodeImpl):
                resultado = self.visit(hijo)
                if resultado:
                    resultados.append(resultado)
        return resultados
    
    def visitAssignment(self, ctx):
        nombre_var = ctx.ID().getText()
        resultado_expr = self.visit(ctx.expression())
        
        # Verificar si la variable ya existe
        simbolo_existente = self.ambito_actual.buscar(nombre_var)
        if simbolo_existente:
            tipo_simbolo = simbolo_existente.tipo
        else:
            tipo_simbolo = 'variable'
        
        # Agregar/actualizar en tabla de símbolos
        simbolo = Simbolo(nombre_var, tipo_simbolo, self.ambito_actual.nivel_ambito)
        self.ambito_actual.agregar_simbolo(simbolo)
        
        # Generar código de tres direcciones
        self.cdt.emitir('=', resultado_expr, None, nombre_var)
        print(f"ASIGNACIÓN: {nombre_var} = {resultado_expr}")
        return nombre_var
    
    def visitExpression(self, ctx):
        # Número
        if ctx.NUMBER():
            numero = ctx.NUMBER().getText()
            print(f"EXPRESIÓN: número {numero}")
            return numero
        
        # Identificador (variable)
        elif ctx.ID():
            nombre_var = ctx.ID().getText()
            simbolo = self.ambito_actual.buscar(nombre_var)
            if simbolo:
                print(f"EXPRESIÓN: variable {nombre_var}")
                return nombre_var
            else:
                raise Exception(f"ERROR: Variable no declarada '{nombre_var}'")
        
        # String
        elif ctx.STRING():
            valor_string = ctx.STRING().getText()
            print(f"EXPRESIÓN: string {valor_string}")
            return valor_string
        
        # Expresión entre paréntesis
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expression(0))
        
        # Operación binaria
        else:
            izquierda = self.visit(ctx.expression(0))
            derecha = self.visit(ctx.expression(1))
            operador = ctx.getChild(1).getText()
            
            temp = self.cdt.nuevo_temporal()
            self.cdt.emitir(operador, izquierda, derecha, temp)
            print(f"EXPRESIÓN: {izquierda} {operador} {derecha} -> {temp}")
            return temp
    
    def visitIf_statement(self, ctx):
        print("\n=== PROCESANDO IF ===")
        resultado_condicion = self.visit(ctx.expression(0))
        
        # Crear etiquetas
        etiqueta_sino = self.cdt.nueva_etiqueta()
        etiqueta_fin = self.cdt.nueva_etiqueta()
        
        # Generar código para condición
        self.cdt.emitir('ifFalse', resultado_condicion, None, f"goto {etiqueta_sino}")
        
        # Bloque entonces
        print("\n--- Bloque ENTONCES ---")
        self.empujar_ambito()
        self.visit(ctx.block(0))
        ambito_entonces = self.sacar_ambito()
        print(ambito_entonces)
        
        self.cdt.emitir('goto', None, None, etiqueta_fin)
        
        # Etiqueta sino
        self.cdt.emitir('label', None, None, etiqueta_sino)
        
        # Bloques sino-si y sino
        for i in range(1, len(ctx.block())):
            if i < len(ctx.expression()):
                # sino-si
                print(f"--- Bloque SINO-SI {i} ---")
                condicion_sinoSi = self.visit(ctx.expression(i))
                etiqueta_sinoSi = self.cdt.nueva_etiqueta()
                self.cdt.emitir('ifFalse', condicion_sinoSi, None, f"goto {etiqueta_sinoSi}")
                
                self.empujar_ambito()
                self.visit(ctx.block(i))
                ambito_sinoSi = self.sacar_ambito()
                print(ambito_sinoSi)
                
                self.cdt.emitir('goto', None, None, etiqueta_fin)
                self.cdt.emitir('label', None, None, etiqueta_sinoSi)
            else:
                # sino
                print("--- Bloque SINO ---")
                self.empujar_ambito()
                self.visit(ctx.block(i))
                ambito_sino = self.sacar_ambito()
                print(ambito_sino)
        
        self.cdt.emitir('label', None, None, etiqueta_fin)
        return "if_completado"
    
    def visitWhile_statement(self, ctx):
        print("\n=== PROCESANDO MIENTRAS ===")
        etiqueta_inicio = self.cdt.nueva_etiqueta()
        etiqueta_fin = self.cdt.nueva_etiqueta()
        
        self.cdt.emitir('label', None, None, etiqueta_inicio)
        resultado_condicion = self.visit(ctx.expression())
        self.cdt.emitir('ifFalse', resultado_condicion, None, f"goto {etiqueta_fin}")
        
        print("--- Bloque MIENTRAS ---")
        self.empujar_ambito()
        self.visit(ctx.block())
        ambito_mientras = self.sacar_ambito()
        print(ambito_mientras)
        
        self.cdt.emitir('goto', None, None, etiqueta_inicio)
        self.cdt.emitir('label', None, None, etiqueta_fin)
        return "mientras_completado"
    
    def visitFunction_def(self, ctx):
        nombre_func = ctx.ID().getText()
        print(f"\n=== PROCESANDO FUNCIÓN: {nombre_func} ===")
        
        # Agregar función a la tabla de símbolos global
        simbolo_func = Simbolo(nombre_func, 'función', self.ambito_actual.nivel_ambito)
        self.ambito_actual.agregar_simbolo(simbolo_func)
        
        # Crear nuevo ámbito para la función
        self.empujar_ambito()
        
        # Agregar parámetros a la tabla de símbolos
        if ctx.parameters():
            parametros = self.visit(ctx.parameters())
            for parametro in parametros:
                simbolo = Simbolo(parametro, 'parámetro', self.ambito_actual.nivel_ambito)
                self.ambito_actual.agregar_simbolo(simbolo)
        
        # Generar etiqueta para la función
        self.cdt.emitir('label', None, None, f"func_{nombre_func}")
        
        # Procesar el cuerpo de la función
        self.visit(ctx.block())
        
        # Si no hay retorno explícito dentro del bloque, agregar uno implícito
        hay_retorno = False
        # Un bloque contiene varias sentencias; comprobar si alguna es un retorno
        try:
            for sentencia in ctx.block().statement():
                if hasattr(sentencia, 'return_statement') and sentencia.return_statement() is not None:
                    hay_retorno = True
                    break
        except Exception:
            # En caso de estructuras inesperadas, asumimos que no hay retorno
            hay_retorno = False

        if not hay_retorno:
            self.cdt.emitir('return', None, None, None)
        
        # Mostrar tabla de símbolos de la función y restaurar ámbito
        ambito_func = self.sacar_ambito()
        print(ambito_func)
        
        return nombre_func
    
    def visitParameters(self, ctx):
        parametros = []
        for parametro in ctx.ID():
            parametros.append(parametro.getText())
        print(f"PARÁMETROS: {parametros}")
        return parametros
    
    def visitReturn_statement(self, ctx):
        if ctx.expression():
            valor_retorno = self.visit(ctx.expression())
            self.cdt.emitir('return', valor_retorno, None, None)
            print(f"RETORNO: {valor_retorno}")
        else:
            self.cdt.emitir('return', None, None, None)
            print("RETORNO: None")
        return "retorno"
    
    def visitBlock(self, ctx):
        resultados = []
        for sentencia in ctx.statement():
            resultados.append(self.visit(sentencia))
        return resultados


def compilar_codigo_python(codigo):
    """Función principal para compilar código Python"""
    print("=" * 50)
    print("COMPILADOR PYTHON - ANTLR4")
    print("=" * 50)
    print("CÓDIGO FUENTE:")
    print(codigo)
    print("=" * 50)
    # Eliminar líneas en blanco iniciales y finales que pueden producir errores de parseo
    codigo = codigo.strip('\n')
    
    # Crear el lexer y parser
    flujo_entrada = antlr4.InputStream(codigo)
    lexer = PythonGrammarLexer(flujo_entrada)
    flujo_tokens = antlr4.CommonTokenStream(lexer)
    parser = PythonGrammarParser(flujo_tokens)
    
    # Parsear el código
    arbol = parser.program()
    
    # Visitar el AST
    visitador = VisitadorPython()
    visitador.visit(arbol)
    
    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESULTADOS FINALES")
    print("=" * 50)
    
    print(visitador.tabla_simbolos)
    
    print("\n=== CÓDIGO DE TRES DIRECCIONES ===")
    codigo_cdt = visitador.cdt.obtener_codigo()
    print(codigo_cdt)
    
    return visitador.tabla_simbolos, codigo_cdt

# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Código simple
    with open("ejemplos/test2.py", "r") as archivo: 
        codigo = archivo.read()
        compilar_codigo_python(codigo)   