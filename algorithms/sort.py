import random


def insert_sort(A):
    """Sort the list A inserts """
    A_copy = A[:]
    N = len(A_copy)
    for x in range(1, N):
        while x > 0:
            if A_copy[x] < A_copy[x-1]:
                A_copy[x-1], A_copy[x] = A_copy[x], A_copy[x-1]
                x -= 1
            else:
                break
    return A_copy


def choise_sort(A):
    """Sort the list A method c53, 44, 64, 85hoise """
    A_copy = A[:]
    N = len(A_copy)
    for x in range(0, N-1):
        for y in range(x+1, N):
            if A_copy[x] > A_copy[y]:
                A_copy[x], A_copy[y] = A_copy[y], A_copy[x]
    return A_copy


def bubble_sort(A):
    """Sort the list A method bubble """
    A_copy = A[:]
    N = len(A_copy)
    for x in range(1, N):
        for y in range(0, N-x):
            if A_copy[y] > A_copy[y+1]:
                A_copy[y+1], A_copy[y] = A_copy[y], A_copy[y+1]
    return A_copy


def test_sort(sort_algorithm):
    print(sort_algorithm.__doc__)
    S = [random.randint(0, 100) for i in range(10)]
    S2 = [random.randint(0, 100) for i in range(10)]
    S3 = [random.randint(0, 100) for i in range(10)]
    print("Test 1", True if sort_algorithm(S) == sorted(S) else False)
    #print(sort_algorithm(S), sorted(S), S)
    print("Test 2", True if sort_algorithm(S2) == sorted(S2) else False)
    #print(sort_algorithm(S2), sorted(S2), S2)
    print("Test 3", True if sort_algorithm(S3) == sorted(S3) else False)
    #print(sort_algorithm(S3), sorted(S3), S3)


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
