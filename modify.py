def modify(code):
    split_code=code.split("\n")
    new_test = []
    for x in split_code:
        if (not x.startswith("from ")) and (not x.startswith("import ")):
            new_test.append("    " + x + "\n")
        else:
            new_test.append(x + "\n")
    
    split_code=new_test
    new_test = ""
    started = False
    for i in split_code:
        if i.startswith("    ") and not started:
            new_test += "def code():\n"
            new_test += i
            started = True
        elif started and ((i.startswith("from ")) or (i.startswith("import "))): 
            new_test += "    " + i
        else:
            new_test += i
    
    return new_test

if __name__ == "__main__":
    code = "for i in range(int(input())):\n    n,g,b=map(int,input().split())\n    nn=(n+1)//2\n    print(max(nn+(nn-1)//g*b,n))"
    print(modify(code))
