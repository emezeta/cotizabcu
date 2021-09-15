
Cotizaciones de moneda extranjera BCU
'''''''''''''''''''''''''''''''''''''

Script simple para obtener cotizaciones de divisas al último cierre. 
Soporta consultas de cotizaciones para rangos de fechas.

requiere suds y requests::

    python >= 3.8
    pip install suds
    pip install requests

se ejecuta::

    ./cotizaciones





Ejemplos::



 $ ./cotizaciones
         DLS. USA BILLETE        13-10-2017      29.413



 $ ./cotizaciones 2015-06-21 2015-07-02
         DLS. USA BILLETE        22-06-2015      26.828 
         DLS. USA BILLETE        23-06-2015      26.901 
         DLS. USA BILLETE        24-06-2015      26.882 
         DLS. USA BILLETE        25-06-2015      26.867 
         DLS. USA BILLETE        26-06-2015      26.903 
         DLS. USA BILLETE        29-06-2015      27.017 
         DLS. USA BILLETE        30-06-2015      27.07 
         DLS. USA BILLETE        01-07-2015      27.189 
         DLS. USA BILLETE        02-07-2015      27.148



 $ ./cotizaciones -h

        Consulta cotizaciones al cierre entre dos fechas

        uso: cotizaciones [<desdefecha> <hastafecha>]

             Sin opciones para ver valores del último cierre 
             Rangos > 5 dias. Final del rango <= hoy

             Formato de fechas: yyyy-mm-dd 
                        yyyy: año 4 dígitos
                          mm: mes 2 dígitos
                          dd: día 2 dígitos




Limitaciones: el tamaño de un rango deberá ser mayor que 5 y menor que 365 días calendario. El valor superior de un rango debe ser igual o menor que la fecha actual. Funciona sólo para dólares USA


GNU/GPLv3 ver <https://www.gnu.org/licenses/>
 
