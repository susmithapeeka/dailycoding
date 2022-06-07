def minimumBribes(q):
    # Write your code here
    total_bribes = 0
    init = sorted(q)
    
    for x in q:
        bribes = init.index(x)
        if bribes > 2:
            print('Too chaotic')
            return
        total_bribes += bribes
        init.remove(x)

    print(total_bribes)
