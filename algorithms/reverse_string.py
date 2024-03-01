# reverse_string.py

def reverse_string(s: str) -> str:
  """
  Recursive reverse string function
  """
  if not s:
    return ''
  return reverse_string(s[1:]) + s[0]
