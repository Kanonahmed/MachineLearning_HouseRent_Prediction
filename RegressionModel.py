import numpy as np
import pandas as pd
import matplotlib as mtplotlib

def compute_co_efficient(x,y):
    number_of_position=np.size(x)
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    sum_xy=np.sum(x*y-number_of_position*x_mean*y_mean)
    sum_x=np.sum(x*x-number_of_position*x_mean*x_mean)
    p1=sum_xy/sum_x
    p0=y_mean-p1*x_mean
    return(p0,p1)
def plot_graph(x,y,b):
    #plot original graph
    mtplotlib.pyplot.scatter(x,y,color="m",marker="o",s=30)
    
    

def main():
   x=np.array([0,1,2,3,4,5,6,7,8,9])
   y=np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
   b=compute_co_efficient(x,y)
   print("The co-efficient\n b0= {}\n b1= {}".format(b[0],b[1]))
   plot_graph(x,y,b)
   
    
if __name__=="__main__":
    main()
