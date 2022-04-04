from pythonosc import dispatcher
from pythonosc import osc_server

if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/annotations/thumb", print)  # set address from

    server = osc_server.ThreadingOSCUDPServer(
        ('localhost', 8081), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

server_close()
