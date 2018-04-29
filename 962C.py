# http://codeforces.com/contest/962/problem/C

from collections import deque
import math
s=deque([(input(), 0)])
created=set()
visited=set()
while len(s):
  (x,l)=s.popleft()
  visited.add(x)
  if not len(x):
    print(-1)
    break
  
  y=math.trunc(math.sqrt(int(x)))**2
  if y == int(x) and not x.startswith('0'):
    print(l)
    break
  
  for i in range(len(x)):
    z=''.join(x[:i] + x[i+1:])
    if not (z in visited) and not ((z,l+1) in created):
      created.add((z, l+1))
      s.append((z, l+1))

  
