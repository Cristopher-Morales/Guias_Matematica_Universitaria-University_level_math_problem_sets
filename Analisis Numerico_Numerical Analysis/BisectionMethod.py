from plots import single_plot, multi_plot
from PrintTable import PrintTable
def bisection_method(a,b,func,tol,n_max):
    a_n=a
    b_n=b
    error=1.0
    n_iteration=0
    x_iter=[]
    error_iter=[]
    interval_iter=[]
    while (n_iteration<n_max and error>tol):
        mid=(b_n+a_n)/2
        error=abs(mid-a_n)/a_n
        error_iter.append(error)
        interval_iter.append((a_n,b_n))
        if func(a_n)*func(mid)<0:
            b_n=mid
        else:
            a_n=mid
        x_iter.append(mid)
        n_iteration+=1
    return x_iter[-1],n_iteration, x_iter,error_iter,interval_iter

x_sol,n_iter, x,e,intervals=bisection_method(1.0,2.0,lambda x: x**2-2,10**-6, 30)
iter=[i+1 for i in range(0,len(e))]

#####################################################
########## Print error ##############################
#####################################################
xlabel ='Iteration'
ylabel ='$log_{10}(Error)$'
title = 'Error per iteration'
# define figure variables to be used in creating the plots,
# if some of them are not giving, defaults value are going to be used
figure_name='Errors'
legend_location='upper left'
marker='ro'
marker_size= 8
figure_size= (8,6)
font_size=16
y_scale='log'
# define plot configuration
plot_config= {'xlabel': xlabel, 'ylabel': ylabel, 'title': title,'marker': marker,'y_scale': y_scale,
    'marker_size': marker_size, 'figure_size': figure_size, 'font_size': font_size}
single_plot(iter, e, **plot_config)

######################################################
########## Print intervals ###########################
######################################################

# Plot results
# define labels for each plot
label_1 = "Limite inferior intervalo"
label_2 = "Limite superior intervalo"
label_3 = "Approximacion Raiz"
# introduce x and y axis labels
xlabel='Iteracion[-]'
ylabel= "Intervalo[-]"
# define markers for each plot
marker_1= 'go'
marker_2= 'rx'
marker_3=  'bs'

# gather inputs, outputs, markers and labels in lists
x_s=[iter,iter, iter]
a_s=[]
b_s=[]
for (i,j) in intervals:
    a_s.append(i)
    b_s.append(j)
y_s=[a_s,b_s, x]
markers=[marker_1,marker_2, marker_3]
labels=[label_1,label_2, label_3]
# zip the list of inputs, targets, markers and labels used in the plot.
plots=zip(x_s,y_s,markers,labels)

# define figure variables to be used in creating the plots,
# if some of them are not giving, defaults value are going to be used
figure_name='plot_comparison'
figure_size=(8,6)
marker_size = 8
font_size = 16
legend_location='upper right'
# define plot configuration
plot_config= {'xlabel': xlabel, 'ylabel': ylabel, 'marker_size': marker_size,\
              'figure_size': figure_size, 'font_size': font_size, 'save_figure': 'no',\
              'figure_name': figure_name, 'legend_location': legend_location}

# plot results
multi_plot(plots, **plot_config)

# print table
header="n_iter|  a     |  b     |  approx  | error"
PrintTable(header,iter,a_s, b_s,x, e)