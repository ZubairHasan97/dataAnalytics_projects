import numpy as np

def calculate(list_data):
  try:
    np_arr = np.asarray(list_data)
    reshaped_arr = np_arr.reshape(3,3)
    dic = {
        'mean': [list(reshaped_arr.mean(axis=0)), list(reshaped_arr.mean(axis=1)), np_arr.mean()],
        'variance': [list(reshaped_arr.var(axis=0)), list(np.round(reshaped_arr.var(axis=1),2)), np.round(np_arr.var(),2)],
        'standard deviation': [list(np.round(reshaped_arr.std(axis=0),2)), list(np.round(reshaped_arr.std(axis=1),2)), np.round(np_arr.std(),2)],
        'max': [list(reshaped_arr.max(axis=0)), list(reshaped_arr.max(axis=1)), np_arr.max()],
        'min': [list(reshaped_arr.min(axis=0)), list(reshaped_arr.min(axis=1)), np_arr.min()],
        'sum': [list(reshaped_arr.sum(axis=0)), list(reshaped_arr.sum(axis=1)), np_arr.sum()]
    }
    # return dic
    print(dic)
  except ValueError:
    print('List must contain nine numbers.')

#Calling calculate() with a given list data
li_data = [0,1,2,3,4,5,6,7,8]
calculate(li_data)
