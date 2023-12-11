from Controller import Controller
from Color import Color
from Color import Colors
import uasyncio
from microdot_asyncio import Microdot
import time

controller = Controller(4, 50)
app = Microdot()


@app.route('/')
async def hello(request):
    return 'Hello world'

@app.route('/rgb')
def rgb(request):
    #http://<ip>/rgb?r=255&g=255&b=255
    controller.onRange(0, 10, Color(int(request.args['r']), int(request.args['g']), int(request.args['b'])))
    controller.setBrightness(0.01)
    return 'RGB set'

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80, debug=True)
    except:
        app.shutdown()
        
        
# while True:
#   controller.rainbow_cycle(10, 0.01)
#   controller.clear()
#   time.sleep(1)