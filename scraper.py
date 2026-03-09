import requests
from bs4 import BeautifulSoup
import csv
# URL da seção de placas de vídeo na Kabum
url = 'https://www.kabum.com.br/hardware/placa-de-video-vga'
# Função para fazer a requisição HTTP e obter o conteúdo da página
def get_page_content(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    return response.content
    except requests.exceptions.RequestException as e:
      print(f"Erro ao acessar a página: {e}")
      return None
      # Função para extrair os dados dos produtos
      def extract_product_data(content):
        try:
          soup = BeautifulSoup(content, 'html.parser')
          products = soup.find_all('div', class_='productCard')
data = []
for product in products:
  name = product.find('h2').text.strip()
price = product.find('span', class_='priceCard').text.strip()
data.append({'Nome': name, 'Preço': price})
return data
except Exception as e:
print(f"Erro ao extrair os dados: {e}")
return []
# Função para salvar os dados em um arquivo CSV
def save_to_csv(data):
  try:
    with open('placas_de_video.csv', 'w', newline='', encoding='utf-8')
    as csvfile:
      fieldnames = ['Nome', 'Preço']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      for row in data:
        writer.writerow(row)
        print("Dados salvos com sucesso em 'placas_de_video.csv'.")
        except Exception as e:
          print(f"Erro ao salvar os dados em CSV: {e}")
          # Fluxo principal do programa
          def main():
            page_content = get_page_content(url)
            if page_content:
              product_data = extract_product_data(page_content)
              save_to_csv(product_data)
              if __name__ == "__main__":
                main()
