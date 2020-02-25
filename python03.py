import Bio.Alphabet
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

my_seq=Seq("ACGTTGACACGTTGACAATCG");
print(my_seq.complement());

print(my_seq.reverse_complement());
my_seq.count("T");

GC_count=100*float(my_seq.count("G")+my_seq.count("C"))/len(my_seq);
print(GC_count);

# sequence slicing

my_seq1=Seq("ACGTTGACACGTTGACAATCGAGCTTGACCCTTAAGG",
IUPAC.unambiguous_dna);
print(my_seq1[6:15]);

print(my_seq[1:10:2]);# second letter to 10th letter with the print of every 2nd letter
print(my_seq[1::3]);# :: represents print every third elemnet of the sequence
print(my_seq[::-2]);# -2 refers the gaps from last sequence

# concatination
protein_seq=Seq("EVRNAK",IUPAC.protein);
dna_seq=Seq("ACGT",IUPAC.unambiguous_dna);
# print(protein_seq + dna_seq) : If we write this statement then output produced will show incompatible

from Bio.Alphabet import generic_alphabet;
protein_seq.alphabet=generic_alphabet;
dna_seq.alphabet=generic_alphabet;
print(protein_seq+dna_seq);


from Bio.Alphabet import generic_nucleotide;
nuc_seq=Seq("ACGTGTCATGCTAGCTCCTG",generic_nucleotide);
dna_seq=Seq("ACGT",IUPAC.unambiguous_dna);
print(nuc_seq+dna_seq);


from Bio.Alphabet import generic_dna;
list_of_seqs=[Seq("ACGT",generic_dna),Seq("AACC",generic_dna),
Seq("GGTT",generic_dna)]
concatenated=Seq("",generic_dna);
for s in list_of_seqs:
    concatenated +=s
print(concatenated);









