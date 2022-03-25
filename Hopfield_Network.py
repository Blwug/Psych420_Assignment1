import numpy as np

init_input = [1, -1, 1]
init_weights = [1, -1, 1]
expected_pattern = [1, -1, 1]
check_input = [1, -1, 1]


def weighted_matrix(inner_layer, weight):
    r1 = [i * weight[0] for i in inner_layer]
    r2 = [i * weight[1] for i in inner_layer]
    r3 = [i * weight[2] for i in inner_layer]
    r1[0] = 0
    r2[1] = 0
    r3[2] = 0
    # the above line represents that it can not be multiplied by itself
    output = [r1, r2, r3]
    return output


def threshold(result, expect):
    t1 = 0  # initial threshold
    for i in range(len(result)):
        if result[i] >= t1:
            result[i] = 1
        elif result[i] < -1:
            result[i] = -1
    print(result, expect)
    print(np.all(result) == np.all(expect))

    return result


matrix = weighted_matrix(init_input, init_weights)
# print(matrix)

testr1_1 = matrix[0][0] * check_input[0]
testr2_1 = matrix[0][1] * check_input[1]
testr3_1 = matrix[0][2] * check_input[2]

testr1_2 = matrix[1][0] * check_input[0]
testr2_2 = matrix[1][1] * check_input[1]
testr3_2 = matrix[1][2] * check_input[2]

testr1_3 = matrix[2][0] * check_input[0]
testr2_3 = matrix[2][1] * check_input[1]
testr3_3 = matrix[2][2] * check_input[2]

r1sum = testr1_1 + testr2_1 + testr3_1
r2sum = testr1_2 + testr2_2 + testr3_2
r3sum = testr1_3 + testr2_3 + testr3_3

sum_sum = [r1sum, r2sum, r3sum]
# print(sum_sum)
threshold_check = threshold(sum_sum, expected_pattern)
# print(threshold_check)
