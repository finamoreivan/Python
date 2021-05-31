from instabot import Bot
bot = Bot()
bot.login(username="finamoreivan", password="1994dcworld")

# Subir Foto #

# bot.upload_photo(#"ubicación de la foto .jpg", caption="Agrega la descrición aquí")

# Seguir a alguien #

# bot.follow("UsuarioASeguir")

# Enviar un mensaje privado #

# bot.send_message("Mensaje de prueba desde un programa. Hola.", ["usuarioDeDestino"])

# Información de la cuenta (Seguidores) #

'''mis_seguidores = bot.get_user_followers("finamoreivan")
for seguidor in mis_seguidores:
    print(seguidor)'''

# Dejar de seguir a todos #

# bot.unfollow_everyone() '''

# Para volver a utilizar eliminar el archivo "usuario_uuid_and_cookie" de la carpeta config.
