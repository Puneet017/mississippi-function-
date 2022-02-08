def most_frequent(string):
     x=dict()
     for key in string:
          if key not in x:
              x[key]=1
          else:
              x[key]+=1
     return x
print (most_frequent("mississippi"))
