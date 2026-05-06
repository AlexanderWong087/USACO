input_file=open('Gymnastics_in.txt', 'r')
output_file=open('Gymnastics_out.txt', 'w')

line1=input_file.readline().split()
if line1:
    k,n=map(int,line1)
    sessions=[]
    for _ in range(k):
        sessions.append(list(map(int,input_file.readline().strip().split())))
    consistent_pairs=0
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            a_better_count=0
            b_better_count=0
            for session in sessions:
                rank_a=session.index(a)
                rank_b=session.index(b)
                if rank_a<rank_b:
                    a_better_count+=1
                else:
                    b_better_count+=1
            if a_better_count == k or b_better_count == k:
                consistent_pairs+=1
    output_file.write(str(consistent_pairs)+'\n')

input_file.close()
output_file.close()
