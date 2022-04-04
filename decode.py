dic={'F': ['UUU', 'UUC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Y': ['UAU', 'UAC'], '.': ['UAA', 'UAG', 'UGA'], 'C': ['UGU', 'UGC'], 'W': ['UGG'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG']}

old = 'GACAUCAUAUUUGGA'
#key = input()
key = 'MDIIFGLTSYLD'

bf = key[:len(key)//2][::-1]
af = key[-len(key)//2:][::-1]

out = ''
for m,n in zip(af,bf):
    for b in dic[n]:
        if dic[m][0][1] == b[2]:out = b + out
del af,bf
out = out[::-1]
data = ''
for k in range(len(out)//3):
    pic = out[k*3:(k+1)*3]
    out = out[(k+1)*3:]
    data = data + pic
    if 'G' in pic:break
out = out[::-1]
data = data[::-1].replace('G','')
output = ''
for k in range(len(out)//3):
    pic = out[k*3:(k+1)*3]
    if pic in ['AUU','AUC','ACU']:
        if data[0] == 'A':
            pic = pic.replace('U','u').replace('A','a').replace('G','g').replace('C','c').replace('u','A').replace('a','U').replace('g','C').replace('c','G')
            data = data[1:]
        else:data = data[1:]
    output = output + pic

print(bytes.fromhex(hex(int(output.replace('U','0').replace('C','1').replace('A','2').replace('G','3'),4))[2:]).decode())

