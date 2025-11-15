## Proyecto: Analizador/Compilador simple con ANTLR4 (Python)
##AUTOR: DIEGO CASALLAS

Este repositorio contiene un ejemplo de un compilador/analizador sencillo para un subconjunto de la sintaxis estilo Python, construido con ANTLR4 y una visita del árbol (visitor) que construye una tabla de símbolos y genera código de tres direcciones (Three Address Code - TAC).

El README explica en detalle la finalidad del proyecto, la estructura de archivos, dependencias, pasos para levantar el proyecto, cómo regenerar los artefactos de ANTLR y cómo ejecutar los ejemplos incluidos.

## Contenido y propósito

- `PythonGrammar.g4`: Gramática ANTLR4 que define la sintaxis del lenguaje (subconjunto estilo Python).
- `PythonGrammarLexer.py`, `PythonGrammarParser.py`, `PythonGrammarVisitor.py`, `PythonGrammarListener.py`: Archivos generados por ANTLR (ya presentes en el repositorio).
- `main.py`: Programa principal que crea el lexer/parser, recorre el AST con `PythonVisitor`, construye la tabla de símbolos y genera código de tres direcciones.
- `ejemplos/`: carpeta con ejemplos de código fuente que se pueden procesar. Ej.: `ejemplos/test2.py`.
- `antlr-4.13.2-complete.jar`: binario de ANTLR incluido para regenerar los analizadores si hace falta.
- `requirements.txt`: dependencias de Python necesarias (runtime de ANTLR para Python).

## Características

- Parseo de un subconjunto de sentencias: asignaciones, expresiones aritméticas y booleanas, `if`/`elif`/`else`, `while`, definición de funciones y `return`.
- Construcción de una tabla de símbolos por ámbitos (scopes), con soporte básico de búsqueda en ámbitos anidados.
- Generación simple de código de tres direcciones (TAC) con temporales y etiquetas.

## Requisitos

- Python 3.8+ (probado con Python 3.x)
- Java Runtime (para ejecutar el JAR de ANTLR si desea regenerar los archivos).

Las dependencias de Python están en `requirements.txt`. Actualmente contiene:

```
antlr4-python3-runtime==4.13.2
```

## Instalación rápida

Recomendada: usar un entorno virtual.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar el proyecto

El `main.py` está diseñado para leer el archivo `ejemplos/test2.py` y ejecutar el flujo: lexer -> parser -> visitor -> mostrar tabla de símbolos y TAC.

Para ejecutar:

```bash
python3 main.py
```

Salida esperada: el programa imprimirá mensajes de procesamiento, la(s) tabla(s) de símbolos y el código de tres direcciones generado.

Si desea procesar otro archivo de ejemplo, edite la última sección de `main.py` (donde se abre `ejemplos/test2.py`) o cargue el contenido del archivo con `compile_python_code(code)` desde un REPL.

## Regenerar los archivos de ANTLR (lexer, parser, visitor/listener)

Si modifica `PythonGrammar.g4` y quiere regenerar los artefactos para Python3, ejecute (desde la raíz del proyecto):

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 PythonGrammar.g4
```

Notas:
- El comando generará varios archivos `.py` (lexer, parser, listener, visitor). Coloque o deje esos archivos en la raíz del proyecto para que `main.py` pueda importarlos.
- Dependiendo de la versión de ANTLR y la forma de manejo de INDENT/DEDENT, puede requerirse un preprocesado o adaptaciones en la gramática/listener para manejar correctamente indentación significante (el ejemplo incluye tokens `INDENT` y `DEDENT` con manejo simplificado).

## Estructura de carpetas (resumen)

- `.`
  - `main.py` — Entrada principal y ejemplo de uso.
  - `PythonGrammar.g4` — Gramática ANTLR4.
  - `PythonGrammar*.py` — Archivos generados por ANTLR.
  - `antlr-4.13.2-complete.jar` — JAR de ANTLR incluido para regenerar artefactos.
  - `requirements.txt` — Dependencias de Python.
  - `ejemplos/` — Ejemplos de código a analizar (p. ej. `test2.py`).

## Qué hace `main.py` (resumen técnico)

- Crea un `InputStream` con el código fuente.
- Ejecuta el `PythonGrammarLexer` y `PythonGrammarParser` para obtener el árbol `program()`.
- Usa `PythonVisitor` (implementado en `main.py`) para:
  - Mantener una `SymbolTable` por scope (padre/hijo).
  - Agregar símbolos (variables, funciones, parámetros) durante el recorrido.
  - Generar instrucciones de TAC usando una clase `ThreeAddressCode` (temporales, etiquetas, `emit`).
- Imprime la tabla de símbolos global y el código TAC al finalizar.

## Limitaciones y notas importantes

- La gramática y el visitor implementan un subconjunto educativo de Python: no cubre todas las construcciones del lenguaje real.
- El manejo de `INDENT`/`DEDENT` está simplificado; la gramática actual tiene un token `DEDENT` vaciado (comentado) y puede necesitar un preprocesador/handle específico para casos complejos de indentación en Python real.
- Error handling: el visitor actualmente lanza excepciones en variables no declaradas o cuando encuentra construcciones no esperadas. Es intencional para propósitos didácticos.

## Ejemplo rápido

Contenido de `ejemplos/test2.py` (incluido en el repo):

```python
a = 1
b = 2
c = 3
if a < b:
    x = a + b
    if x < 10:
        x=x+10
else:
    x = c * 10
```

Si ejecuta `python3 main.py` verá impresiones que muestran el procesamiento y el TAC resultante.

## Extensiones sugeridas (fácilmente implementables)

- Añadir CLI a `main.py` para pasar archivo de entrada y opciones (mostrar AST, imprimir solo tabla de símbolos, etc.).
- Añadir manejo más robusto de errores de sintaxis/semántica y mensajes amigables.
- Implementar generación de código más completa o backend simple para traducir TAC a instrucciones de una máquina virtual.

## Contribuir

1. Haga fork del repositorio.
2. Cree una rama feature/bugfix.
3. Envíe un pull request con descripción clara.

## Licencia

Incluya aquí la licencia deseada (por ejemplo MIT). Actualmente no se añade un archivo `LICENSE` en el repo por defecto.

## Contacto

Si tiene preguntas o quiere colaborar, abra un issue o contacte al mantenedor del repositorio.

---

README generado automáticamente — explica la estructura y uso del proyecto. Si quiere que adapte el README con información adicional (por ejemplo, añadir un `Makefile`, pruebas unitarias o un README en inglés), dígame qué prefiere y lo implemento.
