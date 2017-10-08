import numpy as np
import pandas as pd
import matplotlib as mtplotlib

def compute_error_b0(y,y1):
    error=np.sum(y1-y)/len(y)
    return error

def compute_error_b1(y,y1,x):
    error=(y1-y)*x
    error=np.sum(error)/len(y)
    return error

def gradient_descent(b0,b1,x,y):
    alph=0.0001
    iterator=200000
    for i in range(0,iterator):
        pretiction=b0+b1*x
        error=compute_error_b0(y,pretiction)
        error1=compute_error_b1(y,pretiction,x)
        theta0=b0-alph*error
        theta1=b1-alph*error1
        b0=theta0
        b1=theta1
    return (theta0,theta1)
  
def plot_graph(x,y,b):      
    #plot original graph
    mtplotlib.pyplot.scatter(x,y,color="m",marker="o",s=30)
    #pretiction array
    y_predict=b[0]+b[1]*x    
    error=np.sum(pow(y-y_predict,2))/(2*len(y))
    print("error = {}".format(error))
    for i in range(0,len(y_predict)):
        y_predict[i]+=error
    
    mtplotlib.pyplot.plot(x,y_predict,color="g")
    mtplotlib.pyplot.xlabel('x')
    mtplotlib.pyplot.ylabel('predict_y')
    mtplotlib.pyplot.show()     


def main():
    x=np.array([0,1,2,3,4,5,6,7,8,9])
    y=np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    b=gradient_descent(0,0,x,y)
    print("The co-efficient\n b0= {}\n b1= {}".format(b[0],b[1]))
    plot_graph(x,y,b)



if __name__=="__main__":
    main()