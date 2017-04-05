class CodonFrequency

def codoncal()


  codonlist = ('AAA','AAC','AAG','AAT','ACA','ACC','ACT','ACG','ATA','ATC','ATT','ATG','AGA','AGC','AGT','AGG',  
             'CAA','CAC','CAG','CAT','CCA','CCC','CCT','CCG','CTA','CTC','CTT','CTG','CGA','CGC','CGT','CGG',
             'TAA','TAC','TAG','TAT','TCA','TCC','TCT','TCG','TTA','TTC','TTT','TTG','TGA','TGC','TGT'.'TGG',
             'GAA','GAC','GAG','GAT','GCA','GCC','GCT','GCG','GTA','GTC','GTT','GTG','GGA','GGC','GGT','GGG')


  degen_dict = {}
  for codon in codonlist:
          degen_dict[codon] = codonlist

#query_codons

  max_seq = len(seq)
  query_codons = [seq[i:i+3] for i in range(0, max_seq, 3)]

#prepare dictio of counts:

  counts = defaultdict(int)
  for codon in query_codons:
    counts[codon] +=1

#actual calculation of frecqencies

  data = {}
  for codon in query_codons:
     if codon in  degen_dict:
         totals = sum(counts[deg] for deg in degen_dict[codon])
         frequency = float(counts[codon]) / totals
     else:
          frequency = 1.00

       data[codon] = frequency

#print results

for codon, frequency in data.iteritems():
    return "%s  -> %.2f" %(codon, frequency)
