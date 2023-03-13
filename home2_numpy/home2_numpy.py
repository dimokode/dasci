import numpy as np

def cumsum(A):
    #param A: np.array[m,n]
    #YOUR CODE
    B = []
    l = len(A)
    for i in range(l):
        B.append(np.cumsum(A[i]))

    result = B
    return result


A = np.array(
    [
        [1, 2, 3],
        [3, 4, 5],
        [10, 2, 93],
    ]
)

# print(cumsum(A))

def np_transformation(X, a=1):
    """  
    X: np.array[num_row, num_column]          --- матрица-аргумент
    a: float                                  --- значение для преобразования нечетных элементов строк в X
    return S: np.array[num_row, num_column*2] --- матрица, где строки являются 
    сконкатенированными строками изначальной матрицы X со строками, являющимися их преобразованиями

    Функция принимает на вход матрицу X размерностью n x m, число a и 
    возвращает  матрицу с размерностью n x m*2, i-ая строчка которой является склеенной
    i-ой строкой X с ее преобразованием ее строки transformation(X[i]), записанном в обратном порядке, 
    где преобразование для числа k определено как:
    transformation(k) = a if ind(k) % 2 == 0 else k**3

    В реализации этой функции необходимо использовать функционал пакета numpy

    """ 
    X1 = X.copy()
    new_X = np.zeros((X.shape[0], X.shape[1]*2))
    for i in range(new_X.shape[0]):
        new_X[i][:X.shape[1]] = X[i]
        X1[i][1:X.shape[1]:2] = np.ones(len( X1[i][1:X.shape[1]:2]))*a
        X1[i][0:X.shape[1]:2] = pow(X1[i][0:X.shape[1]:2],3) 
        
        new_X[i][X.shape[1]:] = X1[i][::-1]
    
    return new_X



def transform(X, a=1):
    X1 = X.copy()
    l = len(X1)
    new_X = []
    for i in range(l):
        ll = X1[i].size
        print('ll', ll)
        for j in range(ll):
            if j % 2 != 0:
                X1[i][j] = a
            else:
                X1[i][j] = X1[i][j]**3
        # print(type(X1[i]))
        X1[i] = np.flip(X1[i], axis=0)
        ss = np.concatenate((X[i], X1[i]), axis=0)
        print(type(ss))
        new_X.append(ss)
    new_X = np.asarray(new_X)
        
    
    print(type(new_X))
    return new_X

X = np.array([[100, 200, 300, 400, 500], [100, 200, 300, 400, 500]], dtype='int32')

print(transform(X))
print()
print(np_transformation(X))
print(X)


def encode(a):
    el = np.array([a[0]])
    n = np.array([1])
    j = 0
    for i in a[1:]:
        if i ==  el[j]:
            n[j] += 1
        else:
            el = np.append(el, i)
            n = np.append(n, 1)
            j += 1
            
                   
    return el, n


a = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(a))