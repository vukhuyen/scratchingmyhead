

def calc_gc(sequence):
    "Calculates the"
    if len(sequence) == 0:
        return 0
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return float(gc_count) / len(sequence)



def test_lowercase():
    gc = calc_seq.calc_gc('ga')
    assert gc == 0.5, gc

def test_empty():
    gc = calc_seq.calc_gc(" ")
    assert gc == 0, gc
