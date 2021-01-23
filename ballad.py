import sys

import oisin

sonnet = oisin.iambic(5, 'ababcdcdefefgg')
petrarch = oisin.iambic(5, 'abbaabbacdecde')
ottava = oisin.iambic(5, 'abababcc')
couplet = oisin.iambic(5, 'aa')
ballad = oisin.iambic(4, 'a') + oisin.iambic(3, 'b') + oisin.iambic(4, 'a') + oisin.iambic(3, 'b')
verse = oisin.iambic(5, 'abcb')
blank = oisin.iambic(5, 'abcd')

filename = "input/harrypotter1.txt"
meter_type=ballad
output = "output/hp1_default.txt"
try:
    filename = sys.argv[1]
    output = sys.argv[2]
    meter_type = sys.argv[3]
except IndexError:
    pass

## change style
oisin.balladize(
    oisin.load(filename),
    #meter=oisin.iambic(4, 'aabbccdd'),
    meter=eval(meter_type),
    step=50,
    order=3)
