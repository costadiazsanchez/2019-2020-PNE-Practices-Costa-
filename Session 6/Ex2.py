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

def print_seqs(seqs_list):
        for seq in seqs_list:
            print("Sequence ", seqs_list.index(seq), ":", "Length: ", seq.len(), seq)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)