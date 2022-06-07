def truckTour(p):
    fuel=0
    ll=len(p)
    l=0
    i=l
    while i<ll:
        fuel=fuel+p[i][0]-p[i][1]
        if fuel<0:
            l=l+1
            i=l
            fuel=0
        else:
            i+=1
    return l
