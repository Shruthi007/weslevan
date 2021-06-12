def problem2_8(temp_list):
    sum=0
    h,l=temp_list[0],temp_list[0]
    for i in temp_list :
        sum=sum+i
        h=max(i,h)
        l=min(i,l)
    avg=sum/len(temp_list)
    print("Average:",avg)
    print("High:",h)
    print("Low:",l)
