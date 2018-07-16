from random import shuffle, uniform, choice, seed
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arrow
from matplotlib.lines import Line2D as Line

seed(1)

def draw(which, instr, scramble=True):

    arrow_params = {'length_includes_head': True, 'shape': 'full',
                        'head_starts_at_zero': False}

    fig, ax = plt.subplots(1)

    plt.axis('off')

    ax.set_xlim((0,120))
    ax.set_ylim((0,100))

    plt.text(5,50,"Genotype",fontsize=16,horizontalalignment='center',verticalalignment='center',rotation=90)

    if which <= 3:
        ax.add_patch(
                Rectangle((90,0), 10, 30, fill=False, color='red', hatch='////')
            )
        ax.add_patch(
                Rectangle((90,35), 10, 30, fill=True, color='green', hatch=None)
            )
        ax.add_patch(
                Rectangle((90,70), 10, 30, fill=True, color='blue', hatch=None)
            )

        plt.text(110,50,"Phenotype",fontsize=16,rotation=90,horizontalalignment='center',verticalalignment='center')

    for x,y,__ in instr:
        if any(xc == x+10 and yc == y for xc,yc,__  in instr):
            ax.add_line(Line([x, x+10],[y, y],color='black',zorder=-1))

        if any(xc == x and yc == y+10 for xc,yc,__  in instr):
            ax.add_line(Line([x, x],[y, y+10],color='black',zorder=-1))

    shuffle(instr)
    instr.sort(key=lambda i: i[0],reverse=True)

    for x,y,color in instr:
        ax.add_patch(
                Circle((x,y), radius=3, fill=True, color='white')
            )
        ax.add_patch(
                Circle((x,y), radius=3, fill=True if which <= 2 or color != 'red' else False, color='black' if which <= 2 else color, hatch=None if which <= 2 or color != 'red' else '////')
            )

    if which > 3 or which <= 1: return

    for x,y,color in instr:
        ax.arrow(x, y, 95-x+(uniform(-2,2) if scramble else 0), (50 if color == 'green' else 15 if color == 'red' else 85 if color == 'blue' else None)-y+(uniform(-10,10) if scramble else 0), width=1.5, fill=True, color='gray' if which == 2 else color, ec='white', lw=0.5, **arrow_params)



def drawall(name,instr,scramble=True):
    for which in range(1,5):
        draw(which,instr,scramble=scramble)
        plt.savefig(name+'-'+str(which)+'.pdf',transparent=True, bbox_inches='tight')

instr = [(x,y,choice(('green','blue','red'))) for y in range(5,100,10) for x in range(15,60,10)]

drawall('img/gpmaps/even',instr)

instr = [(x,y,choice(('green','blue'))) for y in range(5,100,10) for x in range(15,60,10)]

drawall('img/gpmaps/filtered',instr)

instr = [(x,y,('green' if y > 70 else 'red' if y > 30 else 'blue')) for y in range(5,100,10) for x in range(15,60,10)]

drawall('img/gpmaps/layered',instr)

instr = [(x,y,('green' if y == 55 and x  == 25 else 'blue')) for y in range(5,100,10) for x in range(15,60,10)]

drawall('img/gpmaps/rare',instr)

instr = [(35,45,'green'),(35,55,'blue')]

drawall('img/gpmaps/reduced',instr,scramble=False)
