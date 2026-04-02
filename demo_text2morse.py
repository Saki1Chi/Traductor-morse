# ─── Diccionario Morse ───────────────────────────────────────────────────────
MORSE = {
    # Letras
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    # Números
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.',
    # Puntuación
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',  ')': '-.--.-',
    '@': '.--.-.', '=': '-...-',
} 


MORSE_INV = {v: k for k, v in MORSE.items()}


# ─── Traducción ──────────────────────────────────────────────────────────────
def encode(text: str) -> str:
    """Texto → Morse.  Palabras separadas por ' / '."""
    tokens = []
    for char in text.upper():
        if char == ' ':
            tokens.append('/')
        elif char in MORSE:
            tokens.append(MORSE[char])
        else:
            tokens.append('?')
    return ' '.join(tokens)


def decode(morse: str) -> str:
    """Morse → Texto.  Acepta '/' o ' / ' como separador de palabra."""
    # Normalizar separador de palabras
    morse = morse.strip().replace(' / ', ' / ')
    resultado = []
    for word in morse.split(' / '):
        for token in word.strip().split():
            resultado.append(MORSE_INV.get(token, '?'))
        resultado.append(' ')
    return ''.join(resultado).strip()


# ─── Ejemplos de uso ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(encode("HOLA MUNDO"))
    print(decode(".... --- .-.. .- / -- ..- -. -.. ---"))
