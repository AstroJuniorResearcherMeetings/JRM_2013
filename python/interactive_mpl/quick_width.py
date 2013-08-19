import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
import scipy.optimize
import scipy.integrate

def get_gaussian(self, wvs, center, g_width, g_depth, continuum):
    return continuum*(1.0 - g_depth*np.exp(-0.5*(wvs-center/g_width)**2))

class WidthMeasurement:
    
    def __init__(self, center, left, right, g_width, g_depth
                 continuum, integrated_width):
        self.left = left
        self.right = right
        self.center = center
        self.g_width = g_width
        self.g_depth = g_depth
        self.continuum = continuum
    
    @property
    def analytic_width(self):
        #the result of symbolically integrating the fitted gaussian
        return self.g_depth*self.g_width*np.sqrt(2*np.pi)

    def __str__(self):
        out_tup = (self.center, self.left, self.right, self.g_width, self.continuum)
        print "% 10.3f% 10.3f% 10.3f% 10.3f% 10.3f" % out_tup


class WidthFinder(wvs, flux):
    
    def __init__(self, wvs, flux):
        self.wvs = wvs
        self.flux = flux
        self.c_left = None
        self.c_right = None
        self.vlines = plt.vline([wvs[0], wvs[0]], 0.5, 1.5)
        self.fit_plot ,= plt.plot([wvs[0], wvs[1]], [1, 1])
        self.c_measurement = None
        self.measurements = []
    
    def set_left(self, wv):
        self.c_left = wv
    
    def set_right(self, wv):
        self.c_right = wv

    def fit_gaussian(self):
        try:
            assert c_left != None
            assert c_right != None
            fit_mask = self.wvs >= self.c_left
            fit_mask *= (self.wvs <= self.c_right)
            masked_wvs = self.wvs[fit_mask]
            masked_flux = self.flux[fit_mask]
            def g_error(param_vec):
                gaussian = get_gaussian(masked_wvs, *param_vec)
                return np.sum((masked_flux-gaussian)**2)
            
            #create guess gaussian parameters to start with
            fl_med = np.median(masked_flux)
            cont_guess = np.median(masked_flux[masked_flux > fl_med])
            flux_decr = np.where(masked_flux < cont_guess, cont_guess-masked_flux, 0)
            decr_sum = np.sum(flux_decr)
            cent_guess = np.sum(masked_wvs*flux_decr)/decr_sum
            sq_diffs = (masked_wvs-cent_guess)**2
            rms_diff = np.sqrt(np.sum(sq_diffs*flux_decr)/decr_sum)
            width_guess = rms_diff
            depth_guess = np.min(decr_sum)
            guess_vec = np.array([cent_guess, width_guess, depth_guess, cont_guess])
            #start the optimization running
            fit_params = scipy.optimize.fmin(g_error, guess_vec, maxfun=10000)[0]
            fcent, fwidth, fdepth, fcont = fit_params
            #carry out simpsons rule integration between the left and right
            integrated_width = scipy.integrate.simps(fcont-masked_flux, masked_wvs)
            self.c_measurement = WidthMeasurement(fcent, self.c_left, self.c_right, 
                                             fwidth, fdepth, fcont, integrated_width)
        except AssertionError:
            print "Error left and right not set"

    def on_key(self, event):
        wv = event.xdata
        key = event.key
        if key == "[":
            print "left set % 6.3f" % wv
            self.set_left(wv)
        elif key == "]":
            print "right set % 6.3f" % wv
            self.set_right(wv)
        elif key == "f":
            self.fit_gaussian()
            print "gaussian_fitted" 
            print str(self.c_measurement)
        elif key == "a":
            if self.c_measurement != None:
                self.measurements.append(self.c_measurement)

if __name__ == "__main__":

    
