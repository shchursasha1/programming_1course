import math
s, R_zovnishnogo = [float(d) for d in input().split()]
r_vnutrishnogo = math.sqrt(R_zovnishnogo**2 - (s / math.pi))
print(f"{r_vnutrishnogo:.2f}")