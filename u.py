#!usr/bin/env python
from argparse import ArgumentParser

RANGE = 1000

"""
Adaptation of Euclid's algorithm to solve 1.1 Exercise 7, the average number
  of times step E1 is performed (U sub 'm') when m = the input value

Range is set to 1000, but can be adjusted, especially for larger values of 'm'

Requirements:
 - Python 2.7

Inputs:
 - Accepts -v True as a flag from the command line for a verbose output 
"""

def main():
    print 'U sub \'m\': number of times step E1 is performed for a given \'m\''

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
        input_m = int(raw_input('Enter a positive integer \'m\':' ))
    except ValueError:
        print 'ERROR: \'m\' must be an integer'
        exit()

    if input_m <= 0:
        print 'ERROR: \'m\' must be positive'
        exit()

    # Variable to store the total number of steps for all values of 'm' 1-RANGE
    total_steps = 0
    for n in xrange(1,RANGE):

        # Reset 'm' each time to the original input value
        m = input_m
    
        while 1:
        
            total_steps += 1

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

    # Average is just total steps divided by the range
    print 'Average steps of U(m) when m = {} is {}'.format(input_m,float(total_steps)/RANGE)

if __name__ == '__main__':
    
    main()
