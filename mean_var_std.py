import pandas as pd
import numpy as np
def calculate(lst:list)->dict:
    try:
        if(len(lst)<9):
            raise ValueError("List must contain nine numbers.")
        else:
            arr1=np.array(lst)
            arr2=arr1.reshape((3,3))
            dct={
                'mean':[np.mean(arr2,axis=0).tolist(),np.mean(arr2,axis=1).tolist(),np.mean(lst).tolist()],
                'variance':[np.var(arr2,axis=0).tolist(),np.var(arr2,axis=1).tolist(),np.var(lst).tolist()],
                'standard deviation':[np.std(arr2,axis=0).tolist(),np.std(arr2,axis=1).tolist(),np.std(lst).tolist()],
                'max':[np.max(arr2,axis=0).tolist(),np.max(arr2,axis=1).tolist(),np.max(lst).tolist()],
                'min':[np.min(arr2,axis=0).tolist(),np.min(arr2,axis=1).tolist(),np.min(lst).tolist()],
                'sum':[np.sum(arr2,axis=0).tolist(),np.sum(arr2,axis=1).tolist(),np.sum(lst).tolist()]
            }
            return dct;
            
            
    except ValueError as V:
        print(V)
