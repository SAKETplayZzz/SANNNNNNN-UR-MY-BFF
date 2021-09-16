#imps
from ursina import *
import platform

#info_finders
osv = (platform.release())
sysv = (platform.version())
winos = (platform.system())
processor = (platform.processor())
machtype = (platform.machine())

#app
app = Ursina(size=(600,600),editor_ui = None)

#win
window.fps_counter.enabled = False
window.exit_button.enabled = True
window.icon = 'logocon.ico'

#bg
Entity(model='quad',scale= (15,15),texture = load_texture('bg.png'))

#txt
head = Text(text = 'Your system')
head.position = (-0.45,0.35)
head.scale = 3.5
head.font = 'joystix monospace.ttf'

os_caller = Text(text = 'Your Operating system is -' + winos+' '+ osv)
os_caller.position = (-0.45,0.25)
os_caller.scale = 1.2
os_caller.font = 'joystix monospace.ttf'

sys_ver_caller = Text(text = 'Your system version is - ' + sysv)
sys_ver_caller.position = (-0.45,0.20)
sys_ver_caller.scale = 1.2
sys_ver_caller.font = 'joystix monospace.ttf'

pros_caller = Text(text = 'Your processor is - ')
pros_caller.position = (-0.45,0.15)
pros_caller.scale = 1.2
pros_caller.font = 'joystix monospace.ttf'
ut = Text(text = processor)
ut.position = (-0.45,0.10)
ut.scale = 0.9
ut.font = 'joystix monospace.ttf'

machinety = Text(text='Machine type = '+machtype)
machinety.position = (-0.45,0.05)
machinety.scale = 1.2
machinety.font = 'joystix monospace.ttf'

app.run()