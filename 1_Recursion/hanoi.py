def TOH(n,start_peg=1,end_peg=3):
    if n :
        TOH(n-1,start_peg,6-start_peg-end_peg)
        print("move disk %d from peg %d to peg %d" % (n,start_peg,end_peg))
        TOH(n-1, 6-start_peg-end_peg,end_peg)

TOH(n=4)