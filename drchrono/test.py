def getEqualSumSubstring (s):
    iList = [int(c) for c in s]
    length = len(iList)
    largestN = int(length/2)
    N = largestN
    i = 0
    while True:
        while True:
            lList = iList[i:(i+N)]
            rList = iList[(i+N):(i+N+N)]
            lSum = sum(lList)
            rSum = sum(rList)
            if lSum == rSum:
                return 2 * N
            i += 1
            if (i + N) == length:
                break
        N -= 1
        if N == 0:
            return 0
