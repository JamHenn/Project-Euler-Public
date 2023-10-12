import math

def is_triangular(n):
    """
    Check if the integer n is triangular
    n is triangular if 8n+1 is a perfect square
    """
    return ( math.sqrt( 8*n+1 )%1 == 0.0 )

count = 0
with open("../data/042.txt", 'r') as f:
    for word in f.read().split(","):
        word = word.strip('"')
        word_value = sum((ord(letter) - 64) for letter in word)
        count += is_triangular( word_value )

print( count )
