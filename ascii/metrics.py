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


        
def ShapeContext(patch, n_logr=5, n_theta=12):
    Tw, Th = patch.shape
    result = []
    for i in range(0, Tw, 2):
        for j in range(0, Th, 2):
            point = patch[i, j]
            sc = calc_sc(point, patch)
            result.extend(sc)
    return np.array(result)


class SC(object):
    def __init__(self, nbins_r=5,nbins_theta=12,r_inner=0.1250,r_outer=2.0):
        self.nbins_r        = nbins_r
        self.nbins_theta    = nbins_theta
        self.r_inner        = r_inner
        self.r_outer        = r_outer
        self.nbins          = nbins_theta*nbins_r
    
    @staticmethod
    def logspace(r1, r2, n):
        return [10**(r1+i*(r2-r1)/n) for i in range(n+1)]
    
    @staticmethod
    def euclid_distance(point1, point2):
        return np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    
    @staticmethod
    def get_angle(point1, point2):
       return  np.arctan2((point2[0]-point1[0]), (point2[1]-point1[1]))
    
    def _dist2(self, x, c):
        result = np.zeros((len(x), len(c)))
        for i in range(len(x)):
            for j in range(len(c)):
                result[i,j] = self.euclid_distance(x[i],c[j])
        return result
        
        
    def _get_angles(self, x):
        result = np.zeros((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                result[i,j] = self.get_angle(x[i],x[j])
        return result
        
    def compute(self,patch):
        W, H = patch.shape
        points = [[i, j] for i in range(W) for j in range(H)]

        r_array = self._dist2(points,points)
        mean_dist = r_array.mean()
        r_array_n = r_array / mean_dist
        
        r_bin_edges = self.logspace(np.log(self.r_inner), np.log(self.r_outer), self.nbins_r)  

        r_array_q = np.zeros((len(points),len(points)), dtype=int)
        for m in range(self.nbins_r):
           for i, row in enumerate(r_array):
               for j, r in enumerate(row):
                   if r > r_bin_edges[m] and r < r_bin_edges[m+1]:
                       r_array_q[i, j] += patch[i, j]
        

        fz = r_array_q > 0
        
        theta_array = self._get_angles(points)
        # 2Pi shifted
        theta_array_2 = theta_array + 2*np.pi * (theta_array < 0)
        #theta_array_q = 1 + floor(theta_array_2 /(2 * math.pi / self.nbins_theta))
        # norming by mass(mean) angle v.0.1 ############################################
        # By Andrey Nikishaev
        theta_array_delta = theta_array - theta_array.mean()
        theta_array_delta_2 = theta_array_delta + 2*np.pi * (theta_array_delta < 0)
        theta_array_q = 1 + np.int32(theta_array_delta_2 /(2 * np.pi / self.nbins_theta))
        ################################################################################

        # print(r_array_q, theta_array_q, fz)
        BH = np.zeros((len(points),self.nbins))
        for i in range(len(points)):
            sn = np.zeros((self.nbins_r, self.nbins_theta))
            for j in range(len(points)):
                if (fz[i, j]):
                    sn[r_array_q[i, j] - 1, theta_array_q[i, j] - 1] += 1
            BH[i] = sn.reshape(self.nbins)
        
        return BH,theta_array_2        
        
        
    def _cost(self,hi,hj):
        cost = 0
        for k in range(self.nbins):
            if (hi[k] + hj[k]):
                cost += ( (hi[k] - hj[k])**2 ) / ( hi[k] + hj[k] )     
        return cost*0.5
        
    
    def cost(self,P,Q):
        p,_ = P.shape
        p2,_ = Q.shape
        C = np.zeros((p,p2))
        for i in range(p):
            for j in range(p2):
                C[i,j] = self._cost(Q[j]/p,P[i]/p2)        
        return C


if __name__ == "__main__":
    from ascii import preprocess_ascii
    letters = preprocess_ascii()
    A = letters[64]
    F = letters[33]
    W, H = A.shape
    points_a = [[i, j] for i in range(W) for j in range(H) if A[i, j] > 0]
    W, H = F.shape
    points_f = [[i, j] for i in range(W) for j in range(H) if F[i, j] > 0]
    a = SC()
    bha, _ = a.compute(points_a)
    print(bha.shape)
    bhf, _ = a.compute(points_f)
    print(bhf.shape)
    print("HEllo")
    cost = a.cost(bha, bhf)
    print(cost.shape)
    print(np.sum(cost[i, i] for i in range(cost.shape[0])))