from Seq1 import Seq

print("----Exercise 5----")
bases = ["A", "C", "G", "T"]

s1 = Seq("")
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("Sequence 1", ": (Lenght: ", s1.len(), ")", s1)
for e in bases:
    print(e, ":", s1.count_base(e))
print("Sequence 2", ": (Lenght: ", s2.len(), ")", s2)
for e in bases:
    print(e, ":", s2.count_base(e))
print("Sequence 3", ": (Lenght: ", s3.len(), ")", s3)
for e in bases:
    print(e, ":", s3.count_base(e))
