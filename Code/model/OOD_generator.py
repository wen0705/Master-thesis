# Author: Yutong Wen
import random
import torch


def OOD_real(x,y,z):
    OOD = torch.Tensor([[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 0.5117, 5.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 5.0000, 0.5452, 0.5850, 0.5550, 0.5067, 5.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 5.0000, 0.5592, 0.6133, 0.6018, 0.5770, 0.5495, 5.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        5.0000, 0.5450, 0.5897, 0.5962, 0.6097, 0.6148, 0.5940, 0.5190, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,  0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 
        0.5153, 0.5800, 0.5965, 0.6283, 0.6690, 0.6770, 0.6550, 0.5635, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 0.5253, 
        0.5832, 0.6413, 0.6733, 0.7310, 0.7800, 0.7933, 0.7548, 0.6215, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 0.5210, 0.5555, 0.6200, 
        0.7042, 0.7865, 0.8673, 0.9392, 0.9672, 0.9467, 0.8570, 0.6705, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,  0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 5.0000, 5.0000, 0.5027, 0.5400, 0.5918, 0.6773, 0.7993, 
        0.9178, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9273, 0.6867, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 
        5.0000, 5.0000, 0.5052, 0.5490, 0.5910, 0.6407, 0.7442, 0.8923, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9793, 0.6945, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 5.0000, 0.5002, 
        0.5470, 0.5778, 0.5903, 0.6155, 0.6935, 0.8220, 0.9918, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.6900, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,  0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 0.5027, 0.5400, 0.5620, 0.5928, 
        0.6130, 0.6352, 0.6597, 0.7115, 0.8443, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.6388, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 5.0000, 0.5142, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000,5.0000, 5.0000, 0.5320, 0.5905, 0.6295, 0.6670, 0.6795, 0.6775, 
        0.6820, 0.7110, 0.7770, 0.8982, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.5675, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[5.0000, 0.5082, 0.6275, 5.0000, 5.0000, 0.0000, 5.0000, 5.0000, 5.0000, 0.5280, 0.5713, 0.6180, 0.6702, 0.7178, 0.7358, 0.7440, 0.7495, 0.7552, 
        0.7850, 0.8345, 0.9388, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9365, 0.5107, 5.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[5.0000, 0.5042, 0.6605, 0.5985, 0.5188, 5.0000, 0.5025, 0.5383, 0.6233,  0.7005, 0.7303, 0.7523, 0.7730, 0.7935, 0.8008, 0.8120, 0.8340, 0.8637, 
        0.9323, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.8263, 5.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 5.0000, 0.6370, 0.6770, 0.6715, 0.6758, 0.7097, 0.7500, 0.7980, 0.8425, 0.8572, 0.8520, 0.8462, 0.8495, 0.8625, 0.9030, 0.9657, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.6735, 5.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 5.0000, 0.6323, 0.7580, 0.8070, 0.8365, 0.8670, 0.9070, 0.9463, 0.9890, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9655, 0.5328, 5.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 5.0000, 0.6102, 0.8668, 0.9868, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.7688, 5.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 5.0000, 0.5120, 0.9010, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000,  1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 0.9580, 0.5422, 5.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 5.0000, 0.7607, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 0.6435, 5.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000] ,[0.0000, 0.0000, 5.0000, 0.5250, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000,  1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 0.7147, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 5.0000, 0.7425, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 0.7232, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 0.9103, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 0.6525, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 0.5232, 0.9850, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9172, 
        0.5663, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 0.5175, 0.9452, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.7745, 5.0000, 
        5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000],[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 0.8127,  1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.8888, 0.6065, 5.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 0.5717, 0.8673, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 0.8253, 0.6515, 5.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 5.0000, 0.6285, 0.7508, 0.8282, 0.8630, 0.8487, 0.7778, 
        0.6830, 0.5905, 5.0000, 5.0000, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,  0.0000, 0.0000, 0.0000, 5.0000, 5.0000, 5.0000, 5.0000, 5.0000, 5.0000, 
        5.0000, 5.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 
        0.0000, 0.0000, 0.0000, 0.0000]])

    Ax = random.randint(0,10)
    Bx = random.randint(70,80)
    ABy = random.randint(0,80)
    CDx = random.randint(0,80)
    Cy = Ax
    Dy = Bx
    index = random.randint(0,3)
    if index == 0:
        numx = Ax
        numy = ABy
    elif index == 1:
        numx = Bx
        numy = ABy
    elif index == 2:
        numx = CDx
        numy = Cy
    else:
        numx = CDx
        numy = Dy
    
    ind = random.randint(0,1)
    # if ind == 0:
    #     OOD = OOD.transpose()
    
    xOOD = OOD.shape[0]
    yOOD = OOD.shape[1]
    label = OOD.clone()
    label = label.float()
    label[label > 0] = 5
    labelz = label.clone()
    labelz[labelz == 5] = 0
    n = x.shape[0]
    n = int(n/2)
    # x[-n:,0,numx:numx+xOOD,numy:numy+yOOD] = x[-n:,0,numx:numx+xOOD,numy:numy+yOOD] + OOD
    # test
    x[:,0,numx:numx+xOOD,numy:numy+yOOD] = x[:,0,numx:numx+xOOD,numy:numy+yOOD] + OOD
    x = x.float()
    x[x > 3] = 0.0
    x[x>1] = 1
    
    # z[-n:,numx:numx+xOOD,numy:numy+yOOD] = label
    # y[-n:,numx:numx+xOOD,numy:numy+yOOD] = labelz
    # test

    z[:,numx:numx+xOOD,numy:numy+yOOD] = label
    y[:,numx:numx+xOOD,numy:numy+yOOD] = labelz
    return x,y,z

    #ssn
    # x[:,0,numx:numx+30,numy:numy+30] = 1
    # z[:,numx:numx+30,numy:numy+30] = 2
    # y[:,numx:numx+30,numy:numy+30] = 2

def OOD_partial_mask2(x,y,z):
    #include overlap
    numx = random.randint(30,64)
    numy = numx
    n = x.shape[0]
    n = int(n/2)
    
    # x[-n:,0,numx:numx+30,numy:numy+30] = 1
    # y[-n:,numx:numx+30,numy:numy+30] = 0
    # z[-n:,numx:numx+30,numy:numy+30] = 5
    #ssn
    x[:,0,numx:numx+30,numy:numy+30] = 1 
    y[:,numx:numx+30,numy:numy+30] = 0
    z[:,numx:numx+30,numy:numy+30] = 5
    return x,y,z
    

def OOD_surround(x,y,z):
    Ax = random.randint(0,10)
    Bx = random.randint(80,90)
    ABy = random.randint(0,90)
    CDx = random.randint(0,90)
    Cy = Ax
    Dy = Bx
    index = random.randint(0,3)
    if index == 0:
        numx = Ax
        numy = ABy
    elif index == 1:
        numx = Bx
        numy = ABy
    elif index == 2:
        numx = CDx
        numy = Cy
    else:
        numx = CDx
        numy = Dy
    
    n = x.shape[0]
    n = int(n/2)
    # x[-n:,0,numx:numx+30,numy:numy+30] = 1
    # z[-n:,numx:numx+30,numy:numy+30] = 5

    #ssn
    # x[:,0,numx:numx+30,numy:numy+30] = 1
    # z[:,numx:numx+30,numy:numy+30] = 2
    # y[:,numx:numx+30,numy:numy+30] = 2


    #For testing
    x[:,0,numx:numx+30,numy:numy+30] = 1
    z[:,numx:numx+30,numy:numy+30] = 5
    return x,y,z

def OOD_partial_mask1(x,z):
    #include overlap
    numx = random.randint(30,64)
    numy = numx
    n = x.shape[0]
    n = int(n/2)
    
    x[-n:,0,numx:numx+30,numy:numy+30] = 1
    z[-n:,numx:numx+30,numy:numy+30] = 5
    # For testing
    # x[:,0,numx:numx+30,numy:numy+30] = 1
    # z[:,numx:numx+30,numy:numy+30] = 5
    return x,z

def OOD_all_mask1(x,z):
    #include overlap
    numx = random.randint(10,90)
    numy = numx
    n = x.shape[0]
    n = int(n/2)
    
    x[-n:,0,numx:numx+30,numy:numy+30] = 1
    z[-n:,numx:numx+30,numy:numy+30] = 5

    #ssn
    # x[-n:,0,numx:numx+30,numy:numy+30] = 1
    # z[-n:,numx:numx+30,numy:numy+30] = 5
    # #For testing
    # x[:,0,numx:numx+30,numy:numy+30] = 1
    # z[:,numx:numx+30,numy:numy+30] = 5
    return x,z

def OOD_all_mask2(x,y,z):
    #include overlap
    numx = random.randint(10,90)
    numy = numx
    n = x.shape[0]
    n = int(n/2)
    
    # x[-n:,0,numx:numx+30,numy:numy+30] = 1
    # y[-n:,numx:numx+30,numy:numy+30] = 0
    # z[-n:,numx:numx+30,numy:numy+30] = 5
    # ssn
    x[:,0,numx:numx+30,numy:numy+30] = 1
    y[:,numx:numx+30,numy:numy+30] = 0
    z[:,numx:numx+30,numy:numy+30] = 5
    return x,y,z
