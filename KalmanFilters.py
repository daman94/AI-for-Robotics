
#
#def update(mean1, var1, mean2, var2):
#    new_mean = (mean1*var2 + mean2*var1 ) / (var1 + var2)
#    new_var = 1 / ( (1/var1) + (1/var2) )
#    return [new_mean , new_var]
#
#def predict(mean1,var1, mean2, var2):     #mean2 and var2 are motion gaussian variants
#    new_mean = mean1 + mean2
#    new_var = var1 + var2
#    return [new_mean , new_var]
#
#measurements = [5.,6.,7.,9.,10]
#motion = [1.,1.,2.,1.,1.]
#
#measurement_sigma = 4.
#motion_sigma = 2.
#mu = 0.
#sig = 1000.
#
#
#for n in range(len(measurements)):
#    [mu,sig] = update(mu , sig , measurements[n] , measurement_sigma)
#    print 'update: ' , [mu,sig]
#    [mu,sig] = predict(mu , sig , motion[n] , motion_sigma)
#    print 'predict:  , [mu,sig]
#
##print update(10.,8.,13.,2.)
##print predict(10.,4.,12.,14.)
#

from matrix import *

measurements = [1. , 2. , 3.]

def kalman_filter(x, P):
    for n in range(len(measurements)):
        
        # measurement update
        Z = matrix([[measurements[n]]])
        Y = Z - (H*x)
        S = (H*P*H.transpose() ) + R
        K = P*H.transpose()*S.inverse()
        x = x + (K*Y)
        P = (I - (K*H))*P
    
        # prediction
        x = (F*x) + u
        P = (F*P*F.transpose())
    return x,P

x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix([[1., 0.]]) # measurement function
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix

print kalman_filter(x, P)

