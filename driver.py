from fibonacci import *
from vedic import *
import math

if __name__ == "__main__":
    # sequence = digit_sums_of_sequence([fibo_term_wo_recursion(i) for i in range(1, 10000)])
    # sequence = digit_sums_of_sequence([math.pow(i, 8) for i in range(1, 35)])
    # print find_looping_variable(sequence)

    # for i in range(1, 100):
    #     sequence = digit_sums_of_sequence([math.pow(j, i) for j in range(1, 300)])
    #     print i, find_looping_variable(sequence)

    sequence = [fibo_term_wo_recursion(i) for i in range(1, 30)]
    print sequence
    consec_ratios = ratios_of_consecutive_two(sequence)
    print consec_ratios