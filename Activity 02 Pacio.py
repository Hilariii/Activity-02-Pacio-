import random
import sys
import time
from time import sleep

lev = 90
p = 110
atck = 205
d = 188

trgts = 1
w = 1
bdge = 1
crit = 1
r = random.uniform(0.85, 1)
s = 1.5
typ = 0.5
burn = 1

m = (trgts*w*bdge*crit*r*s*typ*burn*1)
dmg = ((((((2 * lev / 5) + 2) * p) * (atck / d))) / (50 + 2) * m)

txt = "CHARIZARD used FIRE BLAST!"
for a in txt:
    sys.stdout.write(a)
    sys.stdout.flush()
    time.sleep(0.03)
sleep(0.80)
txt1 = "\nIt's not very effective..."
for b in txt1:
    sys.stdout.write(w)
    sys.stdout.flush()
    time.sleep(0.03)
sleep(0.90)
print("\nCHARIZARD attack dealt",round(dmg), "damage to FERALIGATR")