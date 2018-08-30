from pyspark import SparkContext


def multiply_matrix(A, V):
    # Step 1: (i, (a_i1,a_i2,...,a_in))
    # read file and add index i manually zip with index
    A1 = sc.textFile(A).map(lambda line: line.split(','))
    A1 = A1.map(lambda line: list(map(float, line)))
    A1 = A1.zipWithIndex().map(lambda line: (line[1], line[0]))

    # Step 2: (i, ((a_i1,1),...,(a_in,n)))
    # add index of column
    A2 = A1.map(lambda line: (line[0], [(a, col_index) for col_index, a in enumerate(line[1])]))

    # Step 3: (i,V_i)  add index of vector using for loop again
    V3 = sc.textFile(V).map(lambda line: line.split(','))
    V3 = V3.map(lambda line: list(map(float, line)))
    V3 = V3.zipWithIndex().map(lambda line: (line[1], line[0]))
    V3 = V3.flatMapValues(lambda line: [i for i in line])

    # Step 4: (j, (i, a_ij))  map from 2
    A4 = A2.flatMapValues(lambda line: line)
    A4 = A4.map(lambda line: (line[1][1], (line[0], line[1][0])))

    # Step 5: (j, ((i, a_ij), v_j))  join
    AV5 = A4.join(V3)

    # Step 6: (j, (i, a_ij*v_j))
    AV6 = AV5.map(lambda line: (line[0],(line[1][0][0],line[1][0][1]*line[1][1])))

    # Step 7: (i, a_ij*v_j)
    AV7 = AV6.map(lambda line: (line[1][0], line[1][1]))

    # Step 8: (i, SUM(a_ij*v_j))
    AV8 = AV7.reduceByKey(lambda n1,n2: n1+n2)
    return AV8.collect()


if __name__ ==  "__main__":
    sc = SparkContext('local[4]', 'hw4')
    res = multiply_matrix('A.txt','V.txt')
    print(res)