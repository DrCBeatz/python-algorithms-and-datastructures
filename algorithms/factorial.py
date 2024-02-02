# factorial.py

def fact(n: int) -> int:
  if n <= 1:
    return 1
    
  return n * fact(n - 1)

def permutation(n: int, r: int) -> int:
  return fact(n) // fact(n - r)


def combination(n: int, r: int) -> int:
  return fact(n) // (fact(r) * fact(n - r))
