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

X = np.array([[100, 200, 300, 400, 500]])

print(transform(X))
print(X)