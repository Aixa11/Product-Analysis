import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from textblob import TextBlob

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Función para extraer comentarios desde una página web
def extract_comments_from_web(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Ajustar los selectores según la estructura HTML de la página web
    comments_html = soup.select('.comment-class')  # Ajustar '.comment-class' según el sitio web
    comments = [comment.get_text() for comment in comments_html]
    return comments

# Ruta al archivo PDF
pdf_path = "./Análisis Comercial.pdf"
# URL de la página web de la empresa
web_url = "https://www.sitiowebcompetidor.com"

# Extraer texto del PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Aquí se deben identificar y extraer los comentarios específicos del PDF
# Ejemplo con comentarios hipotéticos extraídos del texto PDF
pdf_comments = [
    "El producto es muy útil y eficiente.",
    "No estoy satisfecho con la precisión.",
    "Excelente herramienta para la agricultura."
]

# Extraer comentarios desde la página web
web_comments = extract_comments_from_web(web_url)

# Combinar todos los comentarios
all_comments = pdf_comments + web_comments

# Analizar los sentimientos de los comentarios
sentiments = [TextBlob(comment).sentiment.polarity for comment in all_comments]

# Imprimir los comentarios con su sentimiento
for comment, sentiment in zip(all_comments, sentiments):
    print(f"Comentario: {comment} - Sentimiento: {'Positivo' if sentiment > 0 else 'Negativo' if sentiment < 0 else 'Neutral'}")
