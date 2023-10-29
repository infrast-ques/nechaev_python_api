import threading

local_thread = threading.local()


def get_local_thread():
    if not hasattr(local_thread, 'value'):
        local_thread.value = list()
    return local_thread.value


def add_to_local_thread(new_value):
    if not hasattr(local_thread, 'value'):
        local_thread.value = list()
    return local_thread.value.append(new_value)
