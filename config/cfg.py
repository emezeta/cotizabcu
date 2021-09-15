
# configurables     # este bloque irá a un archivo de configuraciones

x_cacert = False  # "/tmp/Autoridad_Certificadora_Raiz_Nacional_de_Uruguay.crt" # agesic/correos
x_wsdl_url = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
x_headers = {'a': 'b'}  # cualquiera para simplificar el get

# {'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:35.0) Gecko/20170101 Firefox/35.0'}

x_def_file = "/tmp/awsbcucotizaciones.xml"
wsdl_def_url = 'file://' + x_def_file

grupo = 2  # 1. mercado internacional 2. mercado local
moneda = {'item': 2225}  # Dolar USA Billete. Ver  doc/Web_Service_Doc_BCU.pdf
# fin configurables