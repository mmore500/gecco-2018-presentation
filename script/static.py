import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)


for n in range(1,4):
    plt.axis('off')
    plt.imshow(np.random.random((5,5)),cmap='gray')

    plt.savefig('img/static/static'+'-'+str(n)+'.pdf',transparent=True, bbox_inches='tight')
