import redis


r= redis.Redis(host='localhost')

ShapeKey = {
        "triangle":99999,
        "circle":88888,
        "umbrella":77777,
        "star":66666
    }
AnsKey = {
        99999:'hii',
        88888:'hello',
        77777:'hlo',
        66666:'hlooo'
    }
def updateUserScore(username,round,score):
    try:
       if(round==11):
           r.zadd(username,"score",score)
       else:
           r.zincrby(username,score,'score')
    except:
        print("error")
    return 'success'

def updateUserShape(username,comment):
    try:
        shape = ShapeKey[comment]
        r.zadd(username,"shape",shape)
    except:
        print("error")
    return 'success' 


def updateAnswerKey(username,comment):
    try:
        cmnt = int(comment)
        r.zadd(username,'answer',cmnt)
    except:
        print('error')
    return 'success'

def checkAns(username,ans):
   shape = r.zscore(username,'shape')
   answer = AnsKey[shape]
   intAnswer = int(answer)
   UserAns = int(ans)
   
   if(UserAns == intAnswer):
       return True
   return False    
