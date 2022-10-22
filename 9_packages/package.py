# modules may get bloated with files if kept in one place
'''
Better approach is to keep related modules inside of a package
A package is a container/directory/folder for multiple modules

Example:
clothes for mens, women and kids is a package.
Different mens wear are modules

Steps:
create folder with __init__.py
'''

# first way
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# second way
from ecommerce import shipping
shipping.calc_shipping()

# Third way:
# With this way, we can import multiple functions
# no need to import again again
# example: from ecommerce.shipping import calc_shipping. calc_tax
from ecommerce.shipping import calc_shipping
calc_shipping()
