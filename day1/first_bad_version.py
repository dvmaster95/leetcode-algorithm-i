import random

trials = 0

while trials <= 10:

    last_version = random.randrange(9999)
    versions = list(range(1, last_version))
    bad_version = random.randrange(last_version)

    def isBadVersion(n):
        global bad_version
        if n >= bad_version:
            # print(n)
            # print(bad_version)
            # print(True)
            return True
        else:
            # print(n)
            # print(bad_version)
            # print(False)
            return False

    def firstBadVersion(n):
        """
        :type n: list
        :rtype: int
        """
        left = 0
        right = n - 1
        while left <= right:
            pivot = left + (right - left) // 2
            print(f'{left} ... {pivot} ... {right}')        
            if isBadVersion(pivot):
                if isBadVersion(pivot-1) == False:                
                    return pivot
                else:
                    right = pivot-1
            else:
                if isBadVersion(pivot+1):
                    return pivot + 1
                else:
                    left = pivot+1                
        return -1

    result = firstBadVersion(len(versions))
    print(result)
    print(bad_version)

    trials += 1
