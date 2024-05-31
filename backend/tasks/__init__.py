from ..app import huey


def deserialize_task(data):
    return huey.serializer.deserialize(data)
