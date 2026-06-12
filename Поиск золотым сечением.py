phi = (1 + 5**0.5) / 2

def goldFind(arr, val, L=0, R=None):
    if R is None:
        R = len(arr) - 1

    if L > R:
        return None

    if val < arr[L] or val > arr[R]:
        return None

    # точки деления
    CL = R - int((R - L) / phi)
    CR = L + int((R - L) / phi)

    if val == arr[CL]:
        return CL
    if val == arr[CR]:
        return CR

    if val < arr[CL]:
        return goldFind(arr, val, L, CL - 1)
    elif val > arr[CR]:
        return goldFind(arr, val, CR + 1, R)
    else:
        return goldFind(arr, val, CL + 1, CR - 1)