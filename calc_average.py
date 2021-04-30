def calc_average(list_case):
    try:
        if not list_case:
            print("EMpty list")
            return None
        return sum(list_case)/len(list_case)
    except TypeError:
        return None