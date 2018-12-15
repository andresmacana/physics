from numpy import*
from pylab import*

x = arange(0.0,1.01,0.02)

q = 4*x*x*x-3*x*x*x*x
l = x
q2 = 4*q*q*q-3*q*q*q*q #correcto
q3 = 4*q2*q2*q2-3*q2*q2*q2*q2 #correcto

t = (3-2*x)/4
t1 = (3-2*t)/4
t2 = (3-2*t1)/4
t3 = (3-2*t2)/4
t4 =(3-2*t3)/4
t5 = (3-2*t4)/4
for i in arange(0,1,0.01):
    r = i
    p = 4*i*i*i-3*i*i*i*i
    #print r, p
    if r <= p:
        print r

r1=(1+sqrt(13))/6
print r1

y = arange(0.76,1.0,0.01)
q4 = 1-q # 1-prob(error) 1-(3*x**2-2*x**3)
#q5= 3*x*x*x-x*x*x*x

figure(1)
plot(x,q,'-r',label='classical')
plot(x,t,'-b',label='quantum')
#plot(x,l)
plot(x,q2,'+')
plot(x,q3,'.')
plot(x,t1,'-')
plot(x,t2)
plot(x,t3)
plot(x,t4)
plot(x,t5)
xlabel('nose')
ylabel('p')
title('Teleported vs classical')
legend(loc='upper left')
savefig('eraser_channel_1.png')

show()
