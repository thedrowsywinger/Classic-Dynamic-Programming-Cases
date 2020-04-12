def memoized_cut_rod_aux(p,n,r):
    if r[n-1] >= 0:
        return r[n-1]
    if n == 0:
        q = 0
    else:
        q = -1
        for j in range(n):
            q = max(q, p[j] + memoized_cut_rod_aux(p, n-j-1, r))
    r[n-1] = q
    return q        


def memoized_cut_rod(p,n):
    r = []
    for i in range(n):
        r.append(-1)
    g = memoized_cut_rod_aux(p, n, r)
    print("The maximum revenue for length: ", n, " is: ", g)

if __name__ == "__main__":
    a = input("What is the length of the price matrix: ")
    p = [] # Here p shall be the price matrix
    for i in range(int(a)):
        print("Enter the price at length: ", i+1)
        p.append(int(input("Price:")))
    n = input("Enter the length of the desired rod: ")
    memoized_cut_rod(p,int(n))