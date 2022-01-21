import redis


r= redis.Redis(host='localhost')


def updateUserScore(username,round,score):
    return 'success'

def updateUserShape(username,comment):
    return 'success' 


def updateAnswerKey(username,comment):
    return 'success'


def checkAns(username,ans):
    return 'success'