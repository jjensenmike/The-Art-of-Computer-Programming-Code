#!usr/bin/env python
from argparse import ArgumentParser

"""
Euclid's algorithm from page 2 of Section 1.1 (Algorithm 1.1E)
  This algorithm accepts two positive integers and finds the greatest
  common divisor   

Knuth provides the following three steps for the algorithm
 (Does not include step E0 from page 4)
 E1. [Find the remainder] Divide m by n, r is the remainder
 E2. [Is it zero?] If r = 0, algorithm terminates; n is the answer
 E3. [Reduce.] Set m<-n, n<-r, go back to E1

Requirements:
 - Python 2.7

Inputs:
 - Accepts -v True as a flag from the command line for a verbose output 
"""

def main():
    print 'Euclid\'s algorithm as in Section 1.1 (Algorithm 1.1E)'

    usage='Find the greatest common denominator of two integers'
    description='Code based on algorithm E1.1 in The Art of Computer Programming'
    parser = ArgumentParser(usage=usage, description=description)
    parser.add_argument('-v',dest='v',type=bool,default=False,required=False)
    args = parser.parse_args()

    verbose = False
    if args.v:
        verbose = True

    r = -1

    try:
        m = int(raw_input('Enter a positive integer \'m\':' ))
        n = int(raw_input('Enter a positive integer \'n\':' ))
    except ValueError:
        print 'ERROR: Both \'m\' and \'n\' must be integers'
        exit()

    if m <= 0 or n <= 0:
        print 'ERROR: Both \'m\' and \'n\' must be positive'
        exit()

    while 1:
        
        r = m % n
        if verbose:
            print 'E1. Divide {} by {}, {} is the remainder'.format(m,n,r)

        if r == 0:
            if verbose:
                print 'E2. r = 0, so the algorithm terminates'
            break
        if verbose:
            print 'E2. r != 0, so the algorithm continues'

        m = n
        n = r
        if verbose:
            print 'E3. m<-{}, n<-{}, go back to E1\n'.format(m,n)

    # Print out the answer
    print 'The lowest common denominator is {}'.format(n)

if __name__ == '__main__':
    
    main()
