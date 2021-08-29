import Telegram
import Interface
from threading import Thread

botThread = Thread(target=Telegram.botListener)
# interfaceThread = Thread(target=Interface.startTkinterInterface)
botThread.start()
# interfaceThread.start()

Interface.startTkinterInterface()