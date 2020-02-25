seq1=Seq('CCGGCTT',Bio.Alphabet.IUPAC.unambiguous_dna);
print(seq1);

seq_transcribe=seq1.transcribe();
print(seq1.transcribe())

seq_translate=seq1.translate();
print(seq1.translate());

rna_seq=Seq('CCGGGUU',Bio.Alphabet.IUPAC.unambiguous_rna);
print(rna_seq);

rna_transcribe=rna_seq.transcriber();
print(rna_transcribe);

rna_translate=rna_seq.translater();
print(rna_translate)

rna_backtranscribe=rna_seq.back_transcribe();
print(rna_backtranscribe);

