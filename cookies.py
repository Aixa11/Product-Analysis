
import requests
from bs4 import BeautifulSoup

# URL de búsqueda en LinkedIn con un término de búsqueda más específico
search_url = "https://www.linkedin.com/search/results/companies/?keywords=soil%20compaction%20agriculture%20technology"

# Headers para parecer una solicitud de navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Cookies de la sesión autenticada
cookies = {
    'li_at': 'AQEDASnDxyoBzUxbAAABkHidJE8AAAGQnKmoT00A0mHVm7pdZ_m8cZ2N9kdlTGafcssqUHHyvpK_iDGKrpoMBq8Fb0FbeWmuRbhhRVuTrJApHQazUE-Pczx87C3GX3FHHNzbFQqivVaz8CbKCHbDDwv0',  # Reemplaza esto con tu cookie de sesión de LinkedIn
    # Añade otras cookies necesarias aquí
}

# Realizar la solicitud
response = requests.get(search_url, headers=headers, cookies=cookies)
soup = BeautifulSoup(response.content, 'html.parser')

# Filtrar resultados (esto es un ejemplo simplificado, la estructura HTML real puede variar)
companies = soup.find_all('div', class_='entity-result__content')

company_profiles = []

for company in companies:
    name_tag = company.find('span', class_='entity-result__title-text')
    location_tag = company.find('span', class_='entity-result__primary-subtitle')
    description_tag = company.find('p', class_='entity-result__summary')
    
    if name_tag and location_tag and description_tag:
        name = name_tag.text.strip()
        location = location_tag.text.strip()
        description = description_tag.text.strip()
        
        # Filtros basados en el documento PDF
        if "pampa húmeda" in location.lower() or "agricultural" in description.lower():
            profile_url = company.find('a', class_='app-aware-link')['href']
            company_profiles.append({'name': name, 'location': location, 'description': description, 'profile_url': profile_url})

print("Empresas encontradas:")
for profile in company_profiles:
    print(f"Empresa: {profile['name']}, Ubicación: {profile['location']}, Descripción: {profile['description']}, URL: {profile['profile_url']}")
