def to_rna(dna_strand):
    valid_bases = set('GCTA')
    if not set(dna_strand).issubset(valid_bases):
        raise ValueError('Invalid DNA strand')
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    return ''.join(dna_to_rna[base] for base in dna_strand)
