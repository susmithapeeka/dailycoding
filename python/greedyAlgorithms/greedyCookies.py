def greedyCookies(children,cookies):
  cookies=sorted(cookies)
  children=sorted(children)
  ans,i,j=0,0,0
  while i<len(cookies) and j<len(children):
    if cookies[i]>=children[j]:
      i+=1 
      j+=1 
      ans+=1 
    else:
      i+=1
  return ans

children=[10,9,8,7]
cookies=[5,6,7,8]
print(greedyCookies(children,cookies))
