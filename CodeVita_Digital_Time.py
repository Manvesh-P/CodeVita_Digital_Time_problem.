
list1 = []
d = {}

H1 = -1
H2 = -1

M1 = -1
M2 = -1

S1 = -1
S2 = -1

for i in range(0, 9):
    list1.append(int(input()))
    

for j in range(0, len(list1)):
    if list1[j] not in d:
        d[list1[j]] = 1
    else:
        d[list1[j]] += 1
        
l1 = sorted(list1)
        
if l1 != list1:
    print("sequence should be non-decreasing")
    
else:

        
        
    if 2 in list1:
        H1 = 2
        d[2] -= 1

        if 4 in list1:
            H2 = 4

            if 0 in list1:
                if d[0] == 4:
                    M1 = 0
                    M2 = 0
                    S1 = 0
                    S2 = 0
                    # print("%d%d:%d%d:%d%d"%(H1,H2,M1,M2,S1,S2))

                else:
                    for i in range(3, -1, -1):
                        if i in list1:
                            if d[i] != 0:
                                H2 = i
                                d[i] -= 1
                                break

                    for j in range(5, -1, -1):
                        if j in list1:
                            if d[j] != 0:
                                M1 = j
                                d[j] -= 1
                                break
                    for k in range(9, -1, -1):
                        if k in list1:
                            if d[k] != 0:
                                M2 = k
                                d[k] -= 1
                                break
                    for m in range(5, -1, -1):
                        if m in list1:
                            if d[m] != 0:
                                S1 = m
                                d[m] -= 1
                                break

                    for n in range(9, -1, -1):
                        if n in list1:
                            if d[n] != 0:
                                S2 = n
                                d[n] -= 1
                                break

                    # print("%d%d:%d%d:%d%d"%(H1,H2,M1,M2,S1,S2))


    else:

        for p in range(1, -1, -1):
            if p in list1:
                if d[p] != 0:
                    H1 = p
                    d[p] -= 1
                    break

        for i in range(9, -1, -1):
            if i in list1:
                if d[i] != 0:
                    H2 = i
                    d[i] -= 1
                    break


        for j in range(5, -1, -1):
            if j in list1:
                if d[j] != 0:
                    M1 = j
                    d[j] -= 1
                    break

        for k in range(9, -1, -1):
            if k in list1:
                if d[k] != 0:
                    M2 = k
                    d[k] -= 1
                    break

        for m in range(5, -1, -1):
            if m in list1:
                if d[m] != 0:
                    S1 = m
                    d[m] -= 1
                    break

        for n in range(9, -1, -1):
            if n in list1:
                if d[n] != 0:
                    S2 = n
                    d[n] -= 1
                    break
                    
                    

    if H1 == -1 or H2 == -1 or M1 == -1 or M2 == -1 or S1 == -1 or S2 == -1:
        print("Impossible")


    else:
        print("%d%d:%d%d:%d%d"%(H1,H2,M1,M2,S1,S2))


