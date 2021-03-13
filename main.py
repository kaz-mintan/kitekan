from func import *
from func_new import *
import numpy as np

TIME_LEN = 25
dir_path = "./test_dir/"

def set_phi(factor,signal,mental):
  if factor.shape[0] != mental.shape[0]:
    print("input same time size factor and mental")
    return -1
  else:

    size_x = factor.shape[1]#size_x is factor type
    size_t = mental.shape[0]#size_t is time length
    size_z = signal.shape[1]#size_z is signal type(facial expression type)

    #get_phi()
    phi = np.zeros((size_x,size_t,size_z))
    for sig_type in range(size_z):
      for t in range(size_t):
        for fac_type in range(size_x):
          phi[fac_type,t,sig_type]=func(inv_norm(4*sig_type+fac_type,factor[fac_type,sig_type]),mental[t],4*sig_type+fac_type)

    return phi

def get_weight(factor,signal,mental): 
  INDEX_HAP = 0
  INDEX_SUP = 1
  INDEX_ANG = 2
  INDEX_SAD = 3
  SIG_INDEX = [INDEX_HAP,INDEX_SUP,INDEX_ANG,INDEX_SAD]
  phi = set_phi(factor,signal,mental)
  weight = np.zeros((factor.shape[0],factor.shape[1],signal.shape[1]))
  for k in SIG_INDEX:
    weight[:,:,k] = np.linalg.pinv(phi[:,:,k])
  return weight

def get_mental(factor,signal,mental,weight):
  new_mental = None
  size_x = factor.shape[1]#size_x is factor type
  size_t = factor.shape[0]
  size_z = signal.shape[1]#size_z is signal type(facial expression type)
  sig_hat = np.zeros((size_t,size_z))

  while(err>ERR_THRE):
    for sig_type in range(size_z):
      for t in range(size_t):
        for fac_type in range(size_x):
          sig_hat[t,sig_type]+=weight[t,fac_type,sig_type]*func(inv_norm(4*sig_type+fac_type,factor[fac_type,sig_type]),mental[t],4*sig_type+fac_type)

    print("err",np.sum(sig_hat-signal))
  return new_mental

def out_error(factor,signal,mental,weight):
  err = None
  return err

def main(factor,signal,mental):
  count= 0
  if(signal.shape[0] == factor.shape[0]):
    mental = np.zeros(signal.shape[0])
    while(True):
      print("count",count)
      weight = get_weight(factor,signal,mental)
      mental = get_mental(factor,signal,mental,weight)
      count+=1
  else:
    print("input same length data")

if __name__ == '__main__':
  signal = np.loadtxt(dir_path+"signal_test.csv",delimiter=",")
  factor = np.loadtxt(dir_path+"factor_test.csv",delimiter=",")
  mental = np.loadtxt(dir_path+"mental_test.csv",delimiter=",")
  main(factor,signal,mental)
