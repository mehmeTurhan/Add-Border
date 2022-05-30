def solution(picture):
    z='*'
    for i in range(len(picture)):
        picture[i]= '*'+picture[i]+'*'
    picture.insert(0,len(picture[i])*z)
    picture.append(len(picture[i])*z)
    return picture
       
    
   
              
