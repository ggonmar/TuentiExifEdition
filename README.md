# TuentiExifEdition
--------------------
Cuando Tuenti cerró, se ofreció enviar a todos los usuarios que lo solicitaran un zip con todas las fotos que se subieron a la plataforma.

El problema fue que esas imagenes venían sin ningun tipo de información EXIF, por lo que intentar clasificar esas imagenes en un gestor de imagenes (Google Photos, por ejemplo) era misión imposible para ordenar en orden cronológico.

Con un poco de trasteo con los metadatos EXIF y la libreria piexif de python, he conseguido desarrollar un script que busca las fotos en un directorio "path" de manera recursiva en todos los subdirectorios, extrae la fecha del nombre del archivo (tal y como venía de Tuenti), y la asigna en todos los campos correspondientes a fecha de creacion / fecha de digitalización.

He intentado actualizar el campo de "Comentarios" para que incluyera alguna referencia al album o a "Origen: Tuenti", pero por algun motivo, lo carga, pero Windows no lo muestra.

En cualquier caso, espero les sea de utilidad!
