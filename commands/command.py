class Command:
    pane = None

    def __init__(self):
        if self.pane is None:
            raise Exception('Not set pane variable')

    def execute(self):
        raise NotImplementedError
