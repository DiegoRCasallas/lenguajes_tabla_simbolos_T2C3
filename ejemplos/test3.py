from typing import List, Iterable, Any, Optional
import math
import argparse
import sys
from collections import Counter

#!/usr/bin/env python3
"""
Archivo: test3.py
Descripción: Conjunto de funciones básicas (aritmética, listas, archivos, etc.)
Uso:
    Ejecutar directamente para ver ejemplos:
        python test3.py
"""



# ---------------------------
# Operaciones aritméticas
# ---------------------------
def add(a: float, b: float) -> float:
    """Suma a + b"""
    return a + b


def sub(a: float, b: float) -> float:
    """Resta a - b"""
    return a - b


def mul(a: float, b: float) -> float:
    """Multiplicación a * b"""
    return a * b


def div(a: float, b: float) -> float:
    """División a / b. Lanza ValueError si b == 0"""
    if b == 0:
        raise ValueError("División por cero")
    return a / b


# ---------------------------
# Funciones matemáticas comunes
# ---------------------------
def factorial(n: int) -> int:
    """Factorial iterativo. Para n < 0 lanza ValueError"""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def fibonacci(n: int) -> List[int]:
    """Lista con los primeros n números de Fibonacci (n >= 0)"""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def is_prime(n: int) -> bool:
    """Prueba de primalidad simple (determinista suficiente para n razonable)"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


# ---------------------------
# Utilidades para listas / estadísticas simples
# ---------------------------
def sum_list(values: Iterable[float]) -> float:
    """Suma de elementos"""
    return sum(values)


def mean(values: Iterable[float]) -> Optional[float]:
    """Media aritmética; devuelve None si la secuencia está vacía"""
    vals = list(values)
    if not vals:
        return None
    return sum(vals) / len(vals)


def median(values: Iterable[float]) -> Optional[float]:
    """Mediana; devuelve None si vacío"""
    vals = sorted(values)
    n = len(vals)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return vals[mid]
    return (vals[mid - 1] + vals[mid]) / 2


def unique(values: Iterable[Any]) -> List[Any]:
    """Devuelve los elementos en orden de aparición sin duplicados"""
    seen = set()
    result = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


def flatten(nested: Iterable[Iterable[Any]]) -> List[Any]:
    """Aplana una lista de listas en una sola lista (una sola profundidad)"""
    result = []
    for sub in nested:
        result.extend(sub)
    return result


def most_common(values: Iterable[Any], n: int = 1) -> List[Any]:
    """Devuelve los n elementos más comunes en orden descendente"""
    c = Counter(values)
    return [item for item, _ in c.most_common(n)]


# ---------------------------
# Utilidades de archivos
# ---------------------------
def read_text(path: str) -> str:
    """Lee y devuelve el contenido de un archivo de texto"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    """Escribe contenido en un archivo de texto (sobrescribe)"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def find_in_file(path: str, substring: str) -> List[int]:
    """Devuelve las líneas (1-based) que contienen substring"""
    matches = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if substring in line:
                matches.append(i)
    return matches


# ---------------------------
# Ejemplos / CLI simple
# ---------------------------
def demo():
    print("Ejemplos rápidos de funciones básicas:")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"div(7, 2) = {div(7, 2)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"fibonacci(7) = {fibonacci(7)}")
    print(f"is_prime(29) = {is_prime(29)}")
    vals = [3, 1, 4, 1, 5, 9, 2]
    print(f"vals = {vals}")
    print(f"sum = {sum_list(vals)}, mean = {mean(vals)}, median = {median(vals)}")
    print(f"unique(vals) = {unique(vals)}")
    print(f"most_common(vals, 2) = {most_common(vals, 2)}")


def parse_args(argv):
    p = argparse.ArgumentParser(description="Utilidades básicas (demo)")
    p.add_argument("--demo", action="store_true", help="Ejecutar demo")
    p.add_argument("--fib", type=int, help="Imprimir primeros N de Fibonacci")
    p.add_argument("--prime", type=int, help="Probar si N es primo")
    return p.parse_args(argv)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.demo:
        demo()
    elif args.fib is not None:
        print(f"Fibonacci({args.fib}) = {fibonacci(args.fib)}")
    elif args.prime is not None:
        print(f"is_prime({args.prime}) = {is_prime(args.prime)}")
    else:
        # comportamiento por defecto: mostrar demo
        demo()