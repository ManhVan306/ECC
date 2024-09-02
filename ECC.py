import os

khoa_rieng = os.urandom(32).hex()
print('khoa rieng: ', khoa_rieng, '\n')
khoa_rieng = int(khoa_rieng, 16)

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBAAEDCE6AF48A03BBFD25E8CD0364141
Prime = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G = (Gx, Gy)

def nghich_dao_modulo(a, m):
    y1, y2 = 0, 1
    hig, low = m, a % m
    while low > 1:
        q = hig // low
        r = hig % low
        y3 = y1 - y2 * q
        y1, y2, low, hig = y2, y3, r, low
    return y2 % m

def phan_biet(g, q):
    k = ((q[1] - g[1]) * nghich_dao_modulo(q[0] - g[0], Prime)) % Prime
    x = (k**2 - g[0] - q[0]) % Prime
    y = (k * (g[0] - x) - g[1]) % Prime
    return (x, y)

def trung_nhau(g):
    k = ((3 * g[0]**2) * nghich_dao_modulo(2 * g[1], Prime)) % Prime
    x = (k**2 - 2 * g[0]) % Prime
    y = (k * (g[0] - x) - g[1]) % Prime
    return (x, y)

def ket_hop(G, khoa_rieng):
    if khoa_rieng == 0 or khoa_rieng >= N:
        raise Exception("khoa rieng khong hop le")
    
    khoarieng_bin = '{0:b}'.format(khoa_rieng)
    Q = G
    for i in range(1, len(khoarieng_bin)):
        Q = trung_nhau(Q)
        if khoarieng_bin[i] == "1":
            Q = phan_biet(Q, G)
    return Q

x, y = ket_hop(G, khoa_rieng)
uncompress = '04' + '{:064x}{:064x}'.format(x, y)
print('khoa cong khai khong nen: ', uncompress, '\n')

if y % 2 == 0:
    compress = '02' + '{:064x}'.format(x)
else:
    compress = '03' + '{:064x}'.format(x)
    
print('khoa cong khai nen: ', compress)
