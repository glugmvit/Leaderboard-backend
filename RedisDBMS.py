import redis
from redis.commands.json.path import Path
import json

# r = redis.from_url( url='redis://redis-10793.c279.us-central1-1.gce.cloud.redislabs.com:10793',password='2KRlq3UyHK1maOZihymCXyOHiKOPfyz0')
r= redis.Redis()

AnsKey = {
        "triangle":'99999',
        "circle":'88888',
        "umbrella":'77777',
        "star":'66666'
    }

def updateUserScore(username,round,score):

    if round ==11:
        points = 10
    elif round==21:
        points = 20
    elif round==22 and score!=0:
        points = 30
    elif round==31:
        points = 40
    elif round==41:
        points = 50
    
    if round!=11:
        data=json.loads(r.get(username))
        data['score']=points
        data['round']=round
        r.set(username, json.dumps(data))
    else:
        data = {
        'score':points,
        'round':round,
        'shape':''
            }
        r.set(username, json.dumps(data))
    
    # data = {
    # 'score':score,
    # 'round':round
    # } 
    
    # r.execute_command('JSON.SET', username, '.', json.dumps(data))

    # else:
    #     r.execute_command('JSON.NUMINCRBY' , username ,'.score', score)
    reply = json.loads(r.get(username))
    print(f"upadte score= {reply['score']}")
    return 'success'

def updateUserShape(username,comment):
    
    data = json.loads(r.get(username))
    print(f"data befor= {data}")
    data['shape']=comment
    print(f"data after= {data}")
    r.set(username,json.dumps(data))
    reply = json.loads(r.get(username))
    print(f"reply = {reply}")
    return 'success' 


# def updateAnswerKey(username,comment):
#     data = {
#     'answer':comment
#     }
#     r.execute_command('JSON.SET', username, '.', json.dumps(data))
#     reply = json.loads(r.execute_command('JSON.GET', username))
#     print(f"user answer = {reply['answer']}")
#     return reply['answer']

def checkAns(username,ans):
    reply = json.loads(r.get(username))
    shape=reply['shape']
    print(reply)
    print(f"ans= {ans} type= {type(ans)}")
    if(ans == AnsKey[f'{shape}']):
        print('equal')
        return 'success'
    return False

