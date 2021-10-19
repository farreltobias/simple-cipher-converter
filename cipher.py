from functools import reduce

cipher = ["al", "ep", "is", "oc", "uv"]
text = "l asgpsrl rlecil mlrrcm ilatcv icbrp c olohcrrc olnildc"

def changeLetter(letter, first, second):
  return (first if letter == second else second) if letter in [first, second] else letter

def convert(acc, keys):
  return "".join([changeLetter(letter, *keys) for letter in acc])

print(reduce(convert, cipher, text))
