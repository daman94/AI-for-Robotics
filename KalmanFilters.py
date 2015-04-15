

def update(mean1, var1, mean2, var2):
    new_mean = (mean1*var2 + mean2*var1 ) / (var1 + var2)
    new_var = 1 / ( (1/var1) + (1/var2) )
    return [new_mean , new_var]

def predict(mean1,var1, mean2, var2):     #mean2 and var2 are motion gaussian variants
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean , new_var]

measurements = [5.,6.,7.,9.,10]
motion = [1.,1.,2.,1.,1.]

measurement_sigma = 4.
motion_sigma = 2.
mu = 0.
sigma = 1000.


for n in range(len(measurements)):
    [mu,sigma] = update(mu , sigma , measurements[n] , measurement_sigma)
    print "update: " , [mu,sigma]
    [mu,sigma] = predict(mu , sigma , motion[n] , motion_sigma)
    print "predict: " , [mu,sigma]

#print update(10.,8.,13.,2.)
#print predict(10.,4.,12.,14.)
