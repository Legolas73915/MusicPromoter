biblioteca = []
promociones = []



def validar_opcion():
    while True:
        try:
            opcion = int(input('Seleccione la opcion: '))
            return opcion
        except ValueError:
            print('Valor incorrecto')

def menu():
    print('=========================')
    print('  Music Promoter v1.0')
    print('=========================\n')
    print('1. Registrar contenido\n'
          '2. Ver contenido registrado\n'
          '3. Crear promocion\n'
          '4. Ver Promociones\n'
          '5. Salir\n')



def registrar_contenido():
    nombre = input('Nombre del contenido: ')
    artista = input('Artista de la cancion: ')
    tipo_de_contenido = input('Tipo de contenido: ')
    enlace = input('Enlace: ')
    plataforma_principal = input('Plataforma Principal: ')

    contenido = None
    if not nombre or not artista or not tipo_de_contenido or not enlace or not plataforma_principal:
        print('Contenido incompleto vuelve a registrar')
    else:
        contenido = {'nombre': nombre, 'artista': artista, 'tipo_de_contenido': tipo_de_contenido,
                     'enlace': enlace, 'plataforma_principal': plataforma_principal}
        biblioteca.append(contenido)
        print('Contenido registrado exitosamente\n')




def mostrar_contenidos():
    print('======Contenidos======\n')

    if not biblioteca:
        print('No hay contenido')
    else:
        for contenido in biblioteca:
            print(f'Nombre: {contenido['nombre']}')
            print(f'Artista: {contenido['artista']}')
            print(f'Tipo de contenido: {contenido['tipo_de_contenido']}')
            print(f'Enlace: {contenido['enlace']}')
            print(f'Plataforma principal: {contenido['plataforma_principal']}\n')



def crear_promocion():
    contenido_promocion = input('Escribe el nombre del contenido: ')
    contenido_encontrado = None
    for contenido in biblioteca:
        if contenido['nombre'].lower() == contenido_promocion.lower():
            contenido_encontrado = contenido
            break
    if not contenido_encontrado:
        print(f'El contenido {contenido_promocion} no existe')
        return

    print('Elige el lugar de la promocion:')
    print('1. Youtube\n2. Instagram\n3. TikTok\n')
    seleccion_promocion = validar_opcion()

    plataforma = None
    texto = None
    if seleccion_promocion == 1:
        plataforma = 'Youtube'
        texto = promocion_youtube(contenido_encontrado)
    elif seleccion_promocion == 2:
        plataforma = 'Instagram'
        texto = promocion_instagram(contenido_encontrado)
    elif seleccion_promocion == 3:
        plataforma = 'TikTok'
        texto = promocion_tick_tock(contenido_encontrado)
    else:
        print('Elige una opcion correcta')
        return


    hashtags = generar_hashtags(contenido_encontrado)
    if hashtags is None:
        print('No hay hashtags para este contenido')
        return

    guardar_promociones(contenido_encontrado, plataforma, texto, hashtags)
    print('Promocion creada exitosamente')




def promocion_youtube(contenido_youtube):
    texto_youtube = (
        f'🎵 ¡Ya salió mi nueva canción!\n\n'
        f'✨ Título: {contenido_youtube["nombre"]}\n'
        f'🔥 No te la pierdas, está llena de energía y emoción.\n'
        f'👉 Escúchala ahora en YouTube:\n'
        f'{contenido_youtube["enlace"]}\n\n'
        f'Si te gusta, dale 👍 y comparte con tus amigos. ¡Tu apoyo hace la diferencia!')
    return texto_youtube


def promocion_instagram(contenido_instagram):
    texto_instagram = (
        f'🎶 ¡Ya está disponible mi nueva canción en YouTube!\n\n'
        f'✨ {contenido_instagram["nombre"]}\n'
        f'🔥 Dale play y disfruta la vibra.\n'
        f'👉 Escúchala completa aquí:\n'
        f'{contenido_instagram["enlace"]}\n\n'
        f'Apóyame con tu ❤️ y compártela en tus historias.'
    )
    return texto_instagram



def promocion_tick_tock(contenido_tiktok):
    texto_tiktok = (
        f'🎶 ¡Ya salió mi nueva canción!\n'
        f'🔥 {contenido_tiktok["nombre"]}\n'
        f'👉 Escúchala completa en YouTube:\n'
        f'{contenido_tiktok["enlace"]}\n\n'
        f'💃 Súbela a tus videos y etiqueta para que la vea la comunidad.'
    )
    return texto_tiktok




def generar_hashtags(tipo_de_contenido):
    if 'Cancion'.lower() == tipo_de_contenido['tipo_de_contenido'].lower():
        return ['#NuevaCancion', '#MusicaOriginal', '#EstrenoMusical',
            '#CancionDelDia', '#MusicaViral', '#PlaylistNueva',
            '#MusicaIndependiente', '#EscuchaYa', '#HitDelMomento']

    elif 'Video'.lower() == tipo_de_contenido['tipo_de_contenido'].lower():
        return ['#NuevoVideo', '#ContenidoCreativo', '#VideoEstreno',
            '#YouTubeMusic', '#VideoOficial', '#TrendingVideo',
            '#VisualesUnicos', '#MiraYa', '#VideoClip']
    else:
        print('Elige una opcion valida')
        return None


def guardar_promociones(contenido, plataforma, texto, hashtags):
    promocione_guardar = {'contenido': contenido, 'plataforma': plataforma, 'texto': texto, 'hashtags': hashtags}
    promociones.append(promocione_guardar)



def ver_promociones():
    print('======Promociones======\n')
    if not promociones:
        print('No hay promociones para mostrar')
        return
    else:
        for promocion in promociones:
            print('=====================')
            print('Promocion')
            print('=====================')
            print(f'Contenido:\n{promocion["contenido"]}\n')
            print(f'Plataforma:\n{promocion['plataforma']}\n')
            print(f'Texto\n{promocion['texto']}\n')
            print(f'Hashtags:\n{promocion['hashtags']}\n')






while True:
    menu()
    seleccion_menu = validar_opcion()
    if seleccion_menu == 1:
        registrar_contenido()
    elif seleccion_menu == 2:
        mostrar_contenidos()
    elif seleccion_menu == 3:
        crear_promocion()
    elif seleccion_menu == 4:
        ver_promociones()
    elif seleccion_menu == 5:
        print('Gracias por utilizar MusicPromoter v1.0')
        break
    else:
        print('Elige una opcion valida')



