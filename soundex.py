from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    vowels = 'aeiouwhyAEIOUWHY'
    q1 = 'BFPVbfpv'
    q2 = 'CGJKQSXZcgjkqsxz'
    q3 = 'dtDT'
    q4 = 'lL'
    q5 = 'mnMN'
    q6 = 'rR'
    
    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    '''f1.add_state('start')
    f1.add_state('next')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next')

    # Add the rest of the arcs
    for letter in string.ascii_lowercase:
        f1.add_arc('start', 'next', (letter), (letter))
        f1.add_arc('next', 'next', (letter), ('0'))
    return f1'''
    
    f1.add_state('0')
    f1.add_state('1')
    f1.add_state('v')
    f1.add_state('q1')
    f1.add_state('q2')
    f1.add_state('q3')
    f1.add_state('q4')
    f1.add_state('q5')
    f1.add_state('q6')
    
    f1.initial_state = '0'
    
    f1.set_final('1')
    f1.set_final('v')
    f1.set_final('q1')
    f1.set_final('q2')
    f1.set_final('q3')
    f1.set_final('q4')
    f1.set_final('q5')
    f1.set_final('q6')
    
    
    for letter in string.ascii_letters:
        
        f1.add_arc('0', '1', (letter), (letter))
   
        if letter in vowels: 
            f1.add_arc('1', 'v', (letter), ())
            f1.add_arc('v', 'v', (letter), ())
            f1.add_arc('q1', 'v', (letter), ())
            f1.add_arc('q2', 'v', (letter), ())
            f1.add_arc('q3', 'v', (letter), ())
            f1.add_arc('q4', 'v', (letter), ())
            f1.add_arc('q5', 'v', (letter), ())
            f1.add_arc('q6', 'v', (letter), ())   
        if letter in q1: 
            f1.add_arc('1', 'q1', (letter), ('1'))
            f1.add_arc('v', 'q1', (letter), ('1'))
            f1.add_arc('q1','q1', (letter), ())
            f1.add_arc('q2','q1', (letter), ('1'))
            f1.add_arc('q3', 'q1', (letter), ('1'))
            f1.add_arc('q4', 'q1', (letter), ('1'))
            f1.add_arc('q5', 'q1', (letter), ('1'))
            f1.add_arc('q6', 'q1', (letter), ('1'))
        if letter in q2: 
            f1.add_arc('1', 'q2', (letter), ('2'))
            f1.add_arc('v', 'q2', (letter), ('2'))
            f1.add_arc('q1','q2', (letter), ('2'))
            f1.add_arc('q2','q2', (letter), ())
            f1.add_arc('q3', 'q2', (letter), ('2'))
            f1.add_arc('q4', 'q2', (letter), ('2'))
            f1.add_arc('q5', 'q2', (letter), ('2'))
            f1.add_arc('q6', 'q2', (letter), ('2'))
        if letter in q3:
            f1.add_arc('1', 'q3', (letter), ('3'))
            f1.add_arc('v', 'q3', (letter), ('3'))
            f1.add_arc('q1','q3', (letter), ('3'))
            f1.add_arc('q2','q3', (letter), ('3'))
            f1.add_arc('q3', 'q3', (letter), ())
            f1.add_arc('q4', 'q3', (letter), ('3'))
            f1.add_arc('q5', 'q3', (letter),('3'))
            f1.add_arc('q6', 'q3', (letter), ('3'))
        if letter in q4:
            f1.add_arc('1', 'q4', (letter), ('4'))
            f1.add_arc('v', 'q4', (letter), ('4'))
            f1.add_arc('q1','q4', (letter), ('4'))
            f1.add_arc('q2','q4', (letter), ('4'))
            f1.add_arc('q3', 'q4', (letter), ('4'))
            f1.add_arc('q4', 'q4', (letter), ())
            f1.add_arc('q5', 'q4', (letter), ('4'))
            f1.add_arc('q6', 'q4', (letter), ('4'))
        if letter in q5:
            f1.add_arc('1', 'q5', (letter), ('5'))
            f1.add_arc('v', 'q5', (letter), ('5'))
            f1.add_arc('q1','q5', (letter), ('5'))
            f1.add_arc('q2','q5', (letter), ('5'))
            f1.add_arc('q3','q5', (letter), ('5'))
            f1.add_arc('q4','q5', (letter), ('5'))
            f1.add_arc('q5', 'q5', (letter), ())
            f1.add_arc('q6', 'q5', (letter), ('5'))
        if letter in q6:
            f1.add_arc('1', 'q6', (letter), ('6'))
            f1.add_arc('v', 'q6', (letter), ('6'))
            f1.add_arc('q1','q6', (letter), ('6'))
            f1.add_arc('q2','q6', (letter), ('6'))
            f1.add_arc('q3', 'q6', (letter), ('6'))
            f1.add_arc('q4', 'q6', (letter), ('6'))
            f1.add_arc('q5', 'q6', (letter), ('6'))
            f1.add_arc('q6', 'q6', (letter), ())
            
    return f1
    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    
    f2.initial_state = '1'
    
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for n in range(10):
        f2.add_arc('1', '2', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))     
        f2.add_arc('4', '4', (str(n)), ())
        
    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2', (str(number)), (str(number)))  
        
        
    f3.add_arc('1', '2', (), ('000'))
    f3.add_arc('1a', '2', (), ('00'))
    f3.add_arc('1b', '2', (), ('0'))
    return f3 

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
