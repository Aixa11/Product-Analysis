import requests
import json
from urllib.parse import urlencode

# Credenciales de tu aplicación LinkedIn
CLIENT_ID = 'tu_client_id'
CLIENT_SECRET = 'tu_client_secret'
REDIRECT_URI = 'https://www.tu_callback_url.com'
AUTHORIZATION_CODE = 'tu_authorization_code'

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

# Verificar si se obtuvo el token de acceso
if not access_token:
    print('Error al obtener el token de acceso')
    exit()

# Headers para las solicitudes a la API de LinkedIn
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# URL de búsqueda de empresas en LinkedIn
search_url = 'https://api.linkedin.com/v2/search?q=companies&keywords=agriculture%20technology'

# Realizar la solicitud de búsqueda
response = requests.get(search_url, headers=headers)
companies = response.json()

# Filtrar y mostrar los resultados
company_profiles = []

for company in companies.get('elements', []):
    name = company.get('title', {}).get('text', '')
    profile_url = company.get('url', '')
    location = company.get('location', {}).get('name', '')
    if 'Buenos Aires' in location or 'Argentina' in location:
        company_profiles.append({'name': name, 'profile_url': profile_url, 'location': location})

print("Empresas encontradas:")
for profile in company_profiles:
    print(f"Empresa: {profile['name']}, URL: {profile['profile_url']}, Ubicación: {profile['location']}")
