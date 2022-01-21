import json

from RedisDBMS import updateUserScore,updateUserShape,checkAns

def score():
    #score logic
    return 10

def redLightGreenLight(): 
    print('success') 
    return score()

def dalgonaCookie(username,round,comment):
    if round==21:
        status=updateUserShape(username,comment)
        if status=='success':
            print('success 21')
            return score()
    elif round==22:
        status=checkAns(username,comment)
        if status=='success':
            print('success 22')
            return score()
    return 0

def tugOfWar(additions,changed_file):
    print("additions: ",additions," changed file: ",changed_file)
    if str(additions)=="1" and str(changed_file)=="1":
        print('success 31')
        return score()
    print('not done appropriate changes')
    return 0

def squidGame(rebase):
    if rebase!='None':
        print('success')
        return score()
    print('no rebase done')
    return 0