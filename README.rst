
Cotizaciones de moneda extranjera BCU
'''''''''''''''''''''''''''''''''''''

Script simple para obtener cotizaciones de divisas al último cierre. 
Soporta consultas de cotizaciones para rangos de fechas.

requiere suds y requests::

    python >= 3.8
    pip install suds-community
    pip install requests
    pip install python-dateutil 
    


Para ejecutar: descargar y descoprimir `coticabcu` en una carpeta. Luego::

    $ cd carpeta_cotizabcu
    $ ./cotizaciones
    

    
Ejemplos::



 $ ./cotizaciones
         DLS. USA BILLETE        13-10-2017      29.413



 $ ./cotizaciones 2021-10-01 2021-10-16
         DLS. USA BILLETE        01-10-2021      42.942 
         DLS. USA BILLETE        04-10-2021      42.994 
         DLS. USA BILLETE        05-10-2021      43.034 
         DLS. USA BILLETE        06-10-2021      43.295 
         DLS. USA BILLETE        07-10-2021      43.296 
         DLS. USA BILLETE        08-10-2021      43.419 
         DLS. USA BILLETE        12-10-2021      43.623 
         DLS. USA BILLETE        13-10-2021      43.774 
         DLS. USA BILLETE        14-10-2021      43.9 
         DLS. USA BILLETE        15-10-2021      43.889 



 $ ./cotizaciones -h

        Consulta cotizaciones al cierre entre dos fechas

        uso: cotizaciones [<desdefecha> <hastafecha>]

             Sin opciones para ver valores del último cierre 
             Rangos > 5 dias. Final del rango <= hoy

             Formato de fechas: yyyy-mm-dd 
                        yyyy: año 4 dígitos
                          mm: mes 2 dígitos
                          dd: día 2 dígitos




Limitaciones: Si se usa rango de fechas, el tamaño de un rango deberá ser mayor que 5 y menor que 365 días calendario. El valor superior de un rango debe ser igual o menor que la fecha actual. Funciona sólo para dólares USA




**Virtual Python**

Es posible aislar la instalación a efectos de no interferir con las versiones python de tus equipos usando un entorno virtual python como virtualenv u otra herramienta del tipo::


    $ /usr/bin/virtualenv --python=python3.8 /tmp/virtpy3.8
    $ . /tmp/virtpy3.8/bin/activate
    (virtpy3.8) $ pip install suds-community
    (virtpy3.8) $ pip install requests
    (virtpy3.8) $ pip install python-dateutil
    (virtpy3.8) $ cd carpeta_cotizabcu
    (virtpy3.8) $ ./cotizaciones
    
Salir del entorno vitual::


    (virtpy3.8) $ deactivate



El entorno del ejemplo desaparece sin dejar huellas en el próximo reinicio de tu equipo. Para hacerlo permanente, elegir un destino diferente a `/tmp/`
 

GNU/GPLv3 ver <https://www.gnu.org/licenses/>
 
