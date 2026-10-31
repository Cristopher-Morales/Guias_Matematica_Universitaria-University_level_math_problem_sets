
def RungeKutta_2(t_i,t_f,step,x_init,function):
    N=int((t_f-t_i)/step)
    x_s=[x_init]
    t_0,x_0=t_i,x_init
    for _ in range(1,N+1):
        k_1=function(t_0,x_0)
        x_1=x_0+0.5*step*(k_1+function(t_0+step,x_0+step*k_1))
        x_s.append(x_1)
        t_0,x_0=t_0+step,x_1
    return x_s

def RungeKutta_4(t_i,t_f,step,x_init,function):
    N=int((t_f-t_i)/step)
    x_s=[x_init]
    t_0,x_0=t_i,x_init
    for _ in range(1,N+1):
        k_1 = function(t_0, x_0)
        k_2 = function(t_0+step/2, x_0+step*k_1/2)
        k_3 = function(t_0+step/2, x_0+step*k_2/2)
        k_4 = function(t_0+step, x_0+step*k_3)
        x_1 = x_0+(1/6)*step*(k_1+2*k_2+2*k_3+k_4)
        x_s.append(x_1)
        t_0, x_0 = t_0+step, x_1
    return x_s

t_i=0
t_f=1
step=0.01
x_init=1.0
print(RungeKutta_2(t_i=t_i,t_f=t_f,step=step,x_init=x_init,function=lambda t,x: (t+2)*x/(t+1))[-1])
print(RungeKutta_4(t_i=t_i,t_f=t_f,step=step,x_init=x_init,function=lambda t,x: (t+2)*x/(t+1))[-1])