import numpy as np

def calculate(list):
  
  if len(list) < 9 or len(list) > 9:
    raise ValueError("List must contain nine numbers.")
  
  matrix = np.array(list).reshape(3,3)
  #to_mean
  mean_1 = np.mean(matrix, axis=0).tolist()
  mean_2 = np.mean(matrix, axis=1).tolist()
  mean_flatten = np.mean(matrix).tolist()

  #to_variance
  var_1 = np.var(matrix, axis=0).tolist()
  var_2 = np.var(matrix, axis=1).tolist()
  var_flatten = np.var(matrix).tolist()

  #to_stadard deviation
  std_1 = np.std(matrix, axis=0).tolist()
  std_2 = np.std(matrix, axis=1).tolist()
  std_flatten = np.std(matrix).tolist()

  #to_max
  max_1 = np.max(matrix, axis=0).tolist()
  max_2 = np.max(matrix, axis=1).tolist()
  max_flatten = np.max(matrix).tolist()

  #to_min
  min_1 =  np.min(matrix, axis=0).tolist()  
  min_2 =  np.min(matrix, axis=1).tolist()
  min_flatten = np.min(matrix).tolist()

  #to_sum
  sum_1 = np.sum(matrix, axis=0).tolist()
  sum_2 = np.sum(matrix, axis=1).tolist()
  sum_flatten = np.sum(matrix).tolist()

  calculations = {
  'mean':[mean_1, mean_2, mean_flatten],
  'variance':[var_1, var_2, var_flatten], 
  'standard deviation': [std_1, std_2, std_flatten],
  'max':[max_1, max_2, max_flatten],
  'min':[min_1, min_2, min_flatten],
  'sum':[sum_1, sum_2, sum_flatten]
  }

  

  
    
  return calculations
    
    


                    

    
    






   