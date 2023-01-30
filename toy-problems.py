def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
  if n == 0:
    return
  TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
  print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
  TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

  
#driver code
N = int(input())
# A is from rod, C is the rod to be placed at, b is the auxiliary rod
TowerOfHanoi(N, 'A', 'C', 'B')
