import json

# 11- round1 task1
# 21- round2 task1
# 22- round2 task2
# 31- round1 task1
# 41- round2 task2

def squidgameActivity(request):

    if 'forkee' in request.keys():
        return 11
    
    elif 'issue'  in request.keys():
        shapes=['triangle', 'star','circle','umbrella']
        print((str(request['comment']['body'])).lower())
        if (str(request['comment']['body'])).lower() in shapes:
            return 21
        else:
            return 22
        
    elif 'pull_request' in request.keys():
        # print("keys=",request['pull_request'].keys())
        # print(str(request['pull_request']['rebaseable']))
        if request['action']=='opened' and str(request['pull_request']['rebaseable'])=='None':
            return 31
        elif request['action']=='opened':
            return 41
        else:
            return 0

    return 0
