# -*- coding: utf-8 -*-
"""
════════════════════════════════════════════════════════════════════════
  IDE MULTI-LENGUAJE  ·  Python 3.14 + Tkinter
════════════════════════════════════════════════════════════════════════
  Lenguajes:  HTML · JS · C++ · C · C# · Python · Terminal · TS · Go ·
              CodePen · Java · Malbolge · SQL · Rust · EZScript

  · Cada lenguaje REPLICA su propia consola/terminal en el panel derecho
    (colores, fuente, prompt y comando de compilación realistas).
  · "Terminal" abre una consola real del sistema.
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

"Malbolge": "(=<`#9]~6ZY32Vx/4Rs+0No-&Jk)\"Fh}|Bcy?`=*z]Kw%oG4UUS0/@-ejc(:'8dc",

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
#  TEMAS DE CONSOLA POR LENGUAJE (replica el "terminal" de cada uno)
# ══════════════════════════════════════════════════════════════════════
#
#  Cada tema define:
#    bg          → color de fondo del panel
#    fg          → color del texto normal
#    font        → fuente del panel
#    cursor      → color del cursor de texto
#    cmd         → línea de comando falsa que se muestra arriba
#    prompt      → prefijo (ej. "$", "C:\>", ">>>")
#    ok_fg       → color para salida correcta
#    err_fg      → color para errores
#    cmd_fg      → color para la línea de comando
#    info_fg     → color para mensajes del sistema
#    banner      → texto que aparece al seleccionar el lenguaje

CONSOLE_THEMES = {

    "Python": {
        "bg": "#0c0c0c", "fg": "#e6e6e6",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "$ python -X utf8 main.py",
        "prompt": ">>> ",
        "ok_fg": "#e6e6e6", "err_fg": "#ff5555",
        "cmd_fg": "#8be9fd", "info_fg": "#f1fa8c",
        "banner": "Python 3.14 — REPL/script runner",
    },

    "Terminal": {
        "bg": "#0c0c0c", "fg": "#cccccc",
        "font": ("Lucida Console", 10), "cursor": "#ffffff",
        "cmd": "C:\\Users\\user> script.bat",
        "prompt": "C:\\Users\\user> ",
        "ok_fg": "#cccccc", "err_fg": "#f92672",
        "cmd_fg": "#8be9fd", "info_fg": "#f1fa8c",
        "banner": "Windows CMD · bash",
    },

    "HTML": {
        "bg": "#f6f8fa", "fg": "#24292f",
        "font": ("Segoe UI", 10), "cursor": "#24292f",
        "cmd": "🌐  render en navegador → index.html",
        "prompt": "",
        "ok_fg": "#22863a", "err_fg": "#cb2431",
        "cmd_fg": "#0969da", "info_fg": "#6f42c1",
        "banner": "Navegador (render HTML)",
    },

    "CodePen": {
        "bg": "#1c2029", "fg": "#e6e6e6",
        "font": ("Segoe UI", 10), "cursor": "#ffffff",
        "cmd": "🎨  CodePen · HTML + CSS + JS  → index.html",
        "prompt": "",
        "ok_fg": "#50fa7b", "err_fg": "#ff5555",
        "cmd_fg": "#ff79c6", "info_fg": "#8be9fd",
        "banner": "Mini-CodePen (navegador)",
    },

    "JS": {
        "bg": "#1e1e1e", "fg": "#d4d4d4",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "$ node main.js",
        "prompt": "> ",
        "ok_fg": "#d4d4d4", "err_fg": "#f48771",
        "cmd_fg": "#569cd6", "info_fg": "#4ec9b0",
        "banner": "Node.js REPL / script",
    },

    "TS": {
        "bg": "#1e1e1e", "fg": "#d4d4d4",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "$ tsc --target es2020 main.ts && node main.js",
        "prompt": "> ",
        "ok_fg": "#d4d4d4", "err_fg": "#f48771",
        "cmd_fg": "#3178c6", "info_fg": "#4ec9b0",
        "banner": "TypeScript → JavaScript (tsc) → Node.js",
    },

    "C": {
        "bg": "#000000", "fg": "#00ff41",
        "font": ("Consolas", 10), "cursor": "#00ff41",
        "cmd": "$ gcc main.c -O2 -o main && ./main",
        "prompt": "$ ",
        "ok_fg": "#00ff41", "err_fg": "#ff0040",
        "cmd_fg": "#00bfff", "info_fg": "#ffff00",
        "banner": "GCC · compilación + ejecución",
    },

    "C++": {
        "bg": "#0f0f1a", "fg": "#00d4ff",
        "font": ("Consolas", 10), "cursor": "#00d4ff",
        "cmd": "$ g++ main.cpp -O2 -std=c++17 -o main && ./main",
        "prompt": "$ ",
        "ok_fg": "#00d4ff", "err_fg": "#ff2d55",
        "cmd_fg": "#7b68ee", "info_fg": "#ffd700",
        "banner": "G++ 17 · compilación + ejecución",
    },

    "C#": {
        "bg": "#1e1e1e", "fg": "#dcdcdc",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "$ dotnet run  ·  (ó csc / mcs + mono)",
        "prompt": "> ",
        "ok_fg": "#dcdcdc", "err_fg": "#f48771",
        "cmd_fg": "#68217a", "info_fg": "#4ec9b0",
        "banner": ".NET / Roslyn / Mono",
    },

    "Java": {
        "bg": "#1b1b1b", "fg": "#f8f8f2",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "$ javac Main.java && java Main",
        "prompt": "$ ",
        "ok_fg": "#f8f8f2", "err_fg": "#ff5555",
        "cmd_fg": "#f89820", "info_fg": "#50fa7b",
        "banner": "OpenJDK · javac + java",
    },

    "Go": {
        "bg": "#0c0c0c", "fg": "#00add8",
        "font": ("Consolas", 10), "cursor": "#00add8",
        "cmd": "$ go run main.go",
        "prompt": "$ ",
        "ok_fg": "#00add8", "err_fg": "#ff5555",
        "cmd_fg": "#00bcd4", "info_fg": "#f1fa8c",
        "banner": "Go toolchain · go run",
    },

    "Rust": {
        "bg": "#1c1410", "fg": "#f0dfc8",
        "font": ("Consolas", 10), "cursor": "#ff6a00",
        "cmd": "$ rustc -O main.rs -o main && ./main",
        "prompt": "$ ",
        "ok_fg": "#f0dfc8", "err_fg": "#ff5555",
        "cmd_fg": "#ff6a00", "info_fg": "#fce94f",
        "banner": "rustc · compilación nativa",
    },

    "SQL": {
        "bg": "#282c34", "fg": "#abb2bf",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "sqlite>  (base de datos en memoria)",
        "prompt": "sqlite> ",
        "ok_fg": "#98c379", "err_fg": "#e06c75",
        "cmd_fg": "#61afef", "info_fg": "#e5c07b",
        "banner": "SQLite 3 · modo memoria",
    },

    "Malbolge": {
        "bg": "#1a0033", "fg": "#ff00ff",
        "font": ("Courier New", 10), "cursor": "#ff00ff",
        "cmd": "$ malbolge runner --trits=10 --memory=59049",
        "prompt": "👾 ",
        "ok_fg": "#ff00ff", "err_fg": "#ff0055",
        "cmd_fg": "#00ffff", "info_fg": "#ffff00",
        "banner": "Malbolge · intérprete puro de 10 trits",
    },

    "EZScript": {
        "bg": "#1e272e", "fg": "#ffffff",
        "font": ("Consolas", 10), "cursor": "#0984e3",
        "cmd": "$ ezscript ejecutar demo.ez",
        "prompt": "ez> ",
        "ok_fg": "#ffffff", "err_fg": "#e74c3c",
        "cmd_fg": "#0984e3", "info_fg": "#f1c40f",
        "banner": "EZScript · intérprete en español",
    },

    # Tema por defecto por si algo falta
    "_default": {
        "bg": "#0d1117", "fg": "#c9d1d9",
        "font": ("Consolas", 10), "cursor": "#ffffff",
        "cmd": "",
        "prompt": "",
        "ok_fg": "#7ee787", "err_fg": "#ff7b72",
        "cmd_fg": "#79c0ff", "info_fg": "#ffa657",
        "banner": "Consola genérica",
    },
}


# ══════════════════════════════════════════════════════════════════════
#  TEMAS DE EDITOR POR LENGUAJE (replica el IDE/editor real de cada uno)
# ══════════════════════════════════════════════════════════════════════
#
#  Esto es DISTINTO de CONSOLE_THEMES: aquí se tematiza el panel donde
#  se ESCRIBE el código (self.editor), no el panel de resultado.
#
#  Cada tema define:
#    bg          → color de fondo del editor
#    fg          → color del texto
#    font        → fuente del editor
#    cursor      → color del cursor de texto
#    select_bg   → color de fondo al seleccionar texto
#    select_fg   → color de texto al seleccionar
#    tabwidth    → ancho de la tabulación (ej. "4c", "8c")
#    ide         → nombre del IDE/editor que se está replicando

EDITOR_THEMES = {

    "Python": {
        "bg": "#ffffff", "fg": "#000000",
        "font": ("Consolas", 11), "cursor": "#000000",
        "select_bg": "#c0dbf6", "select_fg": "#000000",
        "tabwidth": "4c",
        "ide": "IDLE — Python Shell",
    },

    "Terminal": {
        "bg": "#1e1e1e", "fg": "#cccccc",
        "font": ("Lucida Console", 11), "cursor": "#ffffff",
        "select_bg": "#264f78", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "Editor de script (.bat / .sh)",
    },

    "HTML": {
        "bg": "#ffffff", "fg": "#1e1e1e",
        "font": ("Consolas", 11), "cursor": "#1e1e1e",
        "select_bg": "#add6ff", "select_fg": "#000000",
        "tabwidth": "2c",
        "ide": "VS Code · HTML5",
    },

    "CodePen": {
        "bg": "#1e1e1e", "fg": "#e6e6e6",
        "font": ("Consolas", 11), "cursor": "#47cf73",
        "select_bg": "#3a3a3a", "select_fg": "#ffffff",
        "tabwidth": "2c",
        "ide": "CodePen · HTML + CSS + JS",
    },

    "JS": {
        "bg": "#1e1e1e", "fg": "#d4d4d4",
        "font": ("Consolas", 11), "cursor": "#ffffff",
        "select_bg": "#264f78", "select_fg": "#ffffff",
        "tabwidth": "2c",
        "ide": "VS Code · JavaScript (Node.js)",
    },

    "TS": {
        "bg": "#1e1e1e", "fg": "#d4d4d4",
        "font": ("Consolas", 11), "cursor": "#3178c6",
        "select_bg": "#264f78", "select_fg": "#ffffff",
        "tabwidth": "2c",
        "ide": "VS Code · TypeScript",
    },

    "C": {
        "bg": "#ffffff", "fg": "#000000",
        "font": ("Consolas", 11), "cursor": "#000000",
        "select_bg": "#c9def9", "select_fg": "#000000",
        "tabwidth": "4c",
        "ide": "Code::Blocks · GCC",
    },

    "C++": {
        "bg": "#2b2b2b", "fg": "#a9b7c6",
        "font": ("Consolas", 11), "cursor": "#ffffff",
        "select_bg": "#214283", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "CLion (Darcula) · G++ 17",
    },

    "C#": {
        "bg": "#1e1e1e", "fg": "#dcdcdc",
        "font": ("Consolas", 11), "cursor": "#68217a",
        "select_bg": "#264f78", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "Visual Studio · .NET",
    },

    "Go": {
        "bg": "#2b2b2b", "fg": "#a9b7c6",
        "font": ("Consolas", 11), "cursor": "#00add8",
        "select_bg": "#214283", "select_fg": "#ffffff",
        "tabwidth": "8c",
        "ide": "GoLand · go run",
    },

    "Java": {
        "bg": "#2b2b2b", "fg": "#bababa",
        "font": ("Consolas", 11), "cursor": "#f89820",
        "select_bg": "#214283", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "IntelliJ IDEA (Darcula) · javac",
    },

    "Rust": {
        "bg": "#1c1410", "fg": "#f0dfc8",
        "font": ("Consolas", 11), "cursor": "#ff6a00",
        "select_bg": "#4a2f14", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "VS Code · rust-analyzer",
    },

    "SQL": {
        "bg": "#ffffff", "fg": "#1a1a1a",
        "font": ("Consolas", 11), "cursor": "#0969da",
        "select_bg": "#cfe4ff", "select_fg": "#000000",
        "tabwidth": "4c",
        "ide": "DBeaver · SQLite",
    },

    "Malbolge": {
        "bg": "#1a0033", "fg": "#ff00ff",
        "font": ("Courier New", 11), "cursor": "#00ffff",
        "select_bg": "#4b0082", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "Editor esotérico · Malbolge",
    },

    "EZScript": {
        "bg": "#1e272e", "fg": "#ffffff",
        "font": ("Consolas", 11), "cursor": "#0984e3",
        "select_bg": "#0984e3", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "EZScript IDE (ES)",
    },

    # Tema por defecto por si algo falta
    "_default": {
        "bg": "#1e1e1e", "fg": "#dcdcdc",
        "font": ("Consolas", 11), "cursor": "#ffffff",
        "select_bg": "#264f78", "select_fg": "#ffffff",
        "tabwidth": "4c",
        "ide": "Editor genérico",
    },
}


# ══════════════════════════════════════════════════════════════════════
#  INTÉRPRETE DE MALBOLGE (puro Python)
# ══════════════════════════════════════════════════════════════════════

_CRAZY = ((1, 0, 0), (1, 0, 2), (2, 2, 1))
_MEM_SIZE = 59049          # 3^10


def _crazy(x, y):
    z, p = 0, 1
    for _ in range(10):
        z += _CRAZY[x % 3][y % 3] * p
        x //= 3
        y //= 3
        p *= 3
    return z


def _rotr(x):
    return x // 3 + (x % 3) * 19683


def run_malbolge(code, stdin_text="", max_steps=8_000_000):
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

        if op == 4:
            c = mem[d]; continue
        elif op == 5:
            salida.append(chr(a % 256))
        elif op == 23:
            a = ord(entrada.pop(0)) if entrada else 0
        elif op == 39:
            a = mem[d] = _rotr(mem[d])
        elif op == 40:
            d = mem[d]
        elif op == 62:
            a = mem[d] = _crazy(mem[d], a)
        elif op == 68:
            pass
        elif op == 81:
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
    """Ejecuta EZScript en modo headless y devuelve (ok, salida)."""
    import re as _re
    import random as _random
    import math as _math
    from datetime import datetime as _dt

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

    # Preprocesado: expansión de bucles
    raw_lines = code.split('\n')
    expanded = []
    i = 0
    while i < len(raw_lines):
        text = raw_lines[i]
        stripped = text.strip()
        m = _re.match(r'bucle:\s*\((.*?)\)', stripped)
        if m:
            n = s_int(eval_expr(m.group(1)), 0)
            i += 1
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
            for _ in range(max(0, n)):
                for bl in body:
                    expanded.append((len(expanded) + 1, bl))
            i += 1
            continue
        if stripped.startswith("fin_bucle"):
            i += 1
            continue
        expanded.append((len(expanded) + 1, text))
        i += 1

    # Ejecución
    for num, raw in expanded:
        if should_stop:
            break
        line = raw.strip()
        if not line or line.startswith("//"):
            continue

        try:
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
                log(f"[botón] «{txt}»  (no interactivo en headless)", "dim")

            # ── Variables y cadenas ──
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

            # ── Matemáticas ──
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

            # ── Lógica ──
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

            # ── Dibujo (headless) ──
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

            # ── Sistema ──
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

            # ── IA, Web y archivos ──
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
                if ":" in line and not line.startswith("//"):
                    log(f"Comando no reconocido L{num}: {line}", "warn")

        except Exception as e:
            log(f"Error L{num}: {e}", "error")

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
            if cur.description:
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
            else:
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
    try:
        if os.name == "nt":
            td = tempfile.mkdtemp(prefix="term_")
            bat = os.path.join(td, "script.bat")
            with open(bat, "w", encoding="utf-8") as f:
                f.write("@echo off\r\nchcp 65001 >nul\r\n")
                f.write(code.replace("\n", "\r\n"))
                f.write("\r\necho.\r\npause\r\n")
            os.startfile(bat)
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
    try:
        return run_ezscript(code)
    except Exception:
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

        cabecera = ttk.Frame(frame)
        cabecera.pack(fill=tk.X, padx=6, pady=(4, 0))

        ttk.Label(cabecera, text="EDITOR",
                  font=("Segoe UI", 11, "bold")).pack(side=tk.LEFT)

        self.editor_label = ttk.Label(cabecera, text="",
                                       font=("Segoe UI", 10, "italic"))
        self.editor_label.pack(side=tk.LEFT, padx=(8, 0))

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
            bg="#0d1117", fg="#c9d1d9",
            insertbackground="#ffffff",
            selectbackground="#264f78",
            state=tk.DISABLED,
            yscrollcommand=sb.set,
            padx=10, pady=8,
        )
        sb.config(command=self.output.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Tags que se reconfiguran por lenguaje
        self.output.tag_configure("cmd",   font=("Consolas", 9, "italic"))
        self.output.tag_configure("ok",    font=("Consolas", 10))
        self.output.tag_configure("err",   font=("Consolas", 10, "bold"))
        self.output.tag_configure("info",  font=("Consolas", 10, "italic"))
        self.output.tag_configure("hr",    font=("Consolas", 9))
        self.output.tag_configure("banner",font=("Consolas", 11, "bold"))

    # ═══════════════════════════════════════════════════════════════
    #  TEMA DINÁMICO DE LA CONSOLA (por lenguaje)
    # ═══════════════════════════════════════════════════════════════
    def _apply_console_theme(self, lang):
        """Reconfigura el panel de resultado con el look del lenguaje."""
        theme = CONSOLE_THEMES.get(lang, CONSOLE_THEMES["_default"])

        # Fondo, texto, fuente, cursor
        self.output.configure(
            bg=theme["bg"],
            fg=theme["fg"],
            font=theme["font"],
            insertbackground=theme["cursor"],
        )

        # Tags con los colores del tema
        self.output.tag_configure("cmd",    foreground=theme["cmd_fg"])
        self.output.tag_configure("ok",     foreground=theme["ok_fg"])
        self.output.tag_configure("err",    foreground=theme["err_fg"])
        self.output.tag_configure("info",   foreground=theme["info_fg"])
        self.output.tag_configure("hr",     foreground=theme["cmd_fg"])
        self.output.tag_configure("banner", foreground=theme["info_fg"])

    def _apply_editor_theme(self, lang):
        """Reconfigura el panel de ESCRITURA (self.editor) con el look
        del IDE real de cada lenguaje. Esto es independiente del tema
        de la consola/resultado: aquí se tematiza el lugar donde se
        escribe el código, no el lugar donde se ve la salida."""
        theme = EDITOR_THEMES.get(lang, EDITOR_THEMES["_default"])

        self.editor.configure(
            bg=theme["bg"],
            fg=theme["fg"],
            font=theme["font"],
            insertbackground=theme["cursor"],
            selectbackground=theme["select_bg"],
            selectforeground=theme["select_fg"],
            tabs=(theme["tabwidth"],),
        )
        self.editor_label.config(text="·  " + theme["ide"])

    def _write_banner(self, lang):
        """Escribe un encabezado con el nombre del lenguaje/tema."""
        theme = CONSOLE_THEMES.get(lang, CONSOLE_THEMES["_default"])
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "● " + theme["banner"] + "\n", "banner")
        if theme.get("cmd"):
            self.output.insert(tk.END, theme["cmd"] + "\n\n", "cmd")
        self.output.config(state=tk.DISABLED)

    # ═══════════════════════════════════════════════════════════════
    #  LÓGICA
    # ═══════════════════════════════════════════════════════════════

    def on_select(self, event=None):
        sel = self.listbox.curselection()
        if not sel:
            return

        if self.current_lang:
            self.buffers[self.current_lang] = \
                self.editor.get("1.0", tk.END).rstrip("\n")

        lang = LANGUAGES[sel[0]]
        self.current_lang = lang

        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", self.buffers.get(lang, ""))
        self.lang_label.config(text="Lenguaje:  " + lang)
        self.status.set("Editando %s" % lang)

        # ── Aplicar tema del editor (donde se escribe el código) ──
        self._apply_editor_theme(lang)

        # ── Aplicar tema de consola del lenguaje (donde se ve el resultado) ──
        self._apply_console_theme(lang)
        self._write_banner(lang)

        # Avisos específicos
        if lang == "Terminal":
            self.output.config(state=tk.NORMAL)
            self.output.insert(tk.END,
                "\n🖥  Este lenguaje se ejecuta en una consola REAL\n"
                "   del sistema (CMD / bash), no aquí.\n"
                "   Pulsa ▶ Ejecutar (F5) para lanzarla.\n", "info")
            self.output.config(state=tk.DISABLED)

        elif lang == "EZScript":
            self.output.config(state=tk.NORMAL)
            self.output.insert(tk.END,
                "\n📜  Comandos: var:, mostrar/print, incrementar:,\n"
                "   sumar:/restar:/multiplicar:/dividir:, raiz:, random:,\n"
                "   bucle:(N)…fin_bucle, igual_a:, mayor_que:, menor_que:,\n"
                "   mayusculas:, longitud:, fecha, hora, log_info:, etc.\n"
                "   Los comandos de dibujo (circulo:, rectangulo:,\n"
                "   texto_canvas:, color:) se reportan como texto.\n", "info")
            self.output.config(state=tk.DISABLED)

        elif lang in ("HTML", "CodePen"):
            self.output.config(state=tk.NORMAL)
            self.output.insert(tk.END,
                "\n🌐  El resultado se abrirá en tu navegador al pulsar F5.\n", "info")
            self.output.config(state=tk.DISABLED)

    # ---------------------------------------------------------------
    def set_output(self, texto):
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", texto)
        self.output.config(state=tk.DISABLED)

    def clear_output(self):
        if self.current_lang:
            self._apply_console_theme(self.current_lang)
            self._write_banner(self.current_lang)
        else:
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

        # Mostrar "consola del lenguaje" mientras ejecuta
        self._apply_console_theme(lang)
        theme = CONSOLE_THEMES.get(lang, CONSOLE_THEMES["_default"])
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "● " + theme["banner"] + "\n", "banner")
        if theme.get("cmd"):
            self.output.insert(tk.END, theme["cmd"] + "\n\n", "cmd")
        self.output.insert(tk.END, "⏳  ejecutando...\n", "info")
        self.output.config(state=tk.DISABLED)

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
        theme = CONSOLE_THEMES.get(lang, CONSOLE_THEMES["_default"])

        # Reaplicar tema (por si acaso)
        self._apply_console_theme(lang)

        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)

        # Banner del lenguaje
        self.output.insert(tk.END, "● " + theme["banner"] + "\n", "banner")

        # Línea de comando "fake" replicando el shell real
        if theme.get("cmd"):
            self.output.insert(tk.END, theme["cmd"] + "\n", "cmd")
            self.output.insert(tk.END, "─" * 56 + "\n\n", "hr")

        # Salida real
        tag = "ok" if ok else "err"
        self.output.insert(tk.END, str(salida), tag)

        # Estado final
        if not str(salida).endswith("\n"):
            self.output.insert(tk.END, "\n")
        self.output.insert(tk.END, "\n")
        self.output.insert(
            tk.END,
            ("· proceso finalizado con éxito (exit 0)\n" if ok
             else "· proceso finalizado con errores (exit 1)\n"),
            "cmd",
        )

        self.output.config(state=tk.DISABLED)

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
