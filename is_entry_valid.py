import re
def is_entry_valid(expr):
    literal = r'[abce](\*?)' # 'a', 'b', 'c' or 'e' seguido de un opcional y unico '*'
    simbolo = r'[.|]' # '.' o '|'
    expresion = re.compile (fr'({literal})({simbolo}{literal})*')
    return expresion.fullmatch(expr) is not None
