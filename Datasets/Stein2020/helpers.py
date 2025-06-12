# FREQUENTLY USED FUNCTIONS FOR MODEL FITTING
# SERIAL BIAS NMDAR
# 
# author:   heike stein
# last mod: 23/04/20

# import packages
import numpy as np
import scipy as sp
import cmath
import scipy.stats as sps
import scikits.bootstrap as boot
import sklearn.model_selection as ms
import statsmodels.api as sm
from patsy import dmatrices


# functions
def filter_dat(dat, rt, iti, raderr, err):
    timeoutRT   = dat[dat.RT<rt]
    timeoutITI  = dat[dat.ITI<iti]
    raderror    = dat[dat.raderror<raderr]
    error       = dat[((dat.error<err) & (dat.error>-err))]
    return dat.iloc[timeoutRT.index & timeoutITI.index & raderror.index & error.index]

def len2(x):
    if type(x) is not type([]):
        if type(x) is not type(np.array([])):
            return -1
    return len(x)


def phase2(x):
    if not np.isnan(x):
        return cmath.phase(x)
    return nan


def wrap2pi(x):
    x[x > np.pi] = x[x > np.pi] - 2*np.pi
    x[x < -np.pi] = x[x < -np.pi] + 2*np.pi
    return x


def circdist(angles1, angles2):
    if len2(angles2) < 0:
        if len2(angles1) > 0:
            angles2 = [angles2]*len(angles1)
        else:
            angles2 = [angles2]
            angles1 = [angles1]     
    if len2(angles1) < 0:
        angles1 = [angles1]*len(angles2)
    return np.array(list(map(lambda a1, a2: phase2(np.exp(1j*a1) / np.exp(1j*a2)), 
        angles1, angles2)))


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array-value)).argmin()
    return idx


def sinfit(s,x):
    return np.sin(s*x)


def normgauss(xxx,sigma):
    gauss = (1/(sigma*np.sqrt(2*np.pi)) *np.exp(-(xxx-0)**2 / (2*sigma**2)))
    return gauss/gauss.max()


def normgrad(xxx):
    return np.gradient(xxx)/np.gradient(xxx).max()


def dog3(sigma,x):
    xxx     = np.arange(-2*np.pi, 2*np.pi, .0001) 
    dog_3rd = normgrad(normgrad(normgrad(normgauss(xxx,sigma))))
    return np.array(list(map(lambda x: dog_3rd[find_nearest(xxx,x)], x)))


def dog1(sigma,x):
    xxx     = np.arange(-2*np.pi, 2*np.pi, .0001) 
    dog_1st = normgrad(normgauss(xxx,sigma))
    return np.array(list(map(lambda x: dog_1st[find_nearest(xxx,x)], x)))


def cross_validate(y,X,subj=None):
    if subj==None:
        y_train,y_test, X_train,X_test = ms.train_test_split(y, X, test_size=.33)
    else:
        y_train,y_test, X_train,X_test = ms.train_test_split(y, X, test_size=.33,
        stratify=subj)
    glm     = sm.OLS(y_train, X_train).fit()
    y_pred  = glm.predict(X_test)
    return np.mean(np.square(y_pred.values-y_test.values.flatten()))


def serial_bias(prevcurr, error, window, step):
    xxx = np.arange(-np.pi, np.pi, step)
    m_err=[]; std_err=[]
    for t in xxx:
        idx = (prevcurr>=t-window/2) & (prevcurr<t+window/2)
        if t-window/2 < -np.pi:
            idx = (prevcurr>=t-window/2) & (prevcurr<t+window/2) | (prevcurr>np.pi-(window/2-(np.pi-np.abs(t))))
        if t+window/2 > np.pi:
            idx = (prevcurr>=t-window/2) & (prevcurr<t+window/2) | (prevcurr<-np.pi+(window/2-(np.pi-np.abs(t))))
        m_err.append(sps.circmean(error[idx], low=-np.pi, high=np.pi))
        std_err.append(sps.circstd(error[idx])/np.sqrt(np.sum(idx)))
    return np.array(m_err), np.array(std_err)


def folded_bias(prevcurr, error, window, step):
    xxx = np.arange(-np.pi, np.pi, step)
    t_err=[]; err = []
    for t in xxx:
        idx = (prevcurr>=t-window/2) & (prevcurr<t+window/2)
        if t-window/2 < -np.pi:
            idx = (prevcurr>=t-window/2) & (prevcurr<t+window/2) | (prevcurr>np.pi-(window/2-(np.pi-np.abs(t))))
        if t+window/2 > np.pi:
            idx = (prevcurr>=t-window/2) & (prevcurr<t+window/2) | (prevcurr<-np.pi+(window/2-(np.pi-np.abs(t))))
        t_err.append(list(error[idx]))
    for t in reversed(range(int(len(xxx)/2))):
        err.append([x*-1 for x in t_err[t]]+t_err[-t-1])
    m_err   = [sps.circmean(x, low=-np.pi, high=np.pi) for x in err]
    se_err  = [sps.circstd(x)/np.sqrt(len(x)) for x in err]
    return np.array(m_err), np.array(se_err)
