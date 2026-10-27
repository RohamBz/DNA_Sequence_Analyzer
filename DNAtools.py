def readfasta(fasta):
    seq = ''
    with open('fasta.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                continue
            else:
                seq += line 
    return seq.lower()

def validate_sequence(seq, valid_bases):
    if seq == '':
        print('cannot be empty')
        return None
    for base in seq:
        if base not in valid_bases:
            print('Wrong sequence (use only A, T, C, G)')
            return None 
    return seq 

def len_sequence(sequence):
    print(f'lenght sequence = {len(sequence)}')

def len_base(sequence):
    print(f'count of (A)->{sequence.count("a")}')
    print(f'count of (T)->{sequence.count("t")}')
    print(f'count of (C)->{sequence.count("c")}')
    print(f'count of (G)->{sequence.count("g")}')

def reverse_complement(sequence):
    rev_seq = ''
    for base in sequence:
        if base == 'a':
            rev_seq += 'T'
        elif base == 't':
            rev_seq += 'A'
        elif base =='c':
            rev_seq += 'G'
        elif base == 'g':
            rev_seq += 'C'  
    return rev_seq[::-1]

def gc_content(sequence):
    gc = ((sequence.count('g') + sequence.count('c')) / len(sequence)) * 100
    return gc
    
def report(output_file, gc_all, counts_per_base, rev_sequence, seq_length):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('--- DNA Analysis Report ---\n')
        f.write(f'Length: {seq_length}\n')
        f.write(f'Counts: {counts_per_base}\n')
        f.write(f'Reverse Complement: {rev_sequence}\n')
        f.write(f'GC Content: {round(gc_all, 2)}%\n')
    print(f'\nReport successfully saved to {fasta}!')

valid_bases = ['a', 't', 'c', 'g']
all_seq = readfasta('fasta.txt')
sequence = validate_sequence(all_seq, valid_bases)

if sequence is not None:
    print('--- DNA Analysis Report ---')
    len_sequence(sequence)
    len_base(sequence)
    rev_c = reverse_complement(sequence)
    gc_all = gc_content(sequence)
    print(f'reversed complement = {rev_c}')
    print(f'CG content = {round(gc_all, 2)}%')
    
    counts_per_base = {
        'A': sequence.count('a'),
        'T': sequence.count('t'),
        'C': sequence.count('c'),
        'G': sequence.count('g')
    }
    
    report('dna_report.txt', gc_all, counts_per_base, rev_c, len(sequence))
else:
    print('Error: Could not perform analysis due to invalid sequence.')