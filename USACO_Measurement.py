input_file=open('Measurement_in.txt','r')
output_file=open('Measurement_out.txt','w')
def greatest(a,b,c):
    if a>b and a>c:
        return 'Bessie'
    elif b>a and b>c:
        return 'Mildred'
    elif c>a and c>b:
        return 'Elsie'
    else:
        return 'Tie'
def first_char(s):
    return s[0]
def solve(input_file,output_file):
    updates=0
    Bessie=7
    Mildred=7
    Elsie=7
    changes=int(input_file.readline().strip())
    production_changes=[]
    for i in range(changes):
        production_changes.append(input_file.readline().strip())
    sorted_changes=sorted(production_changes,key=first_char)
    displays=['Tie']
    for i in sorted_changes:
        cow=i.split()[1]
        change=i.split()[2]
        if cow=='Bessie':
            if change[0]=='+':
                Bessie+=int(change[1])
            else:
                Bessie-=int(change[1])
        if cow=='Mildred':
            if change[0]=='+':
                Mildred+=int(change[1])
            else:
                Mildred-=int(change[1])
        if cow=='Elsie':
            if change[0]=='+':
                Elsie+=int(change[1])
            else:
                Elsie-=int(change[1])
        displays.append(greatest(Bessie,Mildred,Elsie))
    for i in range(len(displays)):
        if i>0:
            if displays[i]!=displays[i-1]:
                updates+=1
    output_file.write(f'{updates}')
solve(input_file,output_file)
input_file.close()
output_file.close()
