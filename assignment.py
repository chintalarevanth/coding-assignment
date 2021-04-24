m={'Fitbit Plus':7980,'Ipods':22349,'MI band':999,'Cult Pass':2799,'Macbook Pro':229900,'Digital Camera':11101,'Alexa':9999,'Sandwich Toaster':2195,'Microwave Oven':9800,'Scale':4999}
l=[]
for i in m.values():
  l.append(i)
l.sort()
n=len(l)
w=int(input())
mini=100000
for i in range(n-w-1):
  k=l[i+w-1]-l[i]
  if k<mini:
    mini=k
    e=l.index(l[i+w-1])
    s=l.index(l[i])
print("Number of the employees:",w)
print("Here the goodies selected for distribution are:")
v=[]
for i in range(s,e+1):
  v.append(l[i])
for k,val in m.items():
  for i in v:
    if i==val:
      print(k,":",val)
print("And the choosen goodie with the highest price and the lowest price is",mini)