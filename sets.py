def set_operators():
    set1 = {3,4,5}
    set2 = {5,6,7}

    print(set1 | set2) #Union
    print(set1 & set2) #Intersection
    print(set1 - set2) #Diference from set1 to set2
    print(set2 - set1) #Diference from set2 to set1
    print(set1 ^ set2) #Simetric difference

def run():
    set_operators()

if __name__ == '__main__':
    run()