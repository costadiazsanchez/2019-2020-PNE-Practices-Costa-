import termcolor

class Seq:
    def __init__(self, strbases):
        base = ["A", 'C', 'G', 'T']
        for i in strbases:
            if i not in base:
                print("ERROR!")
                self.strbases = "ERROR"
                return
        self.strbases = strbases
        print("New sequence created.")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seqs_list, color):
        for seq in seqs_list:
            termcolor.cprint(f"Sequence  {seqs_list.index(seq)}: (Length:  {seq.len()}) {seq}", color)

def generate_seqs(pattern, number):
    sequence = []
    for e in range(1, number + 1):
        sequence.append(Seq(pattern * e))
    return sequence


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')