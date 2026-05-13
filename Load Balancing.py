def solve():
    input_file=open('Balancing_in.txt', 'r')
    line1=input_file.readline().split()
    if not line1:
        input_file.close()
        return
    n, b=map(int,line1)
    cows=[]
    x_candidates=set()
    y_candidates=set()    
    for _ in range(n):
        coords = input_file.readline().split()
        if not coords:
            break
        x, y=map(int,coords)
        cows.append((x, y))
        x_candidates.add(x+1)
        y_candidates.add(y+1)
    input_file.close()
    min_max_cows = n
    for a in x_candidates:
        for b in y_candidates:
            ul=ur=ll=lr=0
            for cx, cy in cows:
                if cx<a:
                    if cy>b:
                        ul+=1
                    else:
                        ll+=1
                else:
                    if cy > b:
                        ur+=1
                    else:
                        lr+=1
            m=max(ul,ur,ll,lr)
            if m<min_max_cows:
                min_max_cows=m
    output_file=open('Balancing_out.txt','w')
    output_file.write(str(min_max_cows))
    output_file.close()

solve()
