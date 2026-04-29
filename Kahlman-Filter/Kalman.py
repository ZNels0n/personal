#Zach Nelson
#Kalman Filter Import:


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
