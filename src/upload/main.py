from Controller import Controller, hsv_to_rgb
from Color import Color
from Color import Colors
import uasyncio
import urequests as requests 
import json
from microdot_asyncio import Microdot
import time

controller = Controller(4, 50)
app = Microdot()

while True:
    res = requests.get(url="https://led-tree.vercel.app/api/lights")
    print(res.text)
    data = json.loads(res.text)
    print(data)
    


@app.route('/')
async def hello(request):
    return 'Hello world'

@app.route('/rgb')
def rgb(request):
    #http://<ip>/rgb?r=255&g=255&b=255&br=0.5
    controller.onRange(0, 50, Color(
        int(request.args.get('r') or 10), 
        int(request.args.get('g') or 191), 
        int(request.args.get('b') or 255)))
    controller.setBrightness(float(request.args.get('br') or 0.01))
    controller.apply()
    return 'RGB set'

@app.route('/hsv')
def hsv(request):
    #http://<ip>/hsv?h=&s=1&v=1
    hue = float(request.args.get('h') or 196)
    saturation = float(request.args.get('s') or 0.96)
    # If the value imputed is below 0.07, set the value to 0.07
    value = max(float(request.args.get('v') or 0.5), 0.07)
    RGBColors = hsv_to_rgb(
        hue,
        saturation,
        value
    )
    controller.onRange(0, 50, Color(RGBColors[0], RGBColors[1], RGBColors[2]))
    controller.setBrightness(value)
    controller.apply()
    return 'they call me the hue master'

@app.route('/rainbow')
def rainbow(request):
    #http://<ip>/rainbow?br=0.5
    controller.rainbow_pulse(
        start = 0,
        end = 50,
        brightness = max(float(request.args.get('br') or 0.4), 0.07), 
        loops = int(request.args.get('loops') or 10))
    return 'rainbowed :O'

def start_server():
    print('Starting microdot app')
    print('turning off LEDs')
    controller.clear()
    try:
        app.run(port=80, debug=True)
    except:
        app.shutdown()
        
        
# while True:
#   controller.rainbow_cycle(10, 0.01)
#   controller.clear()
#   time.sleep(1)