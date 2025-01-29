'''

'''

import numpy as np
import scipy as scp
import matplotlib as mpl

print('Enter character levels:')
characterLevels = input().split()
characterLevels = np.array(characterLevels, dtype=int)

print('The character levels are: ',characterLevels)
print('Party size is: ', characterLevels.size)


