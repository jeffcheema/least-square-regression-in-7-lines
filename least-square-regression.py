x = [2400,2650,2350,4950,3100,2500,5106,3100,2900,1750]
y = [41200,50100,52000,66000,44500,37700,73500,37500,56700,35600]
q = sum(((x[n]-sum(x)/len(x))**2)*1.0 for n in range(len(x)))
w = sum((-2*x[n]*y[n])+(2*x[n]*(sum(y)/len(y))+(2*y[n]*(sum(x)/len(x)))-(2*(sum(x)/len(x))*(sum(y)/len(y)))) for n in range(len(x)))
b = (-w)/(2*q)
a = -b*(sum(x)/len(x))+(sum(y)/len(y))
print "a: "+str(a)
print "b: "+str(b)
print str(a)+"+"+str(b)+"x"
