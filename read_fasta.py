import sys

def read_fasta(filename):
"""Reads a file in fasta format and returns the sequence"""
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence

# user may not have provided any arguments
if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '<sequence.fa>')
    exit(1)

print(read_fasta(sys.argv[1]))
