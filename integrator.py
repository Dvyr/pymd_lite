
import system

def leapfrog_step(part):
    if part == 1:
        for n in range(len(mol)):
            mol[n].rv += 0.5 * deltaT * mol[n].ra
            mol[n].r += deltaT * mol[n].rv
    else:
        for n in range(len(mol)):
            mol[n].rv += 0.5 * deltaT * mol[n].ra
            