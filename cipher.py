from functools import reduce

cipher = ["al", "ep", "is", "oc", "uv"]
text = "l asgpsrl rlecil mlrrcm ilatcv icbrp c olohcrrc olnildc"

def changeLetter(letter, first, second):
  return second if (letter == first) else first if (letter == second) else letter

def convert(acc, keys):
  return "".join([changeLetter(letter, *keys) for letter in acc])

print(reduce(convert, cipher, text))
