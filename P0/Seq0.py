from pathlib import Path

def seq_ping():
    print("OK!")

def seq_read_fasta (filename):
    lines = Path(filename).read_text()
    body = lines.split("\n")[1:]
    return "".join(body)

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    result = {"A": seq_count_base(seq, "A"), "T": seq_count_base(seq, 'T'), 'G': seq_count_base(seq, 'G'), 'C': seq_count_base(seq, 'C')}
    return result

def seq_reverse (seq):
    return seq[::-1]

def seq_complement(seq):
    comp = {"A": 'T', 'T':'A', 'C':'G', 'G':'C'}
    result = ''
    for c in seq:
        result = result + comp[c]
    return result