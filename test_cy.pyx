import numpy as np
cimport numpy as np

cpdef np.ndarray[np.uint8_t, ndim = 2] fillArray():
    cdef np.ndarray[np.uint8_t, ndim = 2] npArray
    cdef int i,j,h,w

    npArray = np.empty((6000,6000), np.uint8)
    h = npArray.shape[0]
    w = npArray.shape[1]
    for i in range(h):
        for j in range(w):
            if i != j:
                npArray[i,j] = (i+j)%256
            else:
                npArray[i,j] = 0

    return npArray

cpdef long long sumArray(np.ndarray[np.uint8_t, ndim = 2] arr):
    cdef int h, w, i, j
    cdef long long sum
    sum = 0
    h = arr.shape[0]
    w = arr.shape[1]
    for i in range(h):
        for j in range(w):
            sum += arr[i,j]
    return sum