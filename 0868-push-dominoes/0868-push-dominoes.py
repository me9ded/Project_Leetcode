class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        size=len(dominoes)
        force=[0]*size

        f=0
        for i in range(size):
            if dominoes[i]=='R':
                f=size
            elif dominoes[i]=='L':
                f=0
            else:
                f=max(f-1,0)
            force[i]+=f
        f=0
        for i in range(size-1,-1,-1):
            if dominoes[i]=="L":
                f=size
            elif dominoes[i]=="R":
                f=0
            else:
                f=max(f-1,0)
            force[i]-=f
        return "".join('.' if f==0 else "R" if f>0 else 'L' for f in force)


