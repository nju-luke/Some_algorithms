import numpy
import scipy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation

def accumulation(posb):                 #accumulated possibility 
    p = 0
    accu = []
    for j in range(len(posb)):
        p += posb[j]
        accu.append(p)
    return accu
    
def turnplate_choose(pop):              #choos parents
    value = (pop-30)*sin(pop)+60
    sum_value = sum(value)    
    posb = value/sum_value
    posb_accu = accumulation(posb)
    query_r = rand()
    for i in range(len(posb)):       
        if posb_accu[i]>query_r:
            query_c = i
            break
    return query_c
    
def coding(index):                          #coding to binary
    index = int(index)
    index_bin = bin(index).replace('0b','')
    if len(index_bin)<chromo_size:
        index_bin = '0'*(chromo_size-len(index_bin))+index_bin   
    return index_bin
    
def decoding(str_o):                        #decoding to dec
    str_o = '0b'+str_o
    return eval(str_o)
    
def Cross_pop(pop,fa,mo):                   #generate the children
    posi = int(rand()*chromo_size)
    length = int(rand()*(chromo_size-posi))
    fa = float(pop[fa])/(end_point-start_point)*total
    mo = float(pop[mo])/(end_point-start_point)*total
    code_fa = coding(fa)
    code_mo = coding(mo)    
    childCod_1 = code_fa[:posi]+code_mo[posi:posi+length]+code_fa[posi+length:]
    childCod_2 = code_mo[:posi]+code_fa[posi:posi+length]+code_mo[posi+length:]  
    child_1 = decoding(childCod_1)
    child_2 = decoding(childCod_2)   
    child_1 = float(child_1)*(end_point-start_point)/total
    child_2 = float(child_2)*(end_point-start_point)/total    
    return child_1,child_2
    
def Mutation(pop1):                         #Mutate the children
    for i in range(len(pop1)):
        if rand()<0.25:
            posi = int(rand()*chromo_size)
            length = min(int(rand()*4),chromo_size-posi)
            pop_temp = float(pop1[i])/(end_point-start_point)*total            
            pop_temp = coding(pop_temp)
            pop_temp = pop_temp[:posi]+str(int((int(pop_temp[posi])-0.5)*(-1)+0.5))+pop_temp[posi+1:]           
            pop_temp = decoding(pop_temp)  
            pop1[i] = float(pop_temp)*(end_point-start_point)/total
            
            
global  start_point,pop_size,end_point,chromo_size,total,pop

start_point = 0
end_point = 80
pop_size = 50
chromo_size = 12
total = 2**12
generation = 500

fig = plt.figure()
ax = plt.axes(xlim=(start_point, end_point), ylim=(0,120))
x = linspace(start_point,end_point,total)
y = (x-30)*sin(x)+60
line, = ax.plot(x,y)

pop = rand(pop_size)*(end_point-start_point)+start_point
pop_start = copy(pop)
y1 = (pop_start-30)*sin(pop_start)+60
line, = ax.plot(pop_start,y1,'o',lw=5)

pop_x = []
pop_y = []

for j in range(generation):
    pop_new = []
    while len(pop_new)<pop_size:
        query_c1 = turnplate_choose(pop)     #turnplate choose model
        query_c2 = turnplate_choose(pop)
   
        child_1,child_2 = Cross_pop(pop,query_c1,query_c2)    #cross 
        pop_new.append(child_1)
        pop_new.append(child_2)
    
    pop = copy(pop_new)        
    Mutation(pop)
    y1 = (pop-30)*sin(pop)+60   
    
    pop_x.append(pop)
    pop_y.append(y1)

    
def animate(i):
    x = pop_x[i]
    y = pop_y[i]  
    line.set_data(x,y)
    plt.title('generation=%d'%(i+1))
    return line,
    
anim = animation.FuncAnimation(fig,animate,generation,
                interval=200, blit=False,repeat=False)
plt.show()     