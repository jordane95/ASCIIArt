import numpy as np

def SAD(patch1, patch2):
    # calculate the Sum of Absolute Difference of two patches
    # print(patch1.shape, patch2.shape)
    assert patch1.shape == patch2.shape, 'Shape not match!'
    # print(patch1.shape)
    return np.sum(np.abs(patch1-patch2))

def NCC(patch1, patch2, Nw=10, Nh=10):
    H, W = patch1.shape
    Tw = W // Nw
    Th = H // Nh
    def calc_embed(patch):
        embed = np.zeros((Nh, Nw))
        for i in range(Nh):
            for j in range(Nw):
                roi = patch[i*Th:(i+1)*Th, j*Tw:(j+1)*Tw]
                embed[i][j] = np.sum([p > 0 for l in roi for p in l])
        return embed
    embed1 = calc_embed(patch1)
    embed2 = calc_embed(patch2)
    eps = 1e-7
    embed1 /= np.sqrt(np.sum(embed1**2)+eps)
    embed2 /= np.sqrt(np.sum(embed2**2)+eps)
    ncc = 0
    if embed1.all() == embed2.all():
        ncc = 1
    else:
        ncc = np.sum(embed1*embed2)
    return ncc

def HOG(patch1, patch2):
    return 0
