#!/usr/bin/env python
# coding=utf-8

# ##################################################################################
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by the
#  Free Software Foundation; either version 3, or (at your option) any later
#  version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#  for more details. <https://www.gnu.org/licenses/>
# ##################################################################################

__licence__ = "GNU/GPLv3"
__author__ = "Marcelo Zunino (InfoPrimo SL) 2017-Today"

import sys

try:
    from suds.client import Client
    from suds.sudsobject import asdict
    from suds.cache import NoCache
    from dateutil.parser import parse
    import requests
    from datetime import datetime, date
except Exception as ex:
    print("\n\tVerificar dependecia de módulos:\n `suds` `requests`")
    sys.exit(1)

import urllib3
from config import cfg
from datetime import timedelta, date
urllib3.disable_warnings()

def get_wsdl_def(wsdl_url, headers, cacert, def_file):
    """
       Lee las definiciones del web del banco.
       Crea "awsbcucotizaciones.xml" con las definiciones
       Menos `header` los 3 parámetros restantes son strings
       y que contienen "path" distintos elementos en
       el filesystem local.

    :param wsdl_url:  string: url para obtener las definiciones
    :param headers:   dict:   maquillaje para simular un navegador (no es estrictamente necesario)
    :param cacert:    string: cert. de autoridad certificadora que emitió el certificado al BCU (el url es "httpS://")
    :param def_file:  string: donde de almacenarán las definiciones
    :return:          bool:   `True` las definiciones grabadas "awsbcucotizaciones.xml" o `False` No se pudo grabar.
    """
    res = False
    if not (wsdl_url and headers):
        print("\n\tFaltan parámetros")
    else:
        res = requests.get(wsdl_url, headers=headers, verify=False) or None
        if res:
            try:
                with open(def_file, 'w') as f:
                    f.write(res.text)
                res = True
            except Exception as err:
                print("\n\tError {}: Verificar parámetros".format(err,))
    return res


def ayudin():
    print("\n\tAyuda")
    print("\n\tuso: cotizaciones [<desde> <hasta>]")
    print("\n\t     Sin opciones: valores al último cierre ")

    print("\n\tFormato de fechas: aaaa-mm-dd ")
    print("\t     Año en 4 dígitos, mes y día en 2 dígitos")
    print("\t     Rangos > a 5 días. Final del rango < hoy\n")



def parametros(pars_in):
    """
        Verificación de parámetros de entrada
    :param pars_in: string: -h
                            dd-mm-yyyy
                            dd-mm-yyyy dd-mm-yyyy
                            nada
    :return: tupla  <(fecha_desde, fecha_hasta)> ó <(None,None)> o string: <muestra ayuda>

    """
    _desde = _hasta = None
    if  len(pars_in) == 2 and pars_in[1] == '-h':
        ayudin()

    if len(pars_in) == 1:
        # devolver ultima cotización
        #  _desde = _hasta = None
        pass

    elif len(pars_in) == 3:

        if len(pars_in[1]) == 10 and len(pars_in[2]) == 10:
            try:
                parse(pars_in[1])
                parse(pars_in[2])
                _desde, _hasta = (pars_in[1],pars_in[2])
                #TODO:  verificar formatos de valores para `parse`
                #       parse acepta diferentes tipos de separadores y fechas!
                #       analizar si vale la pena mejorar esto.
            except Exception as err:
                print("\n\t[ERROR] {}:  {} no parece ser una fecha válida\n".format(err, pars_in[2]))
                ayudin()
        else:
            print("\n\t[ERROR]  {}, {} o ambas no parecen ser fechas válidas\n".format(pars_in[1], pars_in[2]))
            ayudin()
        if not (_desde <= _hasta):
            print("\n\t[ERROR]  {} debe ser mayor o igual a {} \n".format(pars_in[2], pars_in[1]))
            ayudin()
    else:
        print("\n\t[ERROR] Verificar parámetros !! {} \n".format(pars_in[1:],))
        ayudin()
    return _desde, _hasta


if __name__ == '__main__':
    
    fdesde, fhasta = parametros(sys.argv)
    if fdesde and fhasta:
        d_fdesde = datetime.strptime(fdesde,"%Y-%m-%d").date()
        d_fhasta = datetime.strptime(fhasta,"%Y-%m-%d").date()
        if (d_fhasta - d_fdesde).days < 6 or d_fhasta > date.today():
            print("\n\t[ERROR] El rango no es válido! ")
            print("\t\t\tEl rango debe tener una extención mayor a 5 días")
            print("\t\t\tLa fecha final del rango debe ser menor que la fecha de hoy\n")
            ayudin()

    else:
        dsd = date.today() - timedelta(days=5)
        fdesde = dsd.strftime("%Y-%m-%d")
        hst = date.today()
        fhasta = hst.strftime("%Y-%m-%d")

    # lee definiciones del wsdl, graba en "/tmp/awsbcucotizaciones.xml"
    ok = get_wsdl_def(cfg.x_wsdl_url, cfg.x_headers, cfg.x_cacert, cfg.x_def_file)

    if ok and fdesde and fhasta:
        # instancia el cliente para 'cosumir` el ws.
        client = Client(cfg.wsdl_def_url, cache=NoCache())

        # personaliza valores del cliente según objetivos
        cotiza_obj = client.factory.create("wsbcucotizacionesin")
        cotiza_obj.FechaDesde = fdesde
        cotiza_obj.FechaHasta = fhasta
        cotiza_obj.Grupo  = cfg.grupo
        cotiza_obj.Moneda = cfg.moneda

        # invoca/consume el servicio web
        # ret = client.service.Execute(cotiza_obj)
        ret = client.service.Execute(cotiza_obj)
        val = list(asdict(ret.datoscotizaciones).items())[0][1]
        for i in val:
            fecha =  i.Fecha.strftime("%d-%m-%Y")
            print("\t {} \t {}\t {} ".format(i.Nombre, i.Fecha.strftime("%d-%m-%Y"), i.TCV,))
        print("\n")

    else:
        print("\n\t{}\n".format("Algo salió mal... :( ",))
