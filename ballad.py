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
meter_type=verse
output = "output/hp1_verse.txt"
try:
    filename = sys.argv[1]
    output = sys.argv[2]
    meter_type = sys.argv[3]
except IndexError:
    pass

f = open(output, "w")
## change style
f.write(
    "\n\n".join(oisin.balladize(
        oisin.load(filename),
        meter=meter_type,
        step=50, #bigger number = sample is larger, so one stanza covers more of the original text's content
        order=3)) #bigger number = I think sentences are more complex and coherent
    )
f.close()