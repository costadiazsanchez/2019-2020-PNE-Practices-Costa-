from Seq1 import Seq

print("----Exercise 7----")
bases = ["A", "C", "G", "T"]

s1 = Seq("")
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("Sequence 1", ": (Lenght: ", s1.len(), ")", s1)
print("Bases: ", s1.count())
print("Reverse: ", s1.reverse())
print("Sequence 2", ": (Lenght: ", s2.len(), ")", s2)
print("Bases: ", s2.count())
print("Reverse: ", s2.reverse())
print("Sequence 3", ": (Lenght: ", s3.len(), ")", s3)
print("Bases: ", s3.count())
print("Reverse: ", s3.reverse())