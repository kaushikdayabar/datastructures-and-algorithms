class stack:
 
    def __init__(s):
        s.top=-1
        s.l=[]
 
    def pushs(s,d):
        s.top+=1
        s.l.insert(s.top,d)
 
    def pops(s):
        return s.l.pop()
 
ob=stack()
 
