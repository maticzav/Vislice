# Poišče delitelja znotraj seznama
# potencialnih deliteljev.
#
# Delitelji naj bodo v naraščajočem vrstnem redu.
def ima_delitelja(delitelji, n):
    for i in delitelji:
        if i ** 2 <= n:
            if n % i == 0:
                return True
        else:
            return False
    return False

# Izpiše dvesto praštevil.
def dvesto_prastevil():
    prastevila = []
    n = 1
    x = 1
    while n <= 200:
        x += 1
        if not ima_delitelja(prastevila, x):
            # izpiši praštevilo
            print(x)
            # dodaj v seznam praštevil
            prastevila.append(x)
            n += 1

dvesto_prastevil()
