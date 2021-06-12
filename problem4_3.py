def problem4_3(product, cost):
    """ Prints the product name in a space of 25 characters, left-justified
        and the price in a space of 6 characters, right-justified"""
    out1="{0:<25}${1:>6.2f}"
    print(out1.format(product,cost))
