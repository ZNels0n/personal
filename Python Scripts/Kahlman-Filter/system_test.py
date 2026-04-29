#zach Nelson
'''
Program to simulate a system Dynamics. Used for testing Controls and Kalman algorythms
USe state Variable Modeling'''

#imports

from system import *

#feed forward state with no feedback
def update_state(A,B,C,D,X,Y, ut):
    num_state = X.size
    W_d = np.random.multivariate_normal(mean,C_d).reshape(num_state, 1)

    dX = A@X + B@ut + W_d
    #update state variables
    X = X + dX 
    Y =  C@X + D@ut #matrix operation uses @ in numpy?
    return X, Y

def unit_feedback(A,B,C,D,X,Y, rt):
    #I don't think this is the correct math
    K = 1
    num_state = X.size
    W_d = np.random.multivariate_normal(mean,C_d).reshape(num_state, 1)
    
    #take the difference between the reverence and the output
    ut = rt-Y
    #update the derivitive
    dX = A@X + K*B@ut + W_d
    #update state variables
    X = X + dX 
    #update the output
    Y =  C@X + K*D@ut #matrix operation uses @ in numpy
    
    return X, Y


#defien the state parameters
num_state = 2
num_output = 2
num_input = 2

#define the state parameters
#following  dX = Ax + BY
#and        Y = Cx + Du

#state Equation parameters
A = np.array([[-2,-1],[1,0]])
B = np.array([[1,0],[0,1]])
#print(f'A = \n{A} ,\n B = \n{B}')

#output state parameters
C = np.array([[1,2],[0,1]])
D = np.array([[0,0],[0,0]])
#print(f'C = \n{C}, \n D = \n{D}')


#Add disturbance into the model
mean = np.array([0,0])
C_d = np.array([[.1,0],[0,.1]])

#time limits
t_final=100
t_step=0.1

#Want Sinusiodal Input
f = 2*np.pi*(1/40)
U_s = np.arange(0,t_final, t_step)
U_s = np.array([np.sin(f*U_s),np.sin(f*U_s)])

#use the system object 
sys = system(num_state, num_output, num_input)
sys.set_A(A)
sys.set_B(B)
sys.set_C(C)
sys.set_D(D)
            

ts, xs, ys = sys.sim_system(t_final=100, t_step=0.1, U=U_s, state_update_function=unit_feedback)
sys.plot_series(ts, U_s, xs, ys)
