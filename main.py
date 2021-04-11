
#main.py
 
import time
import threading
 
from redirection import StdoutTkinter
 
def starter():
    """Debut mainloop de Tkinter """
    app = StdoutTkinter()
    app.mainloop()
 
## Début Boucle de Tkinter, pour lire le stdout
thread = threading.Thread(target=starter)
thread.start()
 
## Test voir si les prints sont redirigé..
TEST = 0
while TEST <= 10:
    print('OK')
    time.sleep(1)
 
thread.join()