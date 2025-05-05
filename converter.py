MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '0': '-----',  '1': '.----', '2': '..---', '3': '...--',
    '4': '....-',  '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',  ' ': '/',     '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',
    '-': '-....-',  '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def text_to_morse(text):
    morse_code = []
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char.upper()])
    return ' '.join(morse_code)


def morse_to_text(morse):
    text = []
    for code in morse.split():
        if code in MORSE_CODE_DICT.values():
            text.append(next(key for key, value in MORSE_CODE_DICT.items() if value == code))
    return ''.join(text).capitalize()
