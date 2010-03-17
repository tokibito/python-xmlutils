class BaseRenderer(object):
    def __init__(self, *args, **kwargs):
        pass

    def render(self, node):
        raise NotImplementedError
