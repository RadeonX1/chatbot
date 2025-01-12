import time
def respond(message):
    time.sleep(1) # delay 1 sec
    return "I can hear you! you said: {}".format(message)

def send_message(message):
# calls respond() to get response
    print(respond(message))
send_message("hello!")