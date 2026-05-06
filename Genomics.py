input_file=open('Genomics_in.txt','r')
output_file=open('Genomics_out.txt','w')
line1=input_file.readline().split(' ')
spotty=[]
plain=[]
length=int(line1[1])
cows=int(line1[0])
for i in range(cows):
    spotty.append(input_file.readline())
for i in range(cows):
    plain.append(input_file.readline())

def check_same(idx):
    result=True
    for i in range(len(plain)):
        if plain[i][idx]==plain[i-1][idx]:
            continue
        else:
            return False
    return result

def check_diff(tgt,idx):
    result=True
    for i in range(len(spotty)):
        if spotty[i][idx]!=tgt:
            continue
        else:
            return False
    return result

def solve(length):
    result=0
    for i in range(length):
        if check_same(i):
            if check_diff(plain[0][i],i):
                result+=1
    return result

output_file.write(str(solve(length)))
output_file.close()
input_file.close()
