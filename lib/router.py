import lib.model as model

class Router:
    @staticmethod
    def run(app):
        
        @app.route('/')
        def root():
            return model.getRootData()
            

