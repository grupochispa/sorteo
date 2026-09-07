import qrcode

# La dirección web exacta que no cambiará
url = "https://grupochispa.github.io/sorteo/"

# Configuración del código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Nivel alto para que funcione incluso si se ensucia o daña un poco
    box_size=10,
    border=4,
)

# Añadir la URL al código QR
qr.add_data(url)
qr.make(fit=True)

# Generar la imagen (puedes cambiar los colores si lo deseas)
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en tu computadora
nombre_archivo = "qr_sorteo_grupochispa.png"
img.save(nombre_archivo)

print(f"¡Éxito! El código QR permanente se ha guardado como '{nombre_archivo}'")