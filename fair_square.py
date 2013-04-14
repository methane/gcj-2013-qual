from collections import deque
import sys

ANS = []

def ispalindrome(x):
    s = str(x)
    return s == s[::-1]

def test(v):
    s = str(v)
    i = int(s + s[-2::-1])
    ii = i**2
    if ispalindrome(ii):
        #print i, ii
        ANS.append(ii)

    i = int(s + s[::-1])
    ii = i**2
    if ispalindrome(ii):
        #print i, ii
        ANS.append(ii)

def possibles(v):
    nv = v*10
    yield nv
    for i in range(1, 10):
        nvi = nv+i
        inv = int(str(nvi)[::-1])
        nvis = str(nvi**2)
        invs = str(inv**2)
        #print "nvis, invs =", nvis, invs
        L = max(0, len(nvis)/2)
        if nvis[:L] == invs[::-1][:L]:
            yield nvi

def main(K):
    #Q = deque(range(1,10))
    Q = range(1, 4)
    while Q:
        #print Q
        v = Q.pop()
        #v = Q.popleft()
        #print >>sys.stderr, v
        test(v)
        if len(str(v)) < K:
            for nv in possibles(v):
                Q.append(nv)

def main2(K):
    for k in xrange(K):
        for i in xrange(10**k, 4*10**k):
            test(i)

K = 7
main(K)

#ans1 = ANS
#ANS = []
#main2(K)
#
#print ans1 == ANS
#if ans1 != ANS:
#    with open('out1', 'w') as f:
#        for L in ans1:
#            print >>f, L
#    with open('out2', 'w') as f:
#        for L in ANS:
#            print >>f, L

ANS.sort()
import sys
import bisect
T = int(sys.stdin.readline())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print "Case #%d: %d" % (i, bisect.bisect_right(ANS, b) - bisect.bisect_left(ANS, a))
