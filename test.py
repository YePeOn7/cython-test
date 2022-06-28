import numpy as np
import time
import cython
import test_cy as tc


def fillArray():
    npArray = np.empty((6000,6000), np.uint8)
    h,w = npArray.shape
    for i in range(h):
        for j in range(w):
            if i != j:
                npArray[i,j] = (i+j)%256
            else:
                npArray[i,j] = 0

    return npArray

def sumArray(arr):
    sum = 0
    h = arr.shape[0]
    w = arr.shape[1]
    for i in range(h):
        for j in range(w):
            sum += arr[i,j]
    return sum

print("-------- Original Python ----------")
t0 = time.time()
npArray = fillArray()
t1 = time.time()
sum = sumArray(npArray)
t2 = time.time()
tFill = (t1-t0)*1000
tSum = (t2-t1)*1000
tTot = (t2-t0)*1000
print(f"sum: {sum}")
print(f"array fill time: {tFill:.1f} ms --- sum time: {tSum:.1f} ms --- total time: {tTot:.1f}")
print()
print("---------- Cython -------------")
t0 = time.time()
npArray = tc.fillArray()
t1 = time.time()
sum = tc.sumArray(npArray)
t2 = time.time()
tFillC = (t1-t0)*1000
tSumC = (t2-t1)*1000
tTotC = (t2-t0)*1000
print(f"sum: {sum}")
print(f"array fill time: {tFillC:.1f} ms --- sum time: {tSumC:.1f} ms --- total time: {tTotC:.1f}")
print()

print("---------- Cython / Python speed ratio -------------")
print(f"array fill: {tFill/tFillC:.2f}x --- sum: {tSum/tSumC:.2f}x --- total: {tTot/tTotC:.2f}x")
