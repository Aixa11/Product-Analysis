import PyPDF2

# Función para extraer texto del PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Función para realizar el análisis SWOT
def analyze_swot(text):
    swot = {
        "Strengths": [],
        "Weaknesses": [],
        "Opportunities": [],
        "Threats": []
    }
    
    # Listas de palabras clave
    strengths_keywords = ["fortaleza", "bueno", "ventaja", "sólido", "robusto", "excelente"]
    weaknesses_keywords = ["debilidad", "malo", "desventaja", "frágil", "deficiente", "problema"]
    opportunities_keywords = ["oportunidad", "crecimiento", "potencial", "desarrollo", "expansión", "nuevo mercado"]
    threats_keywords = ["amenaza", "riesgo", "competencia", "desafío", "peligro", "obstáculo"]
    
    # Función para buscar palabras clave en el texto
    def search_keywords(keywords, category):
        for keyword in keywords:
            if keyword in text.lower():
                swot[category].append(f"Palabra clave encontrada: {keyword}")
    
    # Búsqueda de palabras clave en el texto
    search_keywords(strengths_keywords, "Strengths")
    search_keywords(weaknesses_keywords, "Weaknesses")
    search_keywords(opportunities_keywords, "Opportunities")
    search_keywords(threats_keywords, "Threats")
    
    # Análisis detallado basado en el contenido del texto
    if "buenos resultados en las pruebas de concepto" in text:
        swot["Strengths"].append("Buenos resultados en las pruebas de concepto y demostraciones.")
    if "uso de técnicas de Visión por Computadora y Aprendizaje Automático" in text:
        swot["Strengths"].append("Uso de técnicas avanzadas como Visión por Computadora y Aprendizaje Automático.")
    
    if "falta de conocimientos y herramientas" in text:
        swot["Weaknesses"].append("Falta de conocimientos y herramientas para abordar la compactación del suelo.")
    
    if "solución sistémica de la compactación" in text:
        swot["Opportunities"].append("Desarrollo de una solución sistémica para la compactación que actualmente no existe en el mercado.")
    if "medición remota de compactación de suelos agrícolas" in text:
        swot["Opportunities"].append("Medición remota de compactación de suelos agrícolas utilizando imágenes satelitales.")
    
    if "empresas extranjeras que realicen servicios similares" in text:
        swot["Threats"].append("Competencia de empresas extranjeras que realizan servicios similares.")
    if "requerimientos mínimos y establecer su valor de mercado inicial" in text:
        swot["Threats"].append("Necesidad de definir requerimientos mínimos y establecer un valor de mercado inicial competitivo.")
    
    return swot

# Ruta al documento PDF
pdf_path = './Análisis Comercial.pdf'

# Extraer texto del PDF
text = extract_text_from_pdf(pdf_path)

# Realizar análisis SWOT
swot_analysis = analyze_swot(text)

# Imprimir análisis SWOT
print("Análisis SWOT:")
for key, values in swot_analysis.items():
    print(f"\n{key}:")
    for value in values:
        print(f"- {value}")
