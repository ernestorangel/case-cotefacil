import scrapy
from scrapy.http import FormRequest
import nacl.encoding
import nacl.hash


class ProductSpider(scrapy.Spider):
  name = 'products'

  def start_requests(self):
    login_url = 'https://www.compra-agora.com/cliente/logar'
    # yield scrapy.Request(login_url, callback=self.login) 
    
    data = nacl.encoding.HexEncoder.encode("{'username': '04.502.445/0001-20', 'password': '85243140'}")
    
    self.logger.info("Realizando login...")
    
    yield FormRequest(
      url=login_url,
      method='POST',
      headers={
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.compra-agora.com',
      },
      formdata=data,
      callback=self.category
    )

  # def login(self, response):
  #   self.logger.info("Realizando login...")
  #   #token = response.css('input#recaptcha-token').attrib['value']
  #   data = nacl.encoding.HexEncoder.encode({
  #     #'recaptcha_token': token, 
  #     'username': '04.502.445/0001-20', 
  #     'password': '85243140'
  #   })
  #   self.logger.info("data: " + data)
  #   yield FormRequest.from_response(response, formdata=data, callback=self.category) 

  def category(self, response):
    categories = []
    
    for category in response.css('li.lista-menu-itens'):
      categories.append({
        'name': category.css('a::text').getall()[1].strip('\\').strip('n').strip(),
        'url': category.css('a').attrib['href']
      })
    
    self.logger.info("Buscando itens por categoria")
    for category in categories:
      self.logger.info("Capturando produtos da categoria: " + category['name'])
      yield scrapy.Request(category['url'], callback=self.start_scraping, meta={'cat': category['name']})


  def start_scraping(self, response):
    products = response.css('div.box-produto').getall()
    products_info = []
    product_info = {}
    
    for product in products:
      
      try:
        product_info = {
          'categoria': response.meta.get('cat'),
          'descricao': product.css('a.produto-nome::text').get().strip('\\').strip('n').strip(),
          'fabricante': product.css('a.produto-marca::text').get(),
          'image_url': product.css('img').attrib['src'],
        }
      except:
        product_info = {
          'descricao': 'none',
          'fabricante': 'none',
          'image_url': 'none',
        }
      
      products_info.append(product_info)
      yield product_info

    self.logger.info(products_info)

  #   next_page_button = response.css('button#btnCarregarMais').get()
  #   if next_page_button is not None:
  #     previous_url = response.request.url
  #     auxList = previous_url.split('=')
  #     # next_url = auxList[0] + '=' + int(auxList[1] + 1)
  #     auxList[1] = str(int(auxList[1]) + 1)
  #     next_url = '='.join(auxList)
  #     yield response.follow(next_url, callback=self.start_scraping)