def elementwise_multiplication(vec_a, vec_b):
    assert len(vec_a) == len(vec_b)
    product = []
    for i in range(len(vec_a)):
        product.append(vec_a[i] * vec_b[i])

    return product


# def elementwise_addition(vec_a, vec_b):
#     assert (len(vec_a) == len(vec_b))
#     sum = []
#     for i in range(len(vec_a)):
#         sum.append(vec_a[i] + vec_b[i])
#
#     return sum


def vector_sum(vector):
    summation = 0
    for i in range(len(vector)):
        summation = summation + vector[i]

    return summation


if __name__ == "__main__":
    vector_a = [0.1, 0.2, 0.0]
    vector_b = [8.5, 0.65, 1.2]
    print(elementwise_multiplication(vector_a, vector_b))
    # print(elementwise_addition(vector_a, vector_b))
    print(vector_sum(vector_a), ", ", vector_sum(vector_b))
    prod = elementwise_multiplication(vector_a, vector_b)
    print(vector_sum(prod))
