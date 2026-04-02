# Traductor de Código Morse

Herramientas para traducir texto a código Morse y viceversa, disponibles en dos versiones: un módulo Python para uso en terminal y una aplicación web que funciona directamente en el navegador.

---

## Archivos

### `demo_text2morse.py`
Módulo Python standalone que convierte texto a Morse y Morse a texto desde la terminal. No requiere instalar ninguna librería externa.

### `morse_dashboard.html`
Aplicación web bidireccional con interfaz gráfica. Se abre directamente en cualquier navegador, sin servidor ni instalación.

---

## ¿Qué hace cada uno?

### `demo_text2morse.py`

- Convierte cualquier texto a su equivalente en código Morse
- Decodifica una cadena Morse de vuelta a texto
- Cubre letras (A–Z), números (0–9) y puntuación común
- Los caracteres desconocidos se marcan con `?`
- Las palabras se separan con `/`

**Ejemplo de uso:**
```python
from demo_text2morse import encode, decode

encode("HOLA MUNDO")
# → '.... --- .-.. .- / -- ..- -. -.. ---'

decode(".... --- .-.. .- / -- ..- -. -.. ---")
# → 'HOLA MUNDO'
```

**Ejecución directa:**
```bash
python demo_text2morse.py
```

### `morse_dashboard.html`

Abre el archivo en el navegador y obtienes:

- **Modo Texto → Morse**: escribe texto y obtén el código Morse al instante
- **Modo Morse → Texto**: pega código Morse y lo decodifica en tiempo real
- **Representación visual**: los puntos y rayas se muestran como figuras animadas
- **Desglose por carácter**: cada letra con su código Morse correspondiente
- **Estadísticas**: cuenta de caracteres, palabras, puntos y rayas
- **Ejemplos rápidos**: SOS, HOLA MUNDO, MORSE 2025 y más
- **Copiar resultado**: copia la salida al portapapeles con un clic
- Funciona **offline**, sin internet ni dependencias

---

## Requisitos

| Archivo | Requisito |
|---|---|
| `demo_text2morse.py` | Python 3.6 o superior |
| `morse_dashboard.html` | Cualquier navegador moderno |

---

## Código Morse — referencia rápida

```
A .-    B -...  C -.-.  D -..   E .     F ..-.
G --.   H ....  I ..    J .---  K -.-   L .-..
M --    N -.    O ---   P .--.  Q --.-  R .-.
S ...   T -     U ..-   V ...-  W .--   X -..-
Y -.--  Z --..

0 -----  1 .----  2 ..---  3 ...--  4 ....-
5 .....  6 -....  7 --...  8 ---.   9 ----.
```

Separador de palabras: `/`
