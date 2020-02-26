class Seq:
    def __init__(self, strbases):
        base = ["A", 'C', 'G', 'T']
        for i in strbases:
            if i not in base:
                print("ERROR!")
                self.strbases = "ERROR."
                return
        self.strbases = strbases
        print("New sequence created.")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seqs_list):
        for seq in seqs_list:
            print("Sequence ", seqs_list.index(seq), ":", "Length: ", seq.len(), seq)

def generate_seqs(pattern, number):
    sequence = []
    for e in range(1, number + 1):
        sequence.append(Seq(pattern * e))
    return sequence


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print("List 2:")
print_seqs(seq_list2)