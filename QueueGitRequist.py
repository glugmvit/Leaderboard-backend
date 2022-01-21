import json

from Round import squidgameActivity
from SquidGame import redLightGreenLight, dalgonaCookie, squidGame, tugOfWar
from RedisDBMS import updateUser



def addData(request):
    
    # print(request)
    
    request=json.loads(request)
    username=request['sender']['login']
    round=squidgameActivity(request)
    
    status='None'

    print(f"{username} entered {round} ")
    
    if round==11:        
        score=redLightGreenLight()
        status=updateUser(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status
    elif round==21:
        score=dalgonaCookie()
        status=updateUser(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status    
    elif round==22:
        score=dalgonaCookie()
        status=updateUser(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status  
    elif round==31:
        score=tugOfWar()
        status=updateUser(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status 
    elif round==41:
        score=squidGame()
        status=updateUser(username,round,score)
        print(f"{username} score update {score}, status: {status}")
        return status
    
    
    return status

