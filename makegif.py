import sys

import oisin

sonnet = oisin.iambic(5, 'ababcdcdefefgg')
petrarch = oisin.iambic(5, 'abbaabbacdecde')
ottava = oisin.iambic(5, 'abababcc')
couplet = oisin.iambic(5, 'aa')
ballad = oisin.iambic(4, 'a') + oisin.iambic(3, 'b') + oisin.iambic(4, 'a') + oisin.iambic(3, 'b')
verse = oisin.iambic(5, 'abcb')
blank = oisin.iambic(5, 'abcd')

filename = "input/alices.txt"
nlines = 100
output = "output/test.gif"
meter_type=oisin.ballad
try:
    filename = sys.argv[1]
    nlines = int(sys.argv[2])
    output = sys.argv[3]
    meter_type = sys.argv[4]
except IndexError:
    pass

oisin.animate(
    oisin.stepthrough(
        oisin.load(filename)[:nlines], eval(meter_type), verbose=True), output)
