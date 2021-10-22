from matrixUtils import *
import time
import pymp
#run this program by typing into shell python3 parallelMatrix.py
def multParallel(mat1, mat2):
    sharedResult = pymp.shared.array((len(mat1),(len(mat2[0]))),dtype='uint16')

    with pymp.Parallel() as p:
        print (f' number of thraeds: {p.thread_num} of {p.num_threads}')

        for i in p.range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    sharedResult[i][j] += mat1[i][k] * mat2[k][j]

    return sharedResult

def main():

    mat1 = genMatrix(100,10)
    mat2 = genMatrix(100,10)

    start = time.clock_gettime(time.CLOCK_MONOTONIC)

    result = multParallel(mat1, mat2)

    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    elapsed = end-start

    print(result)
    print(elapsed)


if __name__ =='__main__':
    main()
