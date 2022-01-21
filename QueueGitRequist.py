import json

from Round import squidgameActivity
from SquidGame import redLightGreenLight, dalgonaCookie, squidGame, tugOfWar
from RedisDBMS import updateUserScore



def addData(request):
    
    # print(request)
    
    request=json.loads(request)
    username=request['sender']['login']
    round=squidgameActivity(request)
    
    status='None'

    print(f"{username} entered {round} ")
    
    if round==11:        
        score=redLightGreenLight()
        status=updateUserScore(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status
    elif round==21:
        score=dalgonaCookie(username,round,comment=(str(request['comment']['body'])).lower())
        status=updateUserScore(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status    
    elif round==22:
        score=dalgonaCookie(username,round,comment=str(request['comment']['body']))
        status=updateUserScore(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status  
    elif round==31:
        score=tugOfWar(request['pull_request']['additions'],request['pull_request']['changed_files'])
        status=updateUserScore(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status 
    elif round==41:
        score=squidGame(str(request['pull_request']['rebaseable']))
        status=updateUserScore(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status
    
    
    return status

