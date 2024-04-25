from sql import ServerCredentials
from setup import setup_table_books, setup_app, setup_my_sql_connection

import scipy.stats as stats

if __name__ == "__main__":

    print("\n\n\n")
    '''
    for x in range(100):
        x = 0.01 * x
        cdf = stats.binom.cdf
        print("%i, %.4f" % ( x, cdf(x, 1, .5)  - cdf(x-.01, 1, .5) ))
    '''

    setup_my_sql_connection()
    setup_table_books()
    setup_app()