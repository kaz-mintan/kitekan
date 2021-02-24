from func_new import *
import numpy as np

TIME_LEN = 25

def get_weight(signal,factor,mental): 
  weight = 
  return weight

def get_mental(signal,factor,mental):
  return new_mental

def out_error(signal,factor,mental,weight):
  return err

def main(signal,factor):
  if(signal.shape[0] == factor.shape[0]):
    mental = np.zeros(signal.shape[0])
    while(True):
      weight = get_weight(signal,factor,mental)
      mental = get_mental(signal,factor,mental)
  else:
    print("input same length data")

if __name__ == '__main__':
  signal = np.loadtxt("signal.csv",delimiter=",")
  factor = np.loadtxt("factor.csv",delimiter=",")
  main(signal,factor)
