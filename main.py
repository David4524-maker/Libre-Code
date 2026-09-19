# -*- coding: utf-8 -*-
"""
════════════════════════════════════════════════════════════════════════
  IDE MULTI-LENGUAJE  ·  Python 3.14 + Tkinter
════════════════════════════════════════════════════════════════════════
  Lenguajes:  HTML · JS · C++ · C · C# · Python · Terminal · TS · Go ·
              CodePen · Java · Malbolge · SQL · Rust · EZScript

  · El resultado aparece en el panel DERECHO (excepto "Terminal",
    que se abre en una consola real del sistema).
  · Atajos:  F5 = Ejecutar      Ctrl+S = Guardar
════════════════════════════════════════════════════════════════════════
"""

import os
import sys
import shutil
import sqlite3
import subprocess
import tempfile
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ══════════════════════════════════════════════════════════════════════
#  PLANTILLAS DE CÓDIGO
# ══════════════════════════════════════════════════════════════════════

TEMPLATES = {
"Python": '''print("Hola desde Python")
for i in range(1, 4):
    print("  linea", i)
print("Suma:", sum(range(1, 11)))
''',

"Terminal": '''echo Hola desde la Terminal
echo -------------------------
echo Este script se ejecuta en una consola real.
''',

"HTML": '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Demo HTML</title>
  <style>
    body { font-family: system-ui; background:#0f172a; color:#e2e8f0;
           display:flex; height:100vh; margin:0; align-items:center;
           justify-content:center; flex-direction:column; }
    h1 { color:#38bdf8; }
  </style>
</head>
<body>
  <h1>Hola desde HTML</h1>
  <p>Esto se abre en tu navegador.</p>
</body>
</html>
''',

"JS": '''console.log("Hola desde JavaScript");
const nums = [1, 2, 3, 4, 5];
console.log("Suma:", nums.reduce((a, b) => a + b, 0));
console.log("Fecha:", new Date().toLocaleString());
''',

"C": '''#include <stdio.h>

int main(void) {
    printf("Hola desde C\\n");
    for (int i = 0; i < 3; i++)
        printf("  contador = %d\\n", i);
    return 0;
}
''',

"C++": '''#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::cout << "Hola desde C++" << std::endl;
    std::vector<int> v{1, 2, 3, 4, 5};
    int s = std::accumulate(v.begin(), v.end(), 0);
    std::cout << "Suma vector: " << s << std::endl;
    return 0;
}
''',

"C#": '''using System;

class Program {
    static void Main() {
        Console.WriteLine("Hola desde C#");
        int suma = 0;
        for (int i = 1; i <= 10; i++) suma += i;
        Console.WriteLine($"Suma 1..10 = {suma}");
    }
}
''',

"TS": '''const saludo: string = "Hola desde TypeScript";
const numeros: number[] = [1, 2, 3, 4, 5];

interface Punto { x: number; y: number; }

const p: Punto = { x: 3, y: 7 };

console.log(saludo);
console.log("Suma:", numeros.reduce((a, b) => a + b, 0));
console.log("Punto:", p);
''',

"Go": '''package main

import "fmt"

func main() {
    fmt.Println("Hola desde Go")
    suma := 0
    for i := 1; i <= 10; i++ {
        suma += i
    }
    fmt.Println("Suma 1..10 =", suma)
}
''',

"Java": '''public class Main {
    public static void main(String[] args) {
        System.out.println("Hola desde Java");
        int suma = 0;
        for (int i = 1; i <= 10; i++) suma += i;
        System.out.println("Suma 1..10 = " + suma);
    }
}
''',

"Rust": '''fn main() {
    println!("Hola desde Rust");
    let suma: i32 = (1..=10).sum();
    println!("Suma 1..10 = {}", suma);
}
''',

"SQL": '''CREATE TABLE alumnos (id INTEGER, nombre TEXT, nota REAL);
INSERT INTO alumnos VALUES (1, 'Ana', 9.5);
INSERT INTO alumnos VALUES (2, 'Luis', 7.0);
INSERT INTO alumnos VALUES (3, 'Marta', 8.75);

SELECT * FROM alumnos;
SELECT nombre, nota FROM alumnos WHERE nota > 8;
''',

"CodePen": '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<style>
  body { margin:0; height:100vh; display:flex; align-items:center;
         justify-content:center; background:#111; color:#0f0;
         font-family: monospace; }
  #caja { text-align:center; }
  button { padding:10px 20px; font-size:16px; cursor:pointer; }
</style>
</head>
<body>
  <div id="caja">
    <h1>Mini CodePen</h1>
    <button onclick="saludar()">Pulsame</button>
    <p id="msg"></p>
  </div>
  <script>
    function saludar() {
      document.getElementById('msg').textContent =
        'Hola! Son las ' + new Date().toLocaleTimeString();
    }
  </script>
</body>
</html>
''',

# Programa clásico "Hello World" en Malbolge
"Malbolge": "(=<`#9]~6ZY32Vx/4Rs+0No-&Jk)\"Fh}|Bcy?`=*z]Kw%oG4UUS0/@-ejc(:'8dc",

# ─────────── NUEVO: EZScript ───────────
"EZScript": '''// ============================================
// EZScript — lenguaje en español
// ============================================

// --- Variables ---
var:(nombre, "Mundo")
var:(contador, 0)

// --- Salida ---
mostrar "¡Hola desde EZScript!"
mostrar nombre

// --- Bucles y aritmética ---
bucle:(5)
    incrementar:(contador, 1)
    mostrar contador
fin_bucle

// --- Matemáticas ---
sumar:(total, 10, 20)
multiplicar:(doble, total, 2)
mostrar doble

raiz:(r, 144)
mostrar r

// --- Cadenas ---
var:(texto, "hola mundo")
mayusculas:(texto)
mostrar texto

longitud:(texto)

// --- Aleatorio ---
random:(n, 1, 100)
mostrar n

// --- Lógica ---
igual_a:(esCinco, 5, 5)
mostrar esCinco

mayor_que:(esMayor, 10, 3)
mostrar esMayor

// --- Sistema ---
fecha
hora

// --- Logs ---
log_info:("Demo de EZScript completada")
log_warn:("Esto es una advertencia")
log_error:("Esto es un error simulado")

// --- Dibujo (solo se reporta en modo headless) ---
color:("rojo")
circulo:(100, 100, 40)
texto_canvas:(150, 60, "¡Hola EZScript!", "verde")
''',
}

LANGUAGES = ["HTML", "JS", "C++", "C", "C#", "Python", "Terminal",
             "TS", "Go", "CodePen", "Java", "Malbolge", "SQL", "Rust",
             "EZScript"]


# ══════════════════════════════════════════════════════════════════════
#  INTÉRPRETE DE MALBOLGE (puro Python)
# ══════════════════════════════════════════════════════════════════════

_CRAZY = ((1, 0, 0), (1, 0, 2), (2, 2, 1))
_MEM_SIZE = 59049          # 3^10


def _crazy(x, y):
    """Operación 'crazy' trit a trit."""
    z, p = 0, 1
    for _ in range(10):
        z += _CRAZY[x % 3][y % 3] * p
        x //= 3
        y //= 3
        p *= 3
    return z


def _rotr(x):
    """Rotación a la derecha de un valor de 10 trits."""
    return x // 3 + (x % 3) * 19683


def run_malbolge(code, stdin_text="", max_steps=8_000_000):
    """Ejecuta un programa Malbolge y devuelve su salida."""
    src = "".join(ch for ch in code if 33 <= ord(ch) <= 126)
    if not src:
        return False, "El programa Malbolge está vacío o tiene caracteres inválidos."

    mem = [ord(ch) for ch in src]
    if len(mem) < 2:
        mem.append(0)
    mem += [0] * (_MEM_SIZE - len(mem))
    for i in range(max(len(src), 2), _MEM_SIZE):
        mem[i] = _crazy(mem[i - 1], mem[i - 2])

    a = c = d = 0
    entrada = list(stdin_text)
    salida = []
    pasos = 0

    while pasos < max_steps:
        pasos += 1
        c %= _MEM_SIZE
        d %= _MEM_SIZE

        op = mem[c] = (mem[c] + c) % 94

        if op == 4:                      # jmp [d]
            c = mem[d]
            continue
        elif op == 5:                    # out a
            salida.append(chr(a % 256))
        elif op == 23:                   # in a
            a = ord(entrada.pop(0)) if entrada else 0
        elif op == 39:                   # rotr [d]; mov a,[d]
            a = mem[d] = _rotr(mem[d])
        elif op == 40:                   # mov d,[d]
            d = mem[d]
        elif op == 62:                   # crz [d],a; mov a,[d]
            a = mem[d] = _crazy(mem[d], a)
        elif op == 68:                   # nop
            pass
        elif op == 81:                   # halt
            break
        else:
            return False, ("Instrucción inválida en c=%d (op=%d).\n"
                           "Salida parcial:\n%s" % (c, op, "".join(salida)))
        c += 1

    texto = "".join(salida)
    if pasos >= max_steps:
        return False, "⏱ Límite de pasos alcanzado.\n" + texto
    return True, texto if texto.strip() else "(programa terminado sin salida)"


# ══════════════════════════════════════════════════════════════════════
#  INTÉRPRETE DE EZSCRIPT (modo headless)
# ══════════════════════════════════════════════════════════════════════

def run_ezscript(code):
    """
    Ejecuta código EZScript en modo headless (sin GUI).
    Devuelve (ok: bool, salida: str).
    Los comandos de dibujo/ventana se reportan como mensajes informativos.
    """
    import re as _re
    import random as _random
    import math as _math
    from datetime import datetime as _dt

    # Paleta en español
    COLOR_MAP = {
        "rojo": "#e74c3c", "azul": "#3498db", "verde": "#2ecc71",
        "amarillo": "#f1c40f", "naranja": "#e67e22", "morado": "#9b59b6",
        "rosa": "#fd79a8", "negro": "#2c3e50", "blanco": "#ffffff",
        "gris": "#95a5a6", "cian": "#00cec9", "violeta": "#a29bfe",
        "marron": "#6d4c41", "marrón": "#6d4c41",
        "dorado": "#fdcb6e", "plateado": "#b2bec3",
    }

    variables = {}
    salida = []
    should_stop = False
    current_draw_color = "#0984e3"
    current_line_width = 3
    text_positions = {}
    emulated_os = "unknown"

    def log(txt, level="info"):
        prefix = {"info": "   ", "warn": "⚠  ", "error": "✘  ",
                  "success": "✔  ", "dim": "·  "}.get(level, "   ")
        salida.append(prefix + str(txt))

    def get_color(val):
        clean = str(val).strip().lower().replace('"', '').replace("'", "")
        return COLOR_MAP.get(clean, clean)

    def eval_expr(expr):
        expr = str(expr).strip()
        if (expr.startswith('"') and expr.endswith('"')) or \
           (expr.startswith("'") and expr.endswith("'")):
            return expr[1:-1]
        tokens = _re.split(r'(\s+|[+\-*/()==><!]+)', expr)
        new_tokens = []
        for token in tokens:
            t = token.strip()
            if t in variables:
                v = variables[t]
                new_tokens.append(f'"{v}"' if isinstance(v, str) else str(v))
            else:
                new_tokens.append(token)
        parsed = "".join(new_tokens)
        try:
            return eval(parsed, {"__builtins__": None}, {})
        except Exception:
            return expr

    def s_int(v, default=0):
        try: return int(float(v))
        except Exception: return default

    # ── Preprocesado: expansión de bloques bucle:(N)…fin_bucle ──
    raw_lines = code.split('\n')
    expanded = []          # lista de (num, texto)
    i = 0
    stack = []
    while i < len(raw_lines):
        text = raw_lines[i]
        stripped = text.strip()
        m = _re.match(r'bucle:\s*\((.*?)\)', stripped)
        if m:
            n = s_int(eval_expr(m.group(1)), 0)
            stack.append((n, i))
            i += 1
            # recopilar cuerpo hasta fin_bucle
            body = []
            depth = 1
            while i < len(raw_lines) and depth > 0:
                s2 = raw_lines[i].strip()
                if s2.startswith("bucle:"):
                    depth += 1
                elif s2 == "fin_bucle":
                    depth -= 1
                    if depth == 0:
                        break
                body.append(raw_lines[i])
                i += 1
            if i >= len(raw_lines):
                expanded.append((len(expanded) + 1,
                                 "log_error:(\"bucle: sin fin_bucle\")"))
                break
            # expandir el cuerpo N veces
            for _ in range(max(0, n)):
                for bl in body:
                    expanded.append((len(expanded) + 1, bl))
            i += 1
            continue
        if stripped.startswith("fin_bucle"):
            # fin_bucle suelto: ignorar
            i += 1
            continue
        expanded.append((len(expanded) + 1, text))
        i += 1

    # ── Bucle principal de ejecución ──
    for num, raw in expanded:
        if should_stop:
            break
        line = raw.strip()
        if not line or line.startswith("//"):
            continue

        try:
            # ============ COMANDOS BASE ============
            if line.startswith("IA:"):
                m = _re.match(r'IA:\s*\((.*?)\)', line)
                if m: log(f"[IA] ← '{eval_expr(m.group(1))}'")

            elif line.startswith("SistemaOperativo:"):
                m = _re.match(r'SistemaOperativo:\s*\((.*?)\)', line)
                if m:
                    tgt = str(eval_expr(m.group(1))).strip()
                    if tgt in ("Windows", "macOS", "Linux"):
                        emulated_os = tgt
                        log(f"SO emulado: {emulated_os}")

            elif line.startswith("JS:"):    log(f"[JS] {line[3:].strip()}")
            elif line.startswith("HTML:"):  log(f"[HTML] {line[5:].strip()}")
            elif line.startswith("CSS:"):   log(f"[CSS] {line[4:].strip()}")
            elif line.startswith("JSON:"):
                try: log(f"[JSON] {__import__('json').loads(line[5:].strip())}")
                except Exception as e: log(f"JSON inválido L{num}: {e}", "warn")
            elif line.startswith("ICON:"): log(f"[Icono] {line[5:].strip()}")

            elif line.startswith("linea:"):
                m = _re.match(r'linea:\s*\((.*?)\)', line)
                if m:
                    a = [x.strip() for x in m.group(1).split(',')]
                    if len(a) >= 4:
                        x1, y1 = s_int(eval_expr(a[0])), s_int(eval_expr(a[1]))
                        x2, y2 = s_int(eval_expr(a[2])), s_int(eval_expr(a[3]))
                        col = get_color(eval_expr(a[4])) if len(a) > 4 else current_draw_color
                        log(f"[canvas] línea ({x1},{y1})→({x2},{y2}) color={col}")

            elif line.startswith("conectar:"):
                m = _re.match(r'conectar:\s*\((.*?)\)', line)
                if m:
                    a = [x.strip() for x in m.group(1).split(',')]
                    if len(a) >= 2:
                        log(f"[canvas] conectar '{eval_expr(a[0])}' ↔ '{eval_expr(a[1])}'")

            elif line.startswith("color:"):
                m = _re.match(r'color:\s*\((.*?)\)', line)
                if m: current_draw_color = get_color(eval_expr(m.group(1).strip()))

            elif line == "limpiar_pantalla":
                salida.clear()
                text_positions.clear()

            elif line == "limpiar_consola":
                salida.clear()

            elif line.startswith("mostrar ") or line.startswith("print "):
                log(eval_expr(line.split(" ", 1)[1]))

            elif line.startswith("boton:") or line.startswith("button:"):
                prefix = "boton:" if line.startswith("boton:") else "button:"
                content = line[len(prefix):].strip()
                if content.startswith("(") and content.endswith(")"):
                    content = content[1:-1]
                parts = content.split(",", 1)
                txt = str(eval_expr(parts[0]))
                log(f"[botón] «{txt}»  (no interactivo en modo headless)", "dim")

            # ============ VARIABLES Y CADENAS ============
            elif line.startswith("var:") or line.startswith("VARIABLE_DEFINIR:"):
                m = _re.match(r'(?:var|VARIABLE_DEFINIR):\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = eval_expr(m.group(2))

            elif line.startswith("incrementar:"):
                m = _re.match(r'incrementar:\s*\((.*?),(.*?)\)', line)
                if m:
                    k = m.group(1).strip()
                    variables[k] = variables.get(k, 0) + s_int(eval_expr(m.group(2)), 1)

            elif line.startswith("decrementar:"):
                m = _re.match(r'decrementar:\s*\((.*?),(.*?)\)', line)
                if m:
                    k = m.group(1).strip()
                    variables[k] = variables.get(k, 0) - s_int(eval_expr(m.group(2)), 1)

            elif line.startswith("entrada:"):
                m = _re.match(r'entrada:\s*\((.*?),(.*?)\)', line)
                if m:
                    log(f"[entrada] «{eval_expr(m.group(2))}» → (vacío en headless)", "dim")
                    variables[m.group(1).strip()] = ""

            elif line.startswith("mayusculas:"):
                m = _re.match(r'mayusculas:\s*\((.*?)\)', line)
                if m:
                    k = m.group(1).strip()
                    variables[k] = str(variables.get(k, "")).upper()

            elif line.startswith("minusculas:"):
                m = _re.match(r'minusculas:\s*\((.*?)\)', line)
                if m:
                    k = m.group(1).strip()
                    variables[k] = str(variables.get(k, "")).lower()

            elif line.startswith("longitud:"):
                m = _re.match(r'longitud:\s*\((.*?)\)', line)
                if m: log(f"Longitud: {len(str(eval_expr(m.group(1))))}")

            elif line.startswith("reemplazar:"):
                m = _re.match(r'reemplazar:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    k = m.group(1).strip()
                    variables[k] = str(variables.get(k, "")).replace(
                        str(eval_expr(m.group(2))), str(eval_expr(m.group(3))))

            elif line.startswith("tipo_dato:"):
                m = _re.match(r'tipo_dato:\s*\((.*?)\)', line)
                if m: log(f"Tipo: {type(eval_expr(m.group(1))).__name__}")

            elif line.startswith("concatenar:"):
                m = _re.match(r'concatenar:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        str(eval_expr(m.group(2))) + str(eval_expr(m.group(3)))

            elif line.startswith("a_numero:"):
                m = _re.match(r'a_numero:\s*\((.*?),(.*?)\)', line)
                if m:
                    try: variables[m.group(1).strip()] = float(eval_expr(m.group(2)))
                    except Exception: variables[m.group(1).strip()] = 0

            elif line.startswith("a_texto:"):
                m = _re.match(r'a_texto:\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = str(eval_expr(m.group(2)))

            elif line.startswith("unir:"):
                m = _re.match(r'unir:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        str(eval_expr(m.group(2))) + str(eval_expr(m.group(3)))

            elif line.startswith("dividir_texto:"):
                m = _re.match(r'dividir_texto:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        str(eval_expr(m.group(2))).split(str(eval_expr(m.group(3))))

            elif line.startswith("indice:"):
                m = _re.match(r'indice:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    lst = eval_expr(m.group(2))
                    idx = s_int(eval_expr(m.group(3)))
                    try: variables[m.group(1).strip()] = lst[idx]
                    except Exception: variables[m.group(1).strip()] = ""

            elif line.startswith("invertir:"):
                m = _re.match(r'invertir:\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = str(eval_expr(m.group(2)))[::-1]

            elif line.startswith("ordenar:"):
                m = _re.match(r'ordenar:\s*\((.*?),(.*?)\)', line)
                if m:
                    v = eval_expr(m.group(2))
                    try: variables[m.group(1).strip()] = sorted(v)
                    except Exception: variables[m.group(1).strip()] = v

            elif line.startswith("contar:"):
                m = _re.match(r'contar:\s*\((.*?)\)', line)
                if m: log(f"Contar: {len(str(eval_expr(m.group(1))))}")

            # ============ MATEMÁTICAS ============
            elif line.startswith("random:"):
                m = _re.match(r'random:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = _random.randint(
                        s_int(eval_expr(m.group(2))), s_int(eval_expr(m.group(3))))

            elif line.startswith("raiz:"):
                m = _re.match(r'raiz:\s*\((.*?),(.*?)\)', line)
                if m:
                    try: variables[m.group(1).strip()] = _math.sqrt(float(eval_expr(m.group(2))))
                    except Exception: variables[m.group(1).strip()] = 0

            elif line.startswith("potencia:"):
                m = _re.match(r'potencia:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = _math.pow(
                        float(eval_expr(m.group(2))), float(eval_expr(m.group(3))))

            elif line.startswith("redondear:"):
                m = _re.match(r'redondear:\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = round(float(eval_expr(m.group(2))))

            elif line.startswith("absoluto:"):
                m = _re.match(r'absoluto:\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = abs(float(eval_expr(m.group(2))))

            elif line.startswith("seno:"):
                m = _re.match(r'seno:\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = _math.sin(_math.radians(float(eval_expr(m.group(2)))))

            elif line.startswith("coseno:"):
                m = _re.match(r'coseno:\s*\((.*?),(.*?)\)', line)
                if m: variables[m.group(1).strip()] = _math.cos(_math.radians(float(eval_expr(m.group(2)))))

            elif line.startswith("maximo:"):
                m = _re.match(r'maximo:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = max(
                        float(eval_expr(m.group(2))), float(eval_expr(m.group(3))))

            elif line.startswith("minimo:"):
                m = _re.match(r'minimo:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = min(
                        float(eval_expr(m.group(2))), float(eval_expr(m.group(3))))

            elif line.startswith("pi:"):
                m = _re.match(r'pi:\s*\((.*?)\)', line)
                if m: variables[m.group(1).strip()] = _math.pi

            elif line.startswith("sumar:"):
                m = _re.match(r'sumar:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        float(eval_expr(m.group(2))) + float(eval_expr(m.group(3)))

            elif line.startswith("restar:"):
                m = _re.match(r'restar:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        float(eval_expr(m.group(2))) - float(eval_expr(m.group(3)))

            elif line.startswith("multiplicar:"):
                m = _re.match(r'multiplicar:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        float(eval_expr(m.group(2))) * float(eval_expr(m.group(3)))

            elif line.startswith("dividir:"):
                m = _re.match(r'dividir:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    try:
                        variables[m.group(1).strip()] = \
                            float(eval_expr(m.group(2))) / float(eval_expr(m.group(3)))
                    except Exception:
                        variables[m.group(1).strip()] = 0

            elif line.startswith("modulo:"):
                m = _re.match(r'modulo:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    try:
                        variables[m.group(1).strip()] = \
                            float(eval_expr(m.group(2))) % float(eval_expr(m.group(3)))
                    except Exception:
                        variables[m.group(1).strip()] = 0

            # ============ LÓGICA ============
            elif line.startswith("igual_a:"):
                m = _re.match(r'igual_a:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        (str(eval_expr(m.group(2))) == str(eval_expr(m.group(3))))

            elif line.startswith("mayor_que:"):
                m = _re.match(r'mayor_que:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    try:
                        variables[m.group(1).strip()] = \
                            float(eval_expr(m.group(2))) > float(eval_expr(m.group(3)))
                    except Exception:
                        variables[m.group(1).strip()] = False

            elif line.startswith("menor_que:"):
                m = _re.match(r'menor_que:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    try:
                        variables[m.group(1).strip()] = \
                            float(eval_expr(m.group(2))) < float(eval_expr(m.group(3)))
                    except Exception:
                        variables[m.group(1).strip()] = False

            elif line.startswith("y:"):
                m = _re.match(r'y:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        bool(eval_expr(m.group(2))) and bool(eval_expr(m.group(3)))

            elif line.startswith("o:"):
                m = _re.match(r'o:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = \
                        bool(eval_expr(m.group(2))) or bool(eval_expr(m.group(3)))

            elif line.startswith("no:"):
                m = _re.match(r'no:\s*\((.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = not bool(eval_expr(m.group(2)))

            # ============ DIBUJO (HEADLESS) ============
            elif line.startswith("rectangulo:"):
                m = _re.match(r'rectangulo:\s*\((.*?)\)', line)
                if m:
                    a = [eval_expr(x.strip()) for x in m.group(1).split(',')]
                    c = get_color(a[4]) if len(a) > 4 else current_draw_color
                    log(f"[canvas] rectángulo x={a[0]} y={a[1]} w={a[2]} h={a[3]} color={c}")

            elif line.startswith("circulo:"):
                m = _re.match(r'circulo:\s*\((.*?)\)', line)
                if m:
                    a = [eval_expr(x.strip()) for x in m.group(1).split(',')]
                    c = get_color(a[3]) if len(a) > 3 else current_draw_color
                    log(f"[canvas] círculo x={a[0]} y={a[1]} r={a[2]} color={c}")

            elif line.startswith("ovalo:"):
                m = _re.match(r'ovalo:\s*\((.*?)\)', line)
                if m:
                    a = [eval_expr(x.strip()) for x in m.group(1).split(',')]
                    c = get_color(a[4]) if len(a) > 4 else current_draw_color
                    log(f"[canvas] óvalo x={a[0]} y={a[1]} w={a[2]} h={a[3]} color={c}")

            elif line.startswith("triangulo:"):
                m = _re.match(r'triangulo:\s*\((.*?)\)', line)
                if m:
                    a = [eval_expr(x.strip()) for x in m.group(1).split(',')]
                    c = get_color(a[6]) if len(a) > 6 else current_draw_color
                    log(f"[canvas] triángulo puntos={a[:6]} color={c}")

            elif line.startswith("texto_canvas:"):
                m = _re.match(r'texto_canvas:\s*\((.*?),(.*?),(.*?)(?:,(.*?))?\)', line)
                if m:
                    x, y = eval_expr(m.group(1)), eval_expr(m.group(2))
                    t = eval_expr(m.group(3))
                    c = get_color(eval_expr(m.group(4))) if m.group(4) else current_draw_color
                    log(f"[canvas] texto '{t}' en ({x},{y}) color={c}")

            elif line.startswith("color_canvas:"):
                m = _re.match(r'color_canvas:\s*\((.*?)\)', line)
                if m: log(f"[canvas] fondo = {get_color(eval_expr(m.group(1)))}")

            elif line.startswith("grosor_linea:"):
                m = _re.match(r'grosor_linea:\s*\((.*?)\)', line)
                if m: current_line_width = s_int(eval_expr(m.group(1)), 1)

            elif line == "borrar_canvas":
                log("[canvas] borrado")

            elif line.startswith("poligono:"):
                log("[canvas] polígono")

            elif line.startswith("arco:"):
                log("[canvas] arco")

            elif line.startswith("cuadricula:"):
                m = _re.match(r'cuadricula:\s*\((.*?)\)', line)
                if m: log(f"[canvas] cuadrícula cada {eval_expr(m.group(1))}px")

            elif line.startswith("rgb:"):
                m = _re.match(r'rgb:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    r = s_int(eval_expr(m.group(1))) % 256
                    g = s_int(eval_expr(m.group(2))) % 256
                    b = s_int(eval_expr(m.group(3))) % 256
                    current_draw_color = f"#{r:02x}{g:02x}{b:02x}"

            # ============ SISTEMA ============
            elif line == "fecha":
                log(f"Fecha: {_dt.now().strftime('%Y-%m-%d')}")

            elif line == "hora":
                log(f"Hora: {_dt.now().strftime('%H:%M:%S')}")

            elif line == "hora_actual":
                log(_dt.now().strftime('%H:%M:%S'))

            elif line == "fecha_hora":
                log(_dt.now().strftime('%Y-%m-%d %H:%M:%S'))

            elif line.startswith("esperar:"):
                m = _re.match(r'esperar:\s*\((.*?)\)', line)
                if m:
                    try: t = float(eval_expr(m.group(1)))
                    except Exception: t = 0
                    log(f"[esperar] {t}s (simulado en headless)", "dim")

            elif line.startswith("alerta:"):
                m = _re.match(r'alerta:\s*\((.*?)\)', line)
                if m: log(f"[alerta] {eval_expr(m.group(1))}", "warn")

            elif line.startswith("confirmar:"):
                m = _re.match(r'confirmar:\s*\((.*?),(.*?)\)', line)
                if m:
                    log(f"[confirmar] {eval_expr(m.group(2))} → False (headless)", "dim")
                    variables[m.group(1).strip()] = False

            elif line.startswith("abrir_url:"):
                m = _re.match(r'abrir_url:\s*\((.*?)\)', line)
                if m: log(f"[URL] {eval_expr(m.group(1))}")

            elif line.startswith("copiar:"):
                m = _re.match(r'copiar:\s*\((.*?)\)', line)
                if m: log(f"[copiar] {eval_expr(m.group(1))}", "dim")

            elif line.startswith("notificacion:"):
                m = _re.match(r'notificacion:\s*\((.*?),(.*?)\)', line)
                if m:
                    log(f"[notif: {eval_expr(m.group(1))}] {eval_expr(m.group(2))}")

            elif line == "pitido":
                log("[pitido]", "dim")

            elif line.startswith("beep:"):
                m = _re.match(r'beep:\s*\((.*?)(?:,(.*?))?\)', line)
                if m: log(f"[beep] {eval_expr(m.group(1))}Hz", "dim")

            elif line.startswith("ejecutar_cmd:"):
                m = _re.match(r'ejecutar_cmd:\s*\((.*?)\)', line)
                if m: log(f"[CMD] {eval_expr(m.group(1))}")

            elif line.startswith("log_info:"):
                m = _re.match(r'log_info:\s*\((.*?)\)', line)
                if m: log(eval_expr(m.group(1)), "info")

            elif line.startswith("log_warn:"):
                m = _re.match(r'log_warn:\s*\((.*?)\)', line)
                if m: log(eval_expr(m.group(1)), "warn")

            elif line.startswith("log_error:"):
                m = _re.match(r'log_error:\s*\((.*?)\)', line)
                if m: log(eval_expr(m.group(1)), "error")

            elif line == "esperar_tecla":
                log("[esperar_tecla] (headless, se ignora)", "dim")

            elif line.startswith("uuid:"):
                m = _re.match(r'uuid:\s*\((.*?)\)', line)
                if m:
                    import uuid as _uuid
                    variables[m.group(1).strip()] = str(_uuid.uuid4())

            # ============ IA, WEB Y ARCHIVOS ============
            elif line.startswith("ia_resumir:"):
                m = _re.match(r'ia_resumir:\s*\((.*?)\)', line)
                if m:
                    log(f"[IA resumen] {str(eval_expr(m.group(1)))[:60]}...")

            elif line.startswith("ia_traducir:"):
                m = _re.match(r'ia_traducir:\s*\((.*?),(.*?)\)', line)
                if m:
                    log(f"[IA traducir → {eval_expr(m.group(2))}] {eval_expr(m.group(1))}")

            elif line.startswith("ia_explicar:"):
                m = _re.match(r'ia_explicar:\s*\((.*?)\)', line)
                if m: log("[IA explicar] análisis completado")

            elif line.startswith("crear_archivo:"):
                m = _re.match(r'crear_archivo:\s*\((.*?),(.*?)\)', line)
                if m:
                    try:
                        with open(eval_expr(m.group(1)), "w", encoding="utf-8") as f:
                            f.write(str(eval_expr(m.group(2))))
                        log(f"Archivo creado: {eval_expr(m.group(1))}", "success")
                    except Exception as e:
                        log(str(e), "error")

            elif line.startswith("leer_archivo:"):
                m = _re.match(r'leer_archivo:\s*\((.*?),(.*?)\)', line)
                if m:
                    try:
                        with open(eval_expr(m.group(2)), "r", encoding="utf-8") as f:
                            variables[m.group(1).strip()] = f.read()
                    except Exception as e:
                        log(f"Error al leer: {e}", "error")

            elif line.startswith("json_obtener:"):
                m = _re.match(r'json_obtener:\s*\((.*?),(.*?),(.*?)\)', line)
                if m:
                    try:
                        import json as _json
                        j = eval_expr(m.group(2))
                        data = _json.loads(j) if isinstance(j, str) else j
                        variables[m.group(1).strip()] = data.get(eval_expr(m.group(3)), "")
                    except Exception as e:
                        log(str(e), "warn")

            elif line.startswith("existe_archivo:"):
                m = _re.match(r'existe_archivo:\s*\((.*?),(.*?)\)', line)
                if m:
                    variables[m.group(1).strip()] = os.path.exists(str(eval_expr(m.group(2))))

            elif line.startswith("eliminar_archivo:"):
                m = _re.match(r'eliminar_archivo:\s*\((.*?)\)', line)
                if m:
                    try: os.remove(str(eval_expr(m.group(1))))
                    except Exception as e: log(str(e), "error")

            elif line.startswith("listar_archivos:"):
                m = _re.match(r'listar_archivos:\s*\((.*?),(.*?)\)', line)
                if m:
                    try: variables[m.group(1).strip()] = os.listdir(str(eval_expr(m.group(2))))
                    except Exception as e: log(str(e), "error")

            elif line.startswith("html_titulo:"):
                m = _re.match(r'html_titulo:\s*\((.*?)\)', line)
                if m: log(f"<title>{eval_expr(m.group(1))}</title>")

            elif line.startswith("css_tema:"):
                m = _re.match(r'css_tema:\s*\((.*?)\)', line)
                if m: log(f"[css_tema] {eval_expr(m.group(1))}")

            elif line.startswith("js_eval:"):
                m = _re.match(r'js_eval:\s*\((.*?)\)', line)
                if m: log(f"[JS] {eval_expr(m.group(1))}")

            elif line == "detener":
                should_stop = True
                log("Ejecución detenida.", "warn")

            else:
                # Comando desconocido: aviso pero no error fatal
                if ":" in line and not line.startswith("//"):
                    log(f"Comando no reconocido L{num}: {line}", "warn")

        except Exception as e:
            log(f"Error L{num}: {e}", "error")

    # ── Resumen final ──
    if variables:
        salida.append("")
        salida.append("── Variables finales ─────────────────")
        for k, v in variables.items():
            salida.append(f"   {k} = {v!r}")

    texto = "\n".join(salida)
    return True, texto if texto.strip() else "(programa terminado sin salida)"


# ══════════════════════════════════════════════════════════════════════
#  UTILIDADES DE EJECUCIÓN
# ══════════════════════════════════════════════════════════════════════

def _run_cmd(cmd, cwd=None, timeout=60, stdin_text=""):
    """Ejecuta un comando y devuelve (ok, salida)."""
    try:
        p = subprocess.run(
            cmd, cwd=cwd, input=stdin_text, text=True,
            encoding="utf-8", errors="replace",
            capture_output=True, timeout=timeout,
        )
        out = (p.stdout or "") + (p.stderr or "")
        if not out.strip():
            out = "(sin salida)  ·  código de retorno: %d" % p.returncode
        return p.returncode == 0, out
    except FileNotFoundError:
        return False, ("No se encontró el ejecutable «%s».\n"
                       "Instálalo o añádelo al PATH." % cmd[0])
    except subprocess.TimeoutExpired:
        return False, "⏱ Tiempo de ejecución excedido (%ds)." % timeout
    except Exception as e:
        return False, "Error al ejecutar: %r" % (e,)


def _tmp_file(td, name, content):
    path = os.path.join(td, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def _exe_name(td, base="main"):
    return os.path.join(td, base + (".exe" if os.name == "nt" else ""))


# ══════════════════════════════════════════════════════════════════════
#  RUNNERS POR LENGUAJE
# ══════════════════════════════════════════════════════════════════════

def run_python(code):
    with tempfile.TemporaryDirectory() as td:
        f = _tmp_file(td, "main.py", code)
        return _run_cmd([sys.executable, "-X", "utf8", f], cwd=td)


def run_html(code):
    td = tempfile.mkdtemp(prefix="html_")
    f = _tmp_file(td, "index.html", code)
    webbrowser.open("file://" + f.replace("\\", "/"))
    return True, ("🌐 HTML abierto en el navegador predeterminado.\n\n"
                  "Archivo temporal:\n" + f)


def run_codepen(code):
    td = tempfile.mkdtemp(prefix="codepen_")
    f = _tmp_file(td, "index.html", code)
    webbrowser.open("file://" + f.replace("\\", "/"))
    return True, ("🎨 Mini-CodePen renderizado en el navegador.\n"
                  "   (HTML + CSS + JS en un solo archivo)\n\n"
                  "Archivo temporal:\n" + f +
                  "\n\nConsejo: también puedes pegar esto en codepen.io/pen/")


def run_js(code):
    if not shutil.which("node"):
        return False, "Node.js no está instalado o no está en el PATH."
    with tempfile.TemporaryDirectory() as td:
        f = _tmp_file(td, "main.js", code)
        return _run_cmd(["node", f], cwd=td)


def run_c(code):
    if not shutil.which("gcc"):
        return False, "gcc no encontrado. Instala MinGW / GCC / TDM-GCC."
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "main.c", code)
        exe = _exe_name(td, "main")
        ok, out = _run_cmd(["gcc", src, "-O2", "-o", exe], cwd=td)
        if not ok:
            return False, "── Error de compilación (gcc) ──\n" + out
        return _run_cmd([exe], cwd=td)


def run_cpp(code):
    if not shutil.which("g++"):
        return False, "g++ no encontrado. Instala MinGW / GCC."
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "main.cpp", code)
        exe = _exe_name(td, "main")
        ok, out = _run_cmd(["g++", src, "-O2", "-std=c++17", "-o", exe], cwd=td)
        if not ok:
            return False, "── Error de compilación (g++) ──\n" + out
        return _run_cmd([exe], cwd=td)


def run_csharp(code):
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "Program.cs", code)
        exe = _exe_name(td, "Program")

        if shutil.which("csc"):
            ok, out = _run_cmd(["csc", "/nologo", "/out:" + exe, src], cwd=td)
            if not ok:
                return False, "── Error de compilación (csc) ──\n" + out
            return _run_cmd([exe], cwd=td)

        if shutil.which("mcs"):
            ok, out = _run_cmd(["mcs", "-out:" + exe, src], cwd=td)
            if not ok:
                return False, "── Error de compilación (mcs) ──\n" + out
            if shutil.which("mono"):
                return _run_cmd(["mono", exe], cwd=td)
            return _run_cmd([exe], cwd=td)

        if shutil.which("dotnet"):
            proj = os.path.join(td, "proj")
            ok, out = _run_cmd(["dotnet", "new", "console", "-o", proj,
                                "--force"], cwd=td, timeout=180)
            if not ok:
                return False, "── Error creando proyecto .NET ──\n" + out
            shutil.copy(src, os.path.join(proj, "Program.cs"))
            return _run_cmd(["dotnet", "run", "--project", proj,
                             "-v", "q", "--nologo"], cwd=td, timeout=240)

        return False, ("No se encontró ningún compilador de C#:\n"
                       "  · csc (Roslyn)   · mcs (Mono)   · dotnet (SDK)")


def run_ts(code):
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "main.ts", code)

        if shutil.which("tsc") and shutil.which("node"):
            ok, out = _run_cmd(["tsc", "--target", "es2020",
                                "--outDir", td, src], cwd=td, timeout=120)
            if not ok:
                return False, "── Error de compilación (tsc) ──\n" + out
            js = os.path.join(td, "main.js")
            if os.path.exists(js):
                return _run_cmd(["node", js], cwd=td)
            return True, out

        if shutil.which("ts-node"):
            return _run_cmd(["ts-node", src], cwd=td, timeout=120)

        if shutil.which("deno"):
            return _run_cmd(["deno", "run", "--allow-all", src],
                            cwd=td, timeout=120)

        return False, ("Se necesita alguna de estas cadenas:\n"
                       "  · tsc + node\n  · ts-node\n  · deno")


def run_go(code):
    if not shutil.which("go"):
        return False, "Go no está instalado o no está en el PATH."
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "main.go", code)
        return _run_cmd(["go", "run", src], cwd=td, timeout=180)


def run_java(code):
    if not shutil.which("javac") or not shutil.which("java"):
        return False, "JDK no encontrado (se necesitan javac y java)."
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "Main.java", code)
        ok, out = _run_cmd(["javac", "-encoding", "UTF-8", src], cwd=td)
        if not ok:
            return False, "── Error de compilación (javac) ──\n" + out
        return _run_cmd(["java", "-Dfile.encoding=UTF-8",
                         "-cp", td, "Main"], cwd=td)


def run_rust(code):
    if not shutil.which("rustc"):
        return False, "rustc no encontrado. Instala Rust (rustup)."
    with tempfile.TemporaryDirectory() as td:
        src = _tmp_file(td, "main.rs", code)
        exe = _exe_name(td, "main")
        ok, out = _run_cmd(["rustc", "-O", src, "-o", exe], cwd=td, timeout=180)
        if not ok:
            return False, "── Error de compilación (rustc) ──\n" + out
        return _run_cmd([exe], cwd=td)


def run_sql(code):
    """Ejecuta SQL sobre una base SQLite en memoria."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    lineas = []

    sentencias = [s.strip() for s in code.split(";") if s.strip()]
    if not sentencias:
        conn.close()
        return False, "No hay sentencias SQL."

    try:
        for st in sentencias:
            cur.execute(st)
            if cur.description:                       # SELECT / PRAGMA
                cols = [d[0] for d in cur.description]
                filas = cur.fetchall()
                lineas.append("┌─ " + " | ".join(cols))
                lineas.append("├" + "─" * 52)
                if not filas:
                    lineas.append("│ (0 filas)")
                for f in filas:
                    lineas.append("│ " + " | ".join(
                        "NULL" if v is None else str(v) for v in f))
                lineas.append("└─ %d fila(s)" % len(filas))
            else:                                     # INSERT / CREATE ...
                conn.commit()
                lineas.append("✔ OK  (%d fila(s) afectada(s))" % cur.rowcount)
            lineas.append("")
    except Exception as e:
        conn.close()
        return False, "── Error SQL ──\n%s\n\n%s" % (e, "\n".join(lineas))
    finally:
        try:
            conn.close()
        except Exception:
            pass

    return True, "\n".join(lineas).strip()


def run_terminal(code):
    """Abre una consola REAL del sistema con el script (excepción)."""
    try:
        if os.name == "nt":
            td = tempfile.mkdtemp(prefix="term_")
            bat = os.path.join(td, "script.bat")
            with open(bat, "w", encoding="utf-8") as f:
                f.write("@echo off\r\nchcp 65001 >nul\r\n")
                f.write(code.replace("\n", "\r\n"))
                f.write("\r\necho.\r\npause\r\n")
            os.startfile(bat)          # abre cmd.exe en ventana nueva
            return True, ("🖥  Script lanzado en una consola CMD nueva.\n"
                          "   (el resultado se muestra ahí, no aquí)\n\n"
                          "Archivo: " + bat)
        else:
            td = tempfile.mkdtemp(prefix="term_")
            sh = os.path.join(td, "script.sh")
            with open(sh, "w", encoding="utf-8") as f:
                f.write("#!/bin/bash\n" + code +
                        '\necho\necho "Pulsa Enter para cerrar..."\nread _\n')
            os.chmod(sh, 0o755)
            for term, args in (("x-terminal-emulator", ["-e"]),
                               ("gnome-terminal", ["--"]),
                               ("konsole", ["-e"]),
                               ("xfce4-terminal", ["-e"]),
                               ("xterm", ["-e"])):
                if shutil.which(term):
                    subprocess.Popen([term] + args + ["bash", sh])
                    return True, ("🖥  Script lanzado en %s.\n\nArchivo: %s"
                                  % (term, sh))
            return False, "No se encontró ningún emulador de terminal."
    except Exception as e:
        return False, "No se pudo abrir la terminal: %r" % (e,)


def run_malbolge_lang(code):
    return run_malbolge(code)


def run_ezscript_lang(code):
    """Wrapper para el intérprete EZScript headless."""
    try:
        return run_ezscript(code)
    except Exception as e:
        import traceback
        return False, "Error interno del intérprete EZScript:\n" + traceback.format_exc()


RUNNERS = {
    "HTML":     run_html,
    "JS":       run_js,
    "C++":      run_cpp,
    "C":        run_c,
    "C#":       run_csharp,
    "Python":   run_python,
    "Terminal": run_terminal,
    "TS":       run_ts,
    "Go":       run_go,
    "CodePen":  run_codepen,
    "Java":     run_java,
    "Malbolge": run_malbolge_lang,
    "SQL":      run_sql,
    "Rust":     run_rust,
    "EZScript": run_ezscript_lang,
}


# ══════════════════════════════════════════════════════════════════════
#  INTERFAZ GRÁFICA
# ══════════════════════════════════════════════════════════════════════

class MultiLangIDE:

    BG_EDITOR = "#1e1e1e"
    FG_EDITOR = "#dcdcdc"
    BG_OUT    = "#0d1117"
    FG_OUT    = "#7ee787"

    def __init__(self, root):
        self.root = root
        self.buffers = dict(TEMPLATES)
        self.current_lang = None
        self._running = False

        root.title("IDE Multi-Lenguaje  ·  Python 3.14 + Tkinter")
        root.geometry("1420x840")
        root.minsize(960, 580)

        estilo = ttk.Style()
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        # ── Contenedor principal de 3 paneles ─────────────────────
        paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self._build_left(paned)
        self._build_center(paned)
        self._build_right(paned)

        # ── Barra de estado ───────────────────────────────────────
        self.status = tk.StringVar(value="Listo.")
        barra = ttk.Label(root, textvariable=self.status, anchor="w",
                          relief=tk.SUNKEN, padding=(8, 3))
        barra.pack(fill=tk.X, side=tk.BOTTOM)

        # ── Atajos ────────────────────────────────────────────────
        root.bind("<F5>", lambda e: self.run_code())
        root.bind("<Control-s>", lambda e: self.save_file())
        root.bind("<Control-Return>", lambda e: self.run_code())

        # ── Selección inicial ─────────────────────────────────────
        self.listbox.selection_set(0)
        self.on_select()

    # ---------------------------------------------------------------
    def _build_left(self, paned):
        frame = ttk.Frame(paned, width=180)
        paned.add(frame, weight=0)

        ttk.Label(frame, text="LENGUAJES",
                  font=("Segoe UI", 11, "bold")).pack(anchor="w",
                                                      padx=6, pady=(4, 6))

        cont = ttk.Frame(frame)
        cont.pack(fill=tk.BOTH, expand=True)

        sb = ttk.Scrollbar(cont, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(
            cont, exportselection=False, activestyle="none",
            font=("Consolas", 11), width=15,
            yscrollcommand=sb.set,
            selectbackground="#2563eb", selectforeground="white",
        )
        sb.config(command=self.listbox.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for lang in LANGUAGES:
            self.listbox.insert(tk.END, "  " + lang)

        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    # ---------------------------------------------------------------
    def _build_center(self, paned):
        frame = ttk.Frame(paned)
        paned.add(frame, weight=4)

        barra = ttk.Frame(frame)
        barra.pack(fill=tk.X)

        ttk.Button(barra, text="▶  Ejecutar  (F5)",
                   command=self.run_code).pack(side=tk.LEFT, padx=2, pady=4)
        ttk.Button(barra, text="💾  Guardar",
                   command=self.save_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(barra, text="🧹  Limpiar salida",
                   command=self.clear_output).pack(side=tk.LEFT, padx=2)
        ttk.Button(barra, text="↺  Restaurar plantilla",
                   command=self.restore_template).pack(side=tk.LEFT, padx=2)

        self.lang_label = ttk.Label(barra, text="", font=("Segoe UI", 10, "italic"))
        self.lang_label.pack(side=tk.RIGHT, padx=8)

        zona = ttk.Frame(frame)
        zona.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        sb_v = ttk.Scrollbar(zona, orient=tk.VERTICAL)
        sb_h = ttk.Scrollbar(zona, orient=tk.HORIZONTAL)

        self.editor = tk.Text(
            zona, wrap=tk.NONE, undo=True,
            font=("Consolas", 11),
            bg=self.BG_EDITOR, fg=self.FG_EDITOR,
            insertbackground="#ffffff",
            selectbackground="#264f78",
            tabs=("4c",),
            yscrollcommand=sb_v.set,
            xscrollcommand=sb_h.set,
        )
        sb_v.config(command=self.editor.yview)
        sb_h.config(command=self.editor.xview)

        sb_v.pack(side=tk.RIGHT, fill=tk.Y)
        sb_h.pack(side=tk.BOTTOM, fill=tk.X)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Insertar / Tab con 4 espacios
        self.editor.bind("<Tab>", self._tab)

    def _tab(self, event):
        self.editor.insert(tk.INSERT, "    ")
        return "break"

    # ---------------------------------------------------------------
    def _build_right(self, paned):
        frame = ttk.Frame(paned)
        paned.add(frame, weight=3)

        ttk.Label(frame, text="RESULTADO",
                  font=("Segoe UI", 11, "bold")).pack(anchor="w",
                                                      padx=6, pady=(4, 6))

        cont = ttk.Frame(frame)
        cont.pack(fill=tk.BOTH, expand=True)

        sb = ttk.Scrollbar(cont, orient=tk.VERTICAL)
        self.output = tk.Text(
            cont, wrap=tk.WORD, font=("Consolas", 10),
            bg=self.BG_OUT, fg=self.FG_OUT,
            insertbackground="#ffffff",
            selectbackground="#264f78",
            state=tk.DISABLED,
            yscrollcommand=sb.set,
        )
        sb.config(command=self.output.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ═══════════════════════════════════════════════════════════════
    #  LÓGICA
    # ═══════════════════════════════════════════════════════════════

    def on_select(self, event=None):
        sel = self.listbox.curselection()
        if not sel:
            return

        # Guardar el buffer actual
        if self.current_lang:
            self.buffers[self.current_lang] = \
                self.editor.get("1.0", tk.END).rstrip("\n")

        lang = LANGUAGES[sel[0]]
        self.current_lang = lang

        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", self.buffers.get(lang, ""))
        self.lang_label.config(text="Lenguaje:  " + lang)
        self.status.set("Editando %s" % lang)

        if lang == "Terminal":
            self.set_output("🖥  MODO TERMINAL\n"
                            "─────────────────────────────────────────\n"
                            "Este lenguaje se ejecuta en una consola REAL\n"
                            "del sistema (CMD / bash), no aquí.\n\n"
                            "Pulsa ▶ Ejecutar (F5) para lanzarla.")
        elif lang == "EZScript":
            self.set_output("📜  EZScript — lenguaje en español.\n"
                            "─────────────────────────────────────────\n"
                            "Comandos disponibles: var:, mostrar/print,\n"
                            "incrementar:, sumar:, restar:, multiplicar:,\n"
                            "dividir:, raiz:, potencia:, random:, fecha,\n"
                            "hora, log_info:, log_warn:, log_error:,\n"
                            "bucle:(N) … fin_bucle, igual_a:, mayor_que:,\n"
                            "menor_que:, mayusculas:, longitud:, etc.\n\n"
                            "Los comandos de dibujo (circulo:, rectangulo:,\n"
                            "texto_canvas:, color:) se reportan en modo texto.\n\n"
                            "Pulsa ▶ Ejecutar (F5) para probar.")
        else:
            self.set_output("Listo. Pulsa ▶ Ejecutar (F5).")

    # ---------------------------------------------------------------
    def set_output(self, texto):
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", texto)
        self.output.config(state=tk.DISABLED)

    def clear_output(self):
        self.set_output("")

    def restore_template(self):
        if not self.current_lang:
            return
        self.buffers[self.current_lang] = TEMPLATES[self.current_lang]
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", TEMPLATES[self.current_lang])
        self.status.set("Plantilla restaurada: %s" % self.current_lang)

    # ---------------------------------------------------------------
    def run_code(self, event=None):
        if not self.current_lang:
            return
        if self._running:
            self.status.set("Ya hay una ejecución en curso...")
            return

        lang = self.current_lang
        code = self.editor.get("1.0", tk.END)
        self.buffers[lang] = code.rstrip("\n")

        self._running = True
        self.status.set("Ejecutando %s..." % lang)
        self.set_output("⏳  Ejecutando %s...\n" % lang)

        hilo = threading.Thread(target=self._worker,
                                args=(lang, code), daemon=True)
        hilo.start()

    def _worker(self, lang, code):
        try:
            runner = RUNNERS.get(lang)
            if runner is None:
                ok, salida = False, "Lenguaje no soportado."
            else:
                ok, salida = runner(code)
        except Exception as e:
            ok, salida = False, "Error interno del runner:\n%r" % (e,)

        self.root.after(0, self._mostrar_resultado, lang, ok, salida)

    def _mostrar_resultado(self, lang, ok, salida):
        self._running = False
        cabecera = ("✔  %s — ejecución correcta\n" % lang) if ok else \
                   ("✘  %s — se produjeron errores\n" % lang)
        self.set_output(cabecera + "═" * 48 + "\n\n" + str(salida))
        self.status.set(("Listo." if ok else "Terminado con errores.") +
                        "  ·  " + lang)

    # ---------------------------------------------------------------
    def save_file(self):
        if not self.current_lang:
            return
        ext = {
            "Python": ".py", "HTML": ".html", "JS": ".js", "C": ".c",
            "C++": ".cpp", "C#": ".cs", "TS": ".ts", "Go": ".go",
            "Java": ".java", "Rust": ".rs", "SQL": ".sql",
            "Terminal": ".bat" if os.name == "nt" else ".sh",
            "CodePen": ".html", "Malbolge": ".mb",
            "EZScript": ".ez",
        }.get(self.current_lang, ".txt")

        ruta = filedialog.asksaveasfilename(
            title="Guardar código %s" % self.current_lang,
            defaultextension=ext,
            initialfile="programa" + ext,
            filetypes=[("Archivo", "*" + ext), ("Todos", "*.*")],
        )
        if not ruta:
            return
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.editor.get("1.0", tk.END))
            self.status.set("Guardado en: " + ruta)
        except Exception as e:
            messagebox.showerror("Error al guardar", str(e))


# ══════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════

def main():
    root = tk.Tk()
    app = MultiLangIDE(root)
    root.mainloop()


if __name__ == "__main__":
    main()
