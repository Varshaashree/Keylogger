from pynput.mouse import Listener
def write(x,y):
    print('Position of current mouse{0}'.format(x,y))
with Listener(on_move=write) as li:
    li.join()