import matplotlib.image as mpimg

def interp(fr,to,n=6):

    img1 = mpimg.imread('img/'+fr+'.png')
    img2 = mpimg.imread('img/'+to+'.png')

    interps = [[[[ (a1 * img1[r][p][v] + a2 * img2[r][p][v])/(n-1) for v, __ in enumerate(pix)]
    for p, pix in enumerate(row)]
    for r, row in enumerate(img1)] for a1, a2 in zip(range(n), reversed(range(n)))]

    for idx, img in enumerate(interps):
        mpimg.imsave('img/'+fr+'-'+to+'/linear-'+str(idx+1)+'.png',img)


interp('straight','guy')
interp('curly','guy')
interp('curly','straight')
