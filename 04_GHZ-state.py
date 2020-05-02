# Greenberger-Horne-Zeiilinger state
from blueqat import Circuit

initial = Circuit().h[0,1].x[2]
# 000 -> ++1

xorX = Circuit().cx[1,2].cx[0,2]
# ++1 -> (001 + 010 + 100 + 111)/2

ghz = (initial + xorX).h[:].m[:].run(shots=100)
# (001 + 010 + 100 + 111)/2 -> (000 - 111)/√2


print(ghz)
# Counter({'000': 50, '111': 50})

