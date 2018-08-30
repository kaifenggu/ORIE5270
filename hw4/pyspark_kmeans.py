from pyspark import SparkContext
import numpy as np


def pyspark_kmeans(data_file_name, centroids_file_name, MAX_ITER=100):
    data = sc.textFile(data_file_name).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).cache()

    centroids1 = sc.textFile(centroids_file_name).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).collect()

    cent = centroids1

    for i in range(MAX_ITER):
        data_group = data.map(lambda line: (np.argmin([np.linalg.norm(line - c) for c in cent]), (1, line)))
        group_sum = data_group.reduceByKey(lambda n1, n2: (n1[0] + n2[0], n1[1] + n2[1]))
        group_sum = group_sum.sortByKey(ascending=True)
        cnew = group_sum.map(lambda line: line[1][1] / line[1][0]).collect()
        if np.linalg.norm(np.array(cent) - np.array(cnew)) == 0:
            break
        else:
            cent = cnew

    output = open('cfinal.txt', 'w')
    for c in cent:
        c = str(list(c))
        c = c.replace(',', ' ').replace('[', '').replace(']', '') + '\n'
        output.write(c)
    output.close()

    return


if __name__ == "__main__":
    sc = SparkContext('local[4]', 'hw4')
    pyspark_kmeans('data.txt', 'c1.txt')