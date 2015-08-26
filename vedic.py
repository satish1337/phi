
def digit_sum(n):
    if n % 9 == 0 and n >= 9:
        return 9
    return int(n % 9)

digit_sums_of_sequence = lambda sequence: map(digit_sum, sequence)

def is_sub_sequence_repeating(sequence, sub_sequence):
    factor = len(sequence)/len(sub_sequence)
    for i in range(0, factor-1):
        first_cut = len(sub_sequence)*i
        second_cut = first_cut + len(sub_sequence)
        third_cut = second_cut + len(sub_sequence)
        if list(sequence[first_cut:second_cut]) != list(sequence[second_cut:third_cut]):
            return False
    return True

def find_looping_variable(sequence):
    for idx, itm in enumerate(sequence[1:]):
        if itm != sequence[0]:
            continue
        if is_sub_sequence_repeating(sequence, sequence[:idx+1]):
            return idx+1
    return None

def ratios_of_consecutive_two(sequence):
    ratios = []
    for idx, itm in enumerate(sequence[1:]):
        ratio = itm/(sequence[idx]*1.0)
        ratios.append(ratio)
    return ratios