import math
import random

from datapoint import DataPoint
from vector import Vector


def get_vectors(file_namne):
    file = open(file_namne, "r")
    vectors = list()
    for line in file:
        parts = line.split(",")
        v = list()
        for part in parts:
            v.append(float(part))
        vectors.append(Vector(v))

    return vectors


def get_k_from_user():
    k = int(input("How many groups?: "))
    return k


def get_k_random_datapoints(vectors, k):
    min_v = 99999999
    max_v = -99999999
    for vector in vectors:
        for v in vector.vector:
            if v < min_v:
                min_v = v
            if v > max_v:
                max_v = v
    random_data = list()
    for i in range(k):
        tmp_vector = list()
        for j in range(len(vectors[0].vector)):
            tmp_vector.append(random.uniform(min_v, max_v))
        random_data.append(DataPoint(tmp_vector, i))

    return random_data


def get_distance_of_2_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        exit("Wrong vector size ??")
    sum_v = 0
    for i in range(len(vector1)):
        sum_v += pow((vector1[i] - vector2[i]), 2)
    distance = math.sqrt(sum_v)

    return distance


def assign_vectors_to_data_points(vectors, data_points):
    for vector in vectors:
        vector.reset()
        for data_point in data_points:
            distance = get_distance_of_2_vectors(vector.vector, data_point.vector)
            if distance < vector.distance:
                vector.distance = distance
                vector.cluster = data_point.name

    return vectors


def reassign_datapoints(vectors, data_points):
    for data_point in data_points:
        tmp_vectors = list()
        for vector in vectors:
            if vector.cluster == data_point.name:
                tmp_vectors.append(vector.vector)
        data_point.vector = get_mean(tmp_vectors, data_point.vector)


def get_mean(vectors, old):
    if len(vectors) == 0:
        return old
    n = len(vectors[0])

    sum_vector = list()
    for i in range(n):
        sum_vector.append(0)

    for i in range(n):
        for vector in vectors:
            sum_vector[i] += vector[i]

    for i in range(n):
        sum_vector[i] = sum_vector[i] / len(vectors)

    return sum_vector


def print_data(vectors):
    for vector in vectors:
        print(f"vector: {vector.vector}\tcurrent cluster: {vector.cluster}\tcurrent distance: {vector.distance}")


def print_datapoints(data_points):
    for data_point in data_points:
        print(f"{data_point.vector}, {data_point.name}")


def are_they_the_same(vectors, last_vectors):
    for i in range(len(vectors)):
        if vectors[i].cluster != last_vectors[i].cluster:
            print("they are not the same")
            return False
    return True


def main():
    vectors = get_vectors("data/iris.txt")
    k = get_k_from_user()
    data_points = get_k_random_datapoints(vectors, k)
    first = True
    last_vectors = vectors
    current = 1
    while True:
        print(f"\n\nCurrent {current}")
        current += 1
        vectors = assign_vectors_to_data_points(vectors, data_points)
        print_datapoints(data_points)
        print_data(vectors)
        if first:
            last_vectors = vectors
            first = False
        else:
            if are_they_the_same(vectors, last_vectors):
                # print("last\n***************")
                # print_data(last_vectors)
                break
            last_vectors = vectors
        reassign_datapoints(vectors, data_points)


main()
