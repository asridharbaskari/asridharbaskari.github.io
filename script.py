from operator import add, mul
n, q = map(int, input().split())
d = [[i, 0] for i in reversed(range(1, n+1))]
dir = {
  'R' : [1, 0],
  'L' : [-1, 0],
  'U' : [0, 1],
  'D' : [0, -1]
}
offset = 0
for _ in range(q):
#   print(d)
  t, c = input().split()
  t = int(t)
  if t==1:
    d.append(list(map(add,d[-1],map(mul, dir[c], [-1, 1]))))
    offset += 1
  else:
    c=int(c)
    c-=1
    print(*d[c + offset])
    
    