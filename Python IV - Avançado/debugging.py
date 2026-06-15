# ===== debugging =====

# linting
# ide/editor
# read errors
# pdb
import pdb

def somar(a,b,c):
    pdb.set_trace()
    return a+b+c

somar(4, 32, 67)
