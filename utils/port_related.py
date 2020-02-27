def is_port_in_use(port):
    # https://stackoverflow.com/questions/2470971/fast-way-to-test-if-a-port-is-in-use-using-python
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def get_port_not_used(port):
    port_is_used = is_port_in_use(port)
    while port_is_used:
        port += 1
        port_is_used = is_port_in_use(port)

    return port
