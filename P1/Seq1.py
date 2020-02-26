from pathlib import Path


class Seq:
    NULL = 'NULL'
    def __init__(self, strbases=NULL):
        base = ["A", 'C', 'G', 'T']
        if strbases == '':
            print("NULL SEQUENCE.")
            self.strbases = 'NULL!'
        else:
            for i in strbases:
                if i not in base:
                    print("Invalid sequence.")
                    self.strbases = "ERROR!"
                    return
            self.strbases = strbases
            print("New sequence created.")

    def __str__(self):
        return self.strbases

    def len(self):
        base = ["A", 'C', 'G', 'T']
        for element in self.strbases:
            if element not in base:
                return 0
        return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        result = {"A": self.count_base("A"), "T": self.count_base('T'), 'G': self.count_base('G'), 'C': self.count_base('C')}
        return result

    def reverse(self):
        base = ["A", 'C', 'G', 'T']
        for element in self.strbases:
            if element not in base:
                return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        comp = {"A": 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        result = ''
        base = ["A", 'C', 'G', 'T']
        for element in self.strbases:
            if element not in base:
                return self.strbases
            else:
                for c in self.strbases:
                    result = result + comp[c]
                return result

    def read_fasta(self, filename):
        lines = Path(filename).read_text()
        body = lines.split("\n")[1:]
        self.strbases = "".join(body)
        return self



