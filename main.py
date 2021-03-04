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
    size_x = factor.shape[1]
    size_y = mental.shape[0]
    size_z = signal.shape[1]
    phi = np.zeros((size_x,size_y,size_z))
    for k in range(size_z):
      for j in range(size_y):
        for i in range(size_x):
          phi[i,j,k]=func(inv_norm(4*k+i,factor[i,k]),mental[j],4*k+i)
    return phi

def get_weight(factor,signal,mental): 
  phi = set_phi(factor,signal,mental)
  print("phi shape",phi.shape)
  weight = np.linalg.pinv(phi[:,:,0])
  print("weight",weight.shape)
  return weight

def get_mental(signal,factor,mental):
  new_mental = None
  return new_mental

def out_error(signal,factor,mental,weight):
  err = None
  return err

def main(factor,signal,mental):
  if(signal.shape[0] == factor.shape[0]):
    mental = np.zeros(signal.shape[0])
    while(True):
      weight = get_weight(signal,factor,mental)
      mental = get_mental(signal,factor,mental)
  else:
    print("input same length data")

if __name__ == '__main__':
  signal = np.loadtxt(dir_path+"signal_test.csv",delimiter=",")
  factor = np.loadtxt(dir_path+"factor_test.csv",delimiter=",")
  mental = np.loadtxt(dir_path+"mental_test.csv",delimiter=",")
  main(signal,factor,mental)
