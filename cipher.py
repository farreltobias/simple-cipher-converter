from functools import reduce

cipher = ["al", "ep", "is", "oc", "uv", "rt"]
text = "a ligeira raposa marrom saltou sobre o cachorro cansado"

def changeLetter(letter, first, second):
  return second if (letter == first) else first if (letter == second) else letter

def convert(acc, keys):
  return "".join([changeLetter(letter, *keys) for letter in acc])

encrypted = reduce(convert, cipher, text)
decrypted = reduce(convert, cipher, encrypted)

print(f'Texto Original: {text}\nChaves: {", ".join(cipher)}\n\nCifrado: {encrypted}\nDecifrado: {decrypted}')
