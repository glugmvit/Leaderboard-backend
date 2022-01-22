import redis
from redis.commands.json.path import Path
import json

r = redis.from_url( url='redis://redis-18607.c279.us-central1-1.gce.cloud.redislabs.com:18607',password='Z2PfDUUz8IumHhEs0kj28HE8oum4S4OS')

AnsKey = {
        "triangle":99999,
        "circle":88888,
        "umbrella":77777,
        "star":66666
    }

def updateUserScore(username,round,score):

    # if(round==21 or (round==22 and score==10)):
    #     points = 20
    # elif(round==22 and score==0):
    #     points = 10
    # elif(round==31):
    #     points = 30
    # else:
    #     points = 40
    # data = {
    # 'score':points,
    # 'round':round
    # }
    #r.execute_command('JSON.SET', username, '.', json.dumps(data))
    data = {
    'score':score,
    'round':round
    } 
    if(round==11):
        r.execute_command('JSON.SET', username, '.', json.dumps(data))

    else:
        r.execute_command('JSON.NUMINCRBY' , username ,'.score', score)
    reply = json.loads(r.execute_command('JSON.GET', username))
    print(f"upadte score= {reply['score']}")
    return 'success'

def updateUserShape(username,comment):
    data = {
    'shape':comment
    }
    r.execute_command('JSON.SET', username, '.', json.dumps(data))
    reply = json.loads(r.execute_command('JSON.GET', username))
    print(f"user shape = {reply['shape']}")
    return 'success' 


def updateAnswerKey(username,comment):
    data = {
    'answer':comment
    }
    r.execute_command('JSON.SET', username, '.', json.dumps(data))
    reply = json.loads(r.execute_command('JSON.GET', username))
    print(f"user answer = {reply['answer']}")
    return reply['answer']

def checkAns(username,ans):
    reply = json.loads(r.execute_command('JSON.GET', username))
    if(reply['answer'] == ans):
        return True
    return False
