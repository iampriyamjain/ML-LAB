import matplotlib.pyplot as plt

x=[10,15,20,25,29,37,40,50]
y=[20,25,30,35,40,50,55,60]

size=len(x)

x1=0
y1=0
x2=0
y2=0
xy=0

for i in range(0,size):
    x1+=x[i]    
    y1+=y[i]
    x2+=(x[i]**2)
    y2+=(y[i]**2)
    xy+=(x[i]*y[i])

slope=(size*xy-x1*y1)/(size*x2-x1**2)
intercept=(y1-slope*x1)/size

print("intercept is :",intercept)
print("slope is :",slope)

plt.scatter(x,y)
ypred=[]
for i in range(0,len(x)):
    ypred.append(i+slope*x[i])
plt.plot(x,ypred,color="g")
plt.show()