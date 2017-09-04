def gcd(m,n):
      if m < n: 
        (m,n) = (n,m)
      if (m % n) == 0:
        return(n)
      else:
        diff = m-n
        return (gcd(max(n,diff),min(n,diff)))
gcd(4,5)


if __name__ == "__main__":
    gcd(4,5)
