Juan Sebastian Gonzalez Alvarez
# Descripción del Programa

Este programa permite evaluar expresiones matemáticas ingresadas desde la terminal o un archivo de texto, soportando:
- Operaciones aritméticas: +, -, *, /
- Factorial !
- Funciones matemáticas: Sin, Cos, Tan, Sqrt, Ln, Log
- Paréntesis para control de precedencia
- Variables y asignaciones (x = 5)

# Diseño de la gramatica
- Asociatividad derecha: La recursión en addSub y mulDiv es derecha, es decir, 2 - 3 - 4 se interpreta como 2 - (3 - 4) en vez de (2 - 3) - 4.
- Factorial: '!' se maneja en unary, garantizando que 3! se evalúe antes de operaciones de multiplicación/división.
- Paréntesis: alteran la precedencia de manera estándar.
- Funciones: como Sin(expr) se evalúan antes de operaciones binarias.

  # Precedencia de Operadores (de mayor a menor)
  - Funciones y paréntesis: Sin(expr), (expr)
  - Factorial: n!
  - Multiplicación y división: * / (asociatividad derecha)
  - Suma y resta: + - (asociatividad derecha)
 
# Visitor
- Hereda de LabeledExprVisitor y LabeledExpr2Visitor.
- Implementa métodos para cada etiqueta de la gramática:
- visitAddSubRight, visitMulDivRight, visitUnaryFactorial, visitParens, visitFunction, etc.
- Maneja memoria de variables (self.memory) y evaluación de funciones trigonométricas, logaritmos y raíces.
- Factorial implementado recursivamente (factorial(n)).

El programa está implementado con ANTLR4 para el análisis léxico y sintáctico, usando un visitor en Python (EvalVisitor) para evaluar las expresiones.

# Uso del Programa

Generar parser y visitor con ANTLR4:

antlr4 -Dlanguage=Python3 -visitor -no-listener LabeledExpr2.g4

python3 main.py < cadenas.txt

<img width="726" height="431" alt="image" src="https://github.com/user-attachments/assets/cb11b17c-ca87-4b87-85cb-50e849b9fd61" />
