# alternating_caps.py

def alternating_caps(s, upper=True):
    if not s:
        return ''
    return  (s[0].upper() if upper else s[0].lower()) + alternating_caps(s[1:], (upper if s[0] == ' ' else not upper))
