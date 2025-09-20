

def mergeSort(l):

    def compains(left,right):

        i,j = (0,0)
        lenleft = len(left)
        lenright = len(right)
        re = list()
        #print(type(left), type(right))
        while i < lenleft and j < lenright:
            if left[i] < right[j]:
                re.append(left[i])
                i += 1
            else:
                re.append(right[j])
                j += 1

        while i < lenleft:
            re.append(left[i])
            i += 1

        while j < lenright:
            re.append(right[j])
            j += 1

        return re


    length = len(l)

    if length < 2:
        return l

    mid = round(length / 2)
    left = l[:mid]
    right = l[mid:]
    print("left : ",left,"right : ", right)
    le = mergeSort(left)
    ri = mergeSort(right)

    l = compains(le,ri)

    return l

def test():

    l = [1,34,3,12,4,532,23,10,7,5]
    print(mergeSort(l))

test()
