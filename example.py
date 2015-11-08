import pluma

class ExamplePyPlugin(pluma.Plugin):
    def activate(self, window):
        print "Hola"
        pass

    def deactivate(self, window):
        pass

    def update_ui(self, window):
        pass
