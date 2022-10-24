from datetime import datetime, timedelta
from date_commons import today_date, from_string, diff_dates

date_str = '01-01-2022'
date_obj = from_string(date_str)
date_now = today_date()

a = diff_dates(date_obj, date_now)
print(a)

class Periodo:
    def __init__(self, fecha_desde, fecha_hasta):
        _fecha_desde = from_string(fecha_desde)
        _fecha_hasta = from_string(fecha_hasta)
        self._tiempos = diff_dates(_fecha_desde, _fecha_hasta)
        self._valido = False

    def getTiempos(self):
        return self._tiempos

class Computo:
    def __init__(self, escalafon: str, jerarquia: str):
        self._actividades = []
        self._ausencias = []
        self._escalafon = escalafon
        self._jerarquia = jerarquia
    
    def add_actividad(self, fecha_desde, fecha_hasta):
        periodo = Periodo(fecha_desde, fecha_hasta)
        self._actividades.append(periodo)

    def add_ausencia(self, fecha_desde, fecha_hasta):
        periodo = Periodo(fecha_desde, fecha_hasta)
        self._ausencias.append(periodo)

    def calcular_actividades(self):
        l = [0,0,0]
        for p in self._actividades:
            t = p.getTiempos()
            for i in range(3):
               l[i] += t[i]
        if l[1] > 12:
            l[0] +=l[1] // 12
            l[1] = l[1] % 12
           
        print(l)

    def ver_actividades(self):
        return self._actividades

class ComputoFactory:
    def _get_computo(self, computo: Computo, tipo_tramite: str):
        if tipo_tramite == "JUBVOL":
            return ComputoJubilacionVoluntaria(computo)
        elif tipo_tramite == "JUBOBL":
            return ComputoJubilacioObligatoria(computo)
        elif tipo_tramite == "RETVOL":
            return ComputoRetiroVoluntaria(computo)
        elif tipo_tramite == "RETOBL":
            return ComputoRetiroObligatoria(computo)
        else:
            raise ValueError(tipo_tramite)


class ComputoJubilacionVoluntaria:
    def __init__(self, computo: Computo):
        self._computo = computo

class ComputoJubilacioObligatoria:
    def __init__(self, computo: Computo):
        self._computo = computo

class ComputoRetiroVoluntaria:
    def __init__(self, computo: Computo):
        self._computo = computo

class ComputoRetiroObligatoria:
    def __init__(self, computo: Computo):
        self._computo = computo
    


if __name__ == "__main__":
   print("Prueba Computo")

   computo = Computo("01","10")
   computo.add_actividad('01-08-2012','01-06-2018')
   computo.add_actividad('01-01-2007','31-07-2012')
   computo.add_actividad('01-01-2005','31-12-2006')
   computo.calcular_actividades()
   

   #factory = ComputoFactory()  
   #a = factory._get_computo(computo, "RETVOL")
   
   #print(a)