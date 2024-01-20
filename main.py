import time

from utils.pin import PinNum
from motor.servo import Servo
from picoserver.picoserver import PicoServer

print("[starting]")

servo = Servo(PinNum.D7)
for value in (0, 180, 10):
    servo.angle(value)
    time.sleep(0.5)

server = PicoServer()

@server.route('/servo')
def servo_angle(r):
    if 'angle' not in r.args:
        return server.respond(400, 'text/plain', 'required arg angle not provided')
    servo.angle(int(r.args['angle']))
    server.respond(200, 'text/plain', f'servo rotate to angle {r.args["angle"]}') 

server.start()
