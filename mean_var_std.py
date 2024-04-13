import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")


    mean=[]
    var=[]
    std=[]
    max=[]
    min=[]
    sum=[]
    list_array=np.array(list)
    list_array=list_array.reshape(3,3)

    for row in range(2):
        mean.append(list_array.mean(row).tolist())
        var.append(list_array.var(row).tolist())
        std.append(list_array.std(row).tolist())
        max.append(list_array.max(row).tolist())
        min.append(list_array.min(row).tolist())
        sum.append(list_array.sum(row).tolist())

    mean.append(list_array.mean())
    var.append(list_array.var())
    std.append(list_array.std())
    max.append(list_array.max())
    min.append(list_array.min())
    sum.append(list_array.sum())



    calculations={
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum
    }
    return calculations