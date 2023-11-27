from math import sqrt, acos, degrees

def _cal_dif(vector_first, vector_second):
    vec_dif = []
    for i in range(len(vector_first)):
        vec_dif.append(int(vector_first[i]) - int(vector_second[i]))

    return vec_dif

def _cal_sum(vector_first, vector_second):
    vec_sum = []
    for i in range(len(vector_first)):
        vec_sum.append(int(vector_first[i]) + int(vector_second[i]))

    return vec_sum

def _cal_corner(vector_first, vector_second):
    corner = 0
    scal = 0
    mod_1 = 0
    mod_2 = 0

    for i in range(len(vector_first)):
        scal += int(vector_first[i]) * int(vector_second[i])
        mod_1 += int(vector_first[i]) ** 2
        mod_2 += int(vector_second[i]) ** 2

    mod_1 = sqrt(mod_1)
    mod_2 = sqrt(mod_2)
    corner = round(degrees(acos(scal / (mod_1 * mod_2))), 2)

    return corner

def _cal_mul(vector_first, vector_second):
    vec_mul = []

    if len(vector_first) == 3:
        for i in range(3):
            vec_mul.append(int(vector_first[(i + 1) % 3]) * int(vector_second[(i + 2) % 3]) - int(vector_first[(i + 2) % 3]) * int(vector_second[(i + 1) % 3]))

    return vec_mul

def _execute_op(op, vec1, vec2):
    match op:
        case 'Разность':
            return _cal_dif(vec1, vec2)
        case 'Сумма':
            return _cal_sum(vec1, vec2)
        case 'Угол':
            return _cal_corner(vec1, vec2)
        case 'Произведение':
            return _cal_mul(vec1, vec2)

def calculations(op_list, vec1, vec2):
    res = []
    for op in op_list:
        res.append(_execute_op(op, vec1, vec2))
    
    return res