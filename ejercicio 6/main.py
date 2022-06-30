from repositorioProvincias import RespositorioProvincias
from vistasProvincias import ProvinciasView
from controladorProvincias import ControladorProvincias
from objectEncoder import ObjectEncoder

def main():
    conn = ObjectEncoder('datos.json')
    repo = RespositorioProvincias(conn)
    vista = ProvinciasView()
    ctrl = ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()