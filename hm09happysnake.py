import bottle
import os
import random

def boardUpdate(boardData):
    headX = 0
    headY = 0
    board = [[0 for x in range(boardData['height'])] for x in range(boardData['width'])]
    for snake in boardData['snakes']:
        for coord in range(len(snake['coords'])-1,0,-1):
            board[snake['coords'][coord][0]][snake['coords'][coord][1]] = coord+1
        if snake['id'] == 'c3ce7cf7-f1db-49b3-8b6e-adc5e487aed4':
            headX = snake['coords'][0][0]
            headY = snake['coords'][0][1]
    
    
            
    return (board, headX, headY)

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#ff00ff',
        'head': 'http://orig00.deviantart.net/e406/f/2013/211/5/1/51f702263bb0ed9c65ac186f9e3ab85e-d6fu0h2.png'
    }

@bottle.post('/start')
def start():
    data = bottle.request.json
    
    gamename = data['game']
    mode = data['mode']
    height = data['height']
    width  = data['width']
    
    snake = data['snakes']
    food = data['food']

    return {
        'taunt': 'Lets do this! LEERRRRROYYYY SNAKES!'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    
    board = 0
    headX = 0
    headY = 0
    direction = ''
    
    (board, headX, headY) = boardUpdate(data)
    coords = [headX, headY]
    
    switch = random.randint(0,3)
    if switch==0:
        if (headY-1 >= 0) and board[headX][headY-1]==0:
            direction = 'north'
        elif (headX-1 >= 0) and board[headX-1][headY]==0:
            direction = 'west'
        elif (headY+1 < 17) and board[headX][headY+1]==0:
            direction = 'south'
        elif (headX+1 < 17) and board[headX+1][headY]==0:
            direction = 'east'
    elif switch == 1:
        if (headX+1 < 17) and board[headX+1][headY]==0:
            direction = 'east'
        elif (headY-1 >= 0) and board[headX][headY-1]==0:
            direction = 'north'
        elif (headX-1 >= 0) and board[headX-1][headY]==0:
            direction = 'west'
        elif (headY+1 < 17) and board[headX][headY+1]==0:
            direction = 'south'
    elif switch == 2:
        if (headX-1 >= 0) and board[headX-1][headY]==0:
            direction = 'west'
        elif (headX+1 < 17) and board[headX+1][headY]==0:
            direction = 'east'
        elif (headY-1 >= 0) and board[headX][headY-1]==0:
            direction = 'north'
        elif (headY+1 < 17) and board[headX][headY+1]==0:
            direction = 'south'
    else:
        if (headY+1 < 17) and board[headX][headY+1]==0:
            direction = 'south'
        elif (headY-1 >= 0) and board[headX][headY-1]==0:
            direction = 'north'
        elif (headX-1 >= 0) and board[headX-1][headY]==0:
            direction = 'west'
        elif (headX+1 < 17) and board[headX+1][headY]==0:
            direction = 'east'
        

    return {
        'move': direction,
        'taunt': 'LEERRRRROYYYY JEEENNNKIIINNNS!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'GL HF!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
