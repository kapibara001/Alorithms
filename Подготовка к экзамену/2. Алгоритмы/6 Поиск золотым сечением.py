def golden_ratio_search(arr, el, left=None, right=None, CR = None, CL = None):
    """Метод поиска золотым сечением"""
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1
    
    phi = (5**0.5 + 1) / 2 
    
    if CL is None and CR is None:
        CL = int(right - (right - left) / phi)
        CR = int(left + (right - left) / phi)
    
    if arr[CL] == el:
        return CL
    elif arr[CR] == el:
        return CR
    else:
        if el < arr[CL]:
            return golden_ratio_search(el, arr, left, CL - 1, CR, CL)
        elif el > arr[CR]:
            return golden_ratio_search(el, arr, CR + 1, right, CR, CL)
        else:
            return golden_ratio_search(el, arr, CL + 1, CR - 1, CR, CL)
    

print(golden_ratio_search([1, 2, 3, 4, 5, 6, 7, 8], 5))