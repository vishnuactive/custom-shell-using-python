import signal

def handle_sigint(signum, frame):
    print("\n(Interrupted)")

def listen_to_signint():
    signal.signal(signal.SIGINT,handle_sigint)