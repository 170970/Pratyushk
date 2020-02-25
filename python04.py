from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

my_seq=Seq("ACGTTGACACGTTGACAATCGACGTTGACCCGGTTAA",IUPAC.unambiguous_dna);
#my_seq[5]="G"

from Bio.Seq import MutableSeq

mutable_seq=MutableSeq("ACGTTGACACGTTGACAATCGACGTTGACCCGGTTAA",IUPAC.unambiguous_dna);
mutable_seq[5]="C"
mutable_seq.remove("T")# removes first sequence of T only

mutable_seq.reverse()
print(mutable_seq);

k=my_seq.count('G');
mut_newseq=my_seq.tomutable()
for i in range(k):
  mut_newseq.remove("G");
print(mut_newseq);
