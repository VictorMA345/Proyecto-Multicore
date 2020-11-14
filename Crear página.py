from Multicore import HolaMundo
import webbrowser
import cgitb
import cgi
from Multicore.HolaMundo import *
f = open('Proyecto-Multicore-Jordan-Pedro-Victor.html', 'wb')
inputs = cgi.FieldStorage()

mensaje = """<html lang="es"><head>
<script>
    function accion()
    {
        $.ajax({
            type:'POST', //aqui puede ser igual get
            url: 'HolaMundo.py',//aqui va tu direccion donde esta tu funcion php
            data: {id:1,otrovalor:'valor'},//aqui tus datos
            success:function(data){
                //lo que devuelve tu archivo mifuncion.php
           },
           error:function(data){
            //lo que devuelve si falla tu archivo mifuncion.php
           }
         });
    }
</script>
    <form action="HolaMundo.py">
        <h1>Proyecto multicore</h1>
        <input type=text name="buscar"><br>
        <input type="submit" name="" value="Buscar" id="boton1" onclick = "accion();">
    </form>
"""

#mensaje = """<html lang="es">

#<head>
#    <h1>Proyecto multicore</h1>
#        <form action = "HolaMundo.py" method = "ejecute"
#            <p> <input type="text" id="fname" name="fname"> <input type="submit" value ="Buscar";> </p>
#        </form>
#</head>
#<body>
#    <p>Esto es una prueba!</p>
#</body>
#    <p> </p>
#<body>
#
#</body>
#</html>"""

cgitb.enable()
#mensaje = bytes("""
#<form action = "/cgi-bin/hello_get.py" method = "get">
#First Name: <input type = "text" name = "first_name">  <br />
#
#Last Name: <input type = "text" name = "last_name" />
#<input type = "submit" value = "Submit" />
#</form>
#""".encode())
f.write(mensaje.encode())

form = cgi.FieldStorage()
if form.getlist('opcion'):
    if form['opcion'].value == "1":
        escribir()
f.close()

webbrowser.open_new_tab('Proyecto-Multicore-Jordan-Pedro-Victor.html')
