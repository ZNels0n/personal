#Zach Nelson
'''
Following the tutorial on:
https://www.geeksforgeeks.org/python/kalman-filter-in-python/
'''


import numpy as np

class KalmanFilter:
    '''Constructor Args:
    F: State Transition Matrix (system Model)
    B: Control matrix (effect of control input).
    H: Observation matrix (how we measure the state).
    Q: Process noise covariance (uncertainty in the process).
    R: Measurement noise covariance (uncertainty in the measurements).
    x0: Initial state estimate.
    P0: Initial error covariance (initial uncertainty of state estimate).
    '''
    def __init__(self, F, B, H, Q, R, x0, P0):
        self.F = F
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R
        self.x = x0
        self.P = P0

    '''
    Prediction Step
        Computes the next state prediction based on the current state and the system model and the control unit 
        Updates error Covariance to reflect increasing uncertainty
        returns predicted state
    '''
    def predict(self, u):
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + self.Q
        return self.x
    
    ''' Update Step:
        S: Computes the residual covariance (expected combined uncertainty of prediction and measurement).
        K: Calculates the Kalman Gain (balance factor for blending prediction and measurement).
        y: Measurement residual (innovation), the difference between real measurement and prediction.
        self.x: Updates the state estimate with the innovation, weighted by Kalman Gain.
        I: Identity matrix (for maintaining shape during update).
        self.P: Updates the error covariance to show increased certainty after measurement.
        Returns the updated state estimate.
    '''
    def update(self, z):
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        y = z - np.dot(self.H, self.x)
        self.x = self.x + np.dot(K, y)
        I = np.eye(self.P.shape[0])
        self.P = np.dot(I - np.dot(K, self.H), self.P)
        return self.x

'''
    F: Next position = position + velocity; next velocity = velocity.
    B: How control input (u, e.g. acceleration) affects position and velocity.
    H: we observe position only (not velocity).
    Q: Represents process (model) noise (added uncertainty).
    R: Measurement noise (sensor uncertainty).'''   

F = np.array([[1, 1], [0, 1]])
B = np.array([[0.5], [1]])
H = np.array([[1, 0]])
Q = np.array([[1, 0], [0, 1]])
R = np.array([[1]])

'''Filter state:
X0 -initial position, Velocity 1
Uncertainty Matrix'''

x0 = np.array([[0], [1]])
P0 = np.array([[1, 0], [0, 1]])

'''Run one iteration of the Kalman loop'''
#init Kalman Filter
kf = KalmanFilter(F, B, H, Q, R, x0, P0)

#control input
u = np.array([[1]])

#measurement
z = np.array([[1]])

#State Prediction
predicted_state = kf.predict(u)
print("Predicted state:\n", predicted_state)

#Update state Estimate
updated_state = kf.update(z)
print("Updated state:\n", updated_state)