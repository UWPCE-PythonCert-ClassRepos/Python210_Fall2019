from decimal import Decimal 

#Task One
t= ( 2, 123.4567, 10000, 12345.67)
f= "file000"
a= '%.2f' % (t[1])
x= '%.2f' % Decimal (t[2])  
y= '{:0.2e}'.format (t[3])  
d= (f[0:-(len(str(t[0])))] +str(t[0]))

print(d + " :   " + a + ", " + x + ", " +y )