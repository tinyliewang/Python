b0 = dict({'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'})
#b1 = dict('d:4',e:5,b:2,c:3,a:1)
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(b0)
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)