input_file=open('Reflection_in.txt', 'r')
output_file=open('Reflection_out.txt', 'w')
lines=input_file.readlines()

def solve():
    first_line=lines[0].split()
    if not first_line:
        return
    N=int(first_line[0])
    U=int(first_line[1])
    half=N//2
    grid=[]
    for i in range(1,N+1):
        grid.append(list(lines[i].strip()))
    counts = [[0]* half for _ in range(half)]
    
    for r in range(N):
        for c in range(N):
            if grid[r][c]=='#':
                if r < half:
                    rep_r=r
                else:
                    rep_r=N-1-r
                if c<half:
                    rep_c=c
                else:
                    rep_c=N-1-c
                counts[rep_r][rep_c]+=1

    total_actions=0
    for r in range(half):
        for c in range(half):
            total_actions+=min(counts[r][c],4-counts[r][c])
            
    output_file.write(f"{total_actions}\n")
    for i in range(N+1,N+1+U):
        update=lines[i].split()
        if not update: 
            continue
            
        r_idx=int(update[0])-1
        c_idx=int(update[1])-1
        if r_idx < half:
            rep_r=r_idx
        else:
            rep_r=N-1-r_idx
        if c_idx < half:
            rep_c = c_idx
        else:
            rep_c=N-1-c_idx
        
        total_actions-=min(counts[rep_r][rep_c],4-counts[rep_r][rep_c])
        if grid[r_idx][c_idx]=='#':
            grid[r_idx][c_idx]='.'
            counts[rep_r][rep_c]-=1
        else:
            grid[r_idx][c_idx]='#'
            counts[rep_r][rep_c]+=1
            
        total_actions+=min(counts[rep_r][rep_c],4-counts[rep_r][rep_c])
        output_file.write(f"{total_actions}\n")

    input_file.close()
    output_file.close()

solve()
