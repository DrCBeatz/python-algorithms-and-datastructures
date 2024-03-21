# euclids_algorithm.py

def gcd(x: int, y: int) -> int:
  return x if y == 0 else gcd(y, x % y)
