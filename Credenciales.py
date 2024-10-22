import requests

# Credenciales de tu aplicación LinkedIn
CLIENT_ID = 'tu_client_id'
CLIENT_SECRET = 'tu_client_secret'
REDIRECT_URI = 'https://www.tu_callback_url.com'

# URL para obtener el código de autorización
authorization_url = (
    f'https://www.linkedin.com/oauth/v2/authorization'
    f'?response_type=code&client_id={CLIENT_ID}'
    f'&redirect_uri={REDIRECT_URI}&state=random_string&scope=r_liteprofile%20r_emailaddress%20w_member_social'
)

print('Visita esta URL para autorizar la aplicación:', authorization_url)

# Después de obtener el código de autorización, usa el siguiente código para obtener el token de acceso:

AUTHORIZATION_CODE = 'codigo_de_autorizacion_obtenido'  # Reemplaza esto con el código de autorización obtenido

# URL para obtener el token de acceso
access_token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

# Datos para obtener el token de acceso
data = {
    'grant_type': 'authorization_code',
    'code': AUTHORIZATION_CODE,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}

# Obtener el token de acceso
response = requests.post(access_token_url, data=data)
access_token = response.json().get('access_token')

if access_token:
    print('Token de acceso obtenido:', access_token)
else:
    print('Error al obtener el token de acceso:', response.json())
