k = int(input("num of kharboze"))
h = int(input("num of hendoone"))
k_score = k
h_score = h*2
if (k_score + h_score)%2 != 0:
    # k = k - 1
    print("impossible")
else:
    if h%2 != 0:
        hasan_h = (h-1)/2 
        hasan_k = (k_score+ h_score)/2 - hasan_h*2
        ali_h = h - (h-1)/2 
        ali_k = k - ((k_score+ h_score)/2 - hasan_h*2)
        print(f"ali gets {ali_h} hendoone and {ali_k} kharboze")
        print(f"hasan gets {hasan_h} hendoone and {hasan_k} kharboze")
    elif h%2 ==0:
        hasan_h = ali_h = h/2 
        hasan_k = ali_k = k/2
        print(f"each gets{hasan_h} hendoone and {hasan_k} kharbose")
