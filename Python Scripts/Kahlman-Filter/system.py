#Zach Nelson
'''
Function to simulate a system using state Varriable model'''

#imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

#give default values for disturbances
mean = np.array([0,0])
C_d = np.array([[1,0],[0,1]])

class system():

    def __init__(self, num_state, num_output, num_input, A=None, B=None, C=None, D=None):
        self.num_state = num_state
        self.num_output = num_output
        self.num_input = num_input
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    
    def set_A(self,A):
        self.A = A
    def set_B(self,B):
        self.B = B
    def set_C(self,C):
        self.C = C
    def set_D(self,D):
        self.D = D

    def sim_system(self, t_final, t_step, U, state_update_function):
        #hold the variables for plotting
        Y_t = []
        X_t = []

        X = np.zeros((self.num_state,1))
        Y = np.zeros((self.num_output,1))

        #create a for loop for the state marching through time
        for t in range(0,int(t_final/t_step)):
            ut = U[:,t].reshape(self.num_input,1)
            X, Y = state_update_function(self.A,self.B,self.C,self.D, X, Y, ut)
            Y_t.append(Y)
            X_t.append(X)

        X_t = np.array(X_t)
        Y_t = np.array(Y_t)
        ts = np.arange(0,t_final,t_step)
        return ts, X_t, Y_t

    def plot_series(self, ts, U_t, X_t, Y_t):
        '''plt.plot(ts,U_t[1,:])
        plt.plot(ts,U_t[0,:])
        plt.xlabel("t")
        plt.ylabel('Input')
        plt.show()
        plt.plot(ts,X_t[:,0])
        plt.plot(ts,X_t[:,1])
        plt.xlabel("t")
        plt.ylabel('State Model')
        plt.show()
        plt.plot(ts,Y_t[:,0])
        plt.plot(ts,Y_t[:,1])
        plt.xlabel("t")
        plt.ylabel('Output')
        plt.show()'''
        plt.plot(ts,Y_t[:,0])
        plt.plot(ts,Y_t[:,1])
        plt.plot(ts,U_t[1,:])
        plt.plot(ts,U_t[0,:])
        plt.xlabel("t")
        plt.ylabel('Output')
        plt.show()