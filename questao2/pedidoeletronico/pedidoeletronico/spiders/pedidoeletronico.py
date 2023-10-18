import scrapy
from scrapy.http import Request
import json
import sys


order_input = str(sys.argv[2])

#order_input = '511082'

class PedidoEletronicoSpider(scrapy.Spider):
  
  name = 'pedidoeletronico'
  
  def start_requests(self):

    url = 'https://peapi.servimed.com.br/api/usuario/login'

    headers = {
      "authority": "peapi.servimed.com.br",
      "accept": "application/json, text/plain, */*",
      "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
      "content-type": "application/json",
      "contenttype": "application/json",
      "loggeduser": "0",
      "origin": "https://pedidoeletronico.servimed.com.br",
      "referer": "https://pedidoeletronico.servimed.com.br/",
      "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-site",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    cookies = {
      "_gid": "GA1.3.1774520588.1697567708",
      "_gat": "1",
      "_gat_gtag_UA_149227611_1": "1",
      "_ga_0684EZD6WN": "GS1.1.1697585874.4.1.1697585998.0.0.0",
      "_ga": "GA1.1.2018043015.1697567708"
    }

    body = '{"usuario":"juliano@farmaprevonline.com.br","senha":"a007299A"}'
    
    self.logger.info("Realizando login...")

    yield Request(
      url=url,
      method='POST',
      dont_filter=True,
      cookies=cookies,
      headers=headers,
      body=body,
      callback=self.go_to_orders
    )
    
  def go_to_orders(self, response):
    
    if response.status == 200:
      self.logger.info("Login realizado com sucesso.")
    else:
      self.logger.warning("Falha no login.")
      
    url = 'https://peapi.servimed.com.br/api/Pedido'

    headers = {
      "authority": "peapi.servimed.com.br",
      "accept": "application/json, text/plain, */*",
      "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
      "accesstoken": "84f8f2f0-6d46-11ee-befb-dba7c7fd43b8",
      "content-type": "application/json",
      "contenttype": "application/json",
      "loggeduser": "22850",
      "origin": "https://pedidoeletronico.servimed.com.br",
      "referer": "https://pedidoeletronico.servimed.com.br/",
      "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-site",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    cookies = {
      "_gid": "GA1.3.1774520588.1697567708",
      "_ga_0684EZD6WN": "GS1.1.1697585874.4.1.1697585998.0.0.0",
      "_ga": "GA1.1.2018043015.1697567708",
      "sessiontoken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4NGY4ZjJmMC02ZDQ2LTExZWUtYmVmYi1kYmE3YzdmZDQzYjgiLCJpYXQiOjE2OTc1ODYwMTQsImV4cCI6MTY5NzYyOTIxNCwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.O-2uqPzAP95OTWZCTyCgTzS5OkS6m1ywqdmDrDB-fCvN0b-GUWjN3TVHxNdp-TOB__ty1JIxN6Ad55x-soR1Sg",
      "accesstoken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4NGY4ZjJmMC02ZDQ2LTExZWUtYmVmYi1kYmE3YzdmZDQzYjgiLCJpYXQiOjE2OTc1ODYwMTQsImV4cCI6MTY5NzYyOTIxNCwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.O-2uqPzAP95OTWZCTyCgTzS5OkS6m1ywqdmDrDB-fCvN0b-GUWjN3TVHxNdp-TOB__ty1JIxN6Ad55x-soR1Sg",
      "_gat": "1"
    }

    body = '{"dataInicio":"","dataFim":"","filtro":"","pagina":1,"registrosPorPagina":10,"codigoExterno":518565,"codigoUsuario":22850,"kindSeller":0,"users":[518565,267511]}'

    self.logger.info("Buscando pedidos...")
    
    yield Request(
      url=url,
      method='POST',
      dont_filter=True,
      cookies=cookies,
      headers=headers,
      body=body,
      callback=self.search_order
    )

  
  def search_order(self, response):
    
    if response.status == 200:
      self.logger.info("Pedidos encontrados com sucesso.")
    else:
      self.logger.warning("Falha ao buscar pedidos.")
    
    url = 'https://peapi.servimed.com.br/api/Pedido'

    headers = {
      "authority": "peapi.servimed.com.br",
      "accept": "application/json, text/plain, */*",
      "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
      "accesstoken": "84f8f2f0-6d46-11ee-befb-dba7c7fd43b8",
      "content-type": "application/json",
      "contenttype": "application/json",
      "loggeduser": "22850",
      "origin": "https://pedidoeletronico.servimed.com.br",
      "referer": "https://pedidoeletronico.servimed.com.br/",
      "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-site",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    cookies = {
      "_gid": "GA1.3.1774520588.1697567708",
      "_ga_0684EZD6WN": "GS1.1.1697585874.4.1.1697585998.0.0.0",
      "_ga": "GA1.1.2018043015.1697567708",
      "sessiontoken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4NGY4ZjJmMC02ZDQ2LTExZWUtYmVmYi1kYmE3YzdmZDQzYjgiLCJpYXQiOjE2OTc1ODYyMDEsImV4cCI6MTY5NzYyOTQwMSwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.TA8IgZ_ZGdExd2zFRMKTeDx13DO5tpLzJtw_oBuTV0FtIo1am9Y65XA7uvcVtPlLKiwjWKWEQ077oT1UvsoVfg",
      "accesstoken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4NGY4ZjJmMC02ZDQ2LTExZWUtYmVmYi1kYmE3YzdmZDQzYjgiLCJpYXQiOjE2OTc1ODYyMDEsImV4cCI6MTY5NzYyOTQwMSwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.TA8IgZ_ZGdExd2zFRMKTeDx13DO5tpLzJtw_oBuTV0FtIo1am9Y65XA7uvcVtPlLKiwjWKWEQ077oT1UvsoVfg"
    }

    body = f'{{"dataInicio":"","dataFim":"","filtro":"{order_input}","pagina":1,"registrosPorPagina":10,"codigoExterno":518565,"codigoUsuario":22850,"kindSeller":0,"users":[518565,267511]}}'

    self.logger.info(f"Buscando o pedido {order_input}...")
    
    yield Request(
      url=url,
      method='POST',
      dont_filter=True,
      cookies=cookies,
      headers=headers,
      body=body,
      callback=self.get_details
    )
    
  def get_details(self, response):
    
    if response.status == 200:
      self.logger.info(f"Pedido {order_input} encontrado com sucesso.")
    else:
      self.logger.warning(f"Falha ao encontrar o pedido {order_input}.")

    url = f'https://peapi.servimed.com.br/api/Pedido/ObterTodasInformacoesPedidoPendentePorId/{order_input}'

    headers = {
      "authority": "peapi.servimed.com.br",
      "accept": "application/json, text/plain, */*",
      "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
      "accesstoken": "84f8f2f0-6d46-11ee-befb-dba7c7fd43b8",
      "contenttype": "application/json",
      "loggeduser": "22850",
      "origin": "https://pedidoeletronico.servimed.com.br",
      "referer": "https://pedidoeletronico.servimed.com.br/",
      "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-site",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    cookies = {
      "_gid": "GA1.3.1774520588.1697567708",
      "_ga_0684EZD6WN": "GS1.1.1697585874.4.1.1697585998.0.0.0",
      "_ga": "GA1.1.2018043015.1697567708",
      "sessiontoken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4NGY4ZjJmMC02ZDQ2LTExZWUtYmVmYi1kYmE3YzdmZDQzYjgiLCJpYXQiOjE2OTc1ODYzMjYsImV4cCI6MTY5NzYyOTUyNiwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.lv_pVOSnC85rw66MDC5DWmZMKU4zUK_yafGrKAK6O4Md_AgX6U7aox1dWYd_OM44zFOEIeWPgqWnfFqEK30HfA",
      "accesstoken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2RpZ29Vc3VhcmlvIjoyMjg1MCwidG9rZW4iOiI4NGY4ZjJmMC02ZDQ2LTExZWUtYmVmYi1kYmE3YzdmZDQzYjgiLCJpYXQiOjE2OTc1ODYzMjYsImV4cCI6MTY5NzYyOTUyNiwiYXVkIjoiaHR0cDovL3NlcnZpbWVkLmNvbS5iciIsImlzcyI6IlNlcnZpbWVkIiwic3ViIjoic2VydmltZWRAU2VydmltZWQuY29tLmJyIn0.lv_pVOSnC85rw66MDC5DWmZMKU4zUK_yafGrKAK6O4Md_AgX6U7aox1dWYd_OM44zFOEIeWPgqWnfFqEK30HfA"
    }
    
    self.logger.info(f"Buscando detalhes do pedido {order_input}...")

    yield Request(
      url=url,
      method='GET',
      dont_filter=True,
      cookies=cookies,
      headers=headers,
      callback=self.scrape_info
    )
  
  def scrape_info(self, response):
    
    if response.status == 200:
      self.logger.info(f"Detalhes do pedido {order_input} encontrados com sucesso.")
    else:
      self.logger.warning(f"Falha so buscar detalhes do pedido {order_input}.")
      
    json_response = json.loads(response.text)
    
    itens = []
    for item in json_response["itens"]:
      itens.append({
        "codigo_produto": item["produto"]["codigoExterno"],
        "descricao": item["produto"]["descricao"],
        "quantidade_faturada": item["quantidadeFaturada"]
      })
      
    self.logger.info(f"Retornando detalhes do pedido {order_input}")
      
    yield {
      "motivo": str(json_response["rejeicao"]).strip(),
      "itens": itens
    }

    