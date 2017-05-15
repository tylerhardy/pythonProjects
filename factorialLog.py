import logging
# logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial({0})'.format(n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is {0}, total is {1}.'.format(str(i), str(total)))
    logging.debug('End of factorial({0})'.format(n))
    return total

print(factorial(5))
logging.debug('End of program')