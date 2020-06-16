import lib.model as model

class Router:
    @staticmethod
    def run(app):
        
        @app.route('/')
        def root():
            return model.getRootData()

        @app.route('/daftar-komik')
        def daftar_komik():
            return model.getDaftarKomik()
        
        @app.route('/project-list')
        def project_list():
            return model.getProjectList()
            

