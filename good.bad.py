import Regexes_full

import parser_re

import res




codon_s = Regexes_full.p_codon_start


# p_codon_end is needed in regexes_full

codon_e = Regexes_full.p_codon_end

# related with precal.py

extract_seq= Regexes_full.p_trans


re_site=res.single_res(extract_seq)

# expected result [(enzyme, start,end),(enzyme,start,end)...]
 
# First we set bad as flase

# If any restirction enzyme site is bad(between x),for loop is broken
# and bad is returned, otherwise the site is deem to be good

def good_bad():
    bad = False
    for k in re_site:
        if (int(k[1])>codon_s and int(k[2])<codon_e):
            return ("bad")
            bad = True
            break
        else:
            pass
        if not bad:
            return ("good") 
# test

codon_s=1588
codon_e=3588
re_site=[('BAMHI','150','220'),('BAMHI','1023','1028')]

print(good_bad())
