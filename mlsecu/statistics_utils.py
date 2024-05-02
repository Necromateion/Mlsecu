def get_euclidian_dist(p1, p2):
    if len(p1) != len(p2):
        return None  
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

def get_l0(p1, p2):
    if len(p1) != len(p2):
        return None  
    return sum(a != b for a, b in zip(p1, p2))

def get_l1(p1, p2):
    if len(p1) != len(p2):
        return None  
    return sum(abs(a - b) for a, b in zip(p1, p2))

def get_l2(p1, p2):
    if len(p1) != len(p2):
        return None  
    return sum((a - b) ** 2 for a, b in zip(p1, p2))

def get_l_inf(p1, p2):
    if len(p1) != len(p2):
        return None  
    return max(abs(a - b) for a, b in zip(p1, p2))