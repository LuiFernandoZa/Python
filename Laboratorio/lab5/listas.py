li1=[1,2,3,4,5,6,7,8,9,10]
li2=[5,6,7,8,9,10,11,12,13,14,15]
li3=[10,11,12,13,14,15,16,17,18,19,20]
c1=set(li1)
c2=set(li2)
c3=set(li3)
c4=c1.intersection(c2 and c3)
c5=c1.union(c2 and c3)
c6=c1.difference(c3)
tp1=tuple(c4)
tp2=tuple(c5)
tp3=tuple(c6)
print(tp1)
print(tp2)
print(tp3)
sum=tp2[0]+tp2[int(len(tp2))-1]
sum2=tp3[0]+tp3[int(len(tp3))-1]
print(sum)