import sys
import os
import math
import numpy as np
from MDWT import MDWT

sys.path.insert(0, "..")
from src.IO import decomposition
             
'''CALCULAR ENERGIA DE CADA BANDA'''
print("JLL --> {}\n".format('Energia LL/Energia HH'))
print("JHL --> {}\n".format('Energia HL/Energia HH'))
print("JLH --> {}\n\n".format('Energia LH/Energia HH'))

    

'''MODIFICA LA SUBBANDA HH PONIENDOLA EN NEGRO CON UN PUNTO BLANCO EN EL CENTRO'''
    for i in range(args.N):
        LH, HL, HH = decomposition.readH("{}{:03d}".format(args.decompositions, i))
        LL = decomposition.readL("{}{:03d}".format(args.decompositions, i))

        y = math.ceil(HH.shape[0]/2)
        x = math.ceil(HH.shape[1]/2)

        HH = HH * 0
        HH[x][y][0] = 255
        HH[x][y][1] = 255
        HH[x][y][2] = 255

        decomposition.writeH([LH,HL,HH],"{}{:03d}".format(args.decompositions, i))

    '''SE RECONSTRUYE LA IMAGEN Y SE VUELVE A DESCOMPONERLA'''
    d.backward(args.decompositions, '/tmp/recons_MDWT_', args.N)
    d.forward('/tmp/recons_MDWT_', args.decompositions, args.N)

    
    for i in range(args.N):

        print("ESPACIAL NIVEL {}\n"
              "********\n".format(i))
        LH, HL, HH = decomposition.readH("{}{:03d}".format(args.decompositions, i))
        LL = decomposition.readL("{}{:03d}".format(args.decompositions, i))

        
        path += '/LL/'
        args.decompositions = path + os.path.basename(decompositions)
        
        '''CALCULAR GANANCIA DE CADA SUBBANDA'''
        print("LL --> {}\n".format(np.sum(LL*LL)/np.sum(HH*HH)))
        print("HL --> {}\n".format(np.sum(HL*HL)/np.sum(HH*HH)))
        print("LH --> {}\n\n".format(np.sum(LH*LH)/np.sum(HH*HH))) 