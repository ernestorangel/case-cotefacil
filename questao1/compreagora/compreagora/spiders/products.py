import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request
import nacl.encoding
import nacl.hash
import json

class ProductSpider(scrapy.Spider):
  name = 'products'
  
  produtos = []

  def start_requests(self):

    url = 'https://www.compra-agora.com/cliente/logar'

    headers = {
        "authority": "www.compra-agora.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwOTcxNjciLCJhcCI6IjExMzQxOTY2MDciLCJpZCI6IjcwNzQ5ZDM3MmU1YmU2ZGQiLCJ0ciI6Ijk5YWQzMTMzZDIwZTA3ZGZiNjAzNzgwODZkZWE4YWM4IiwidGkiOjE2OTc2MDA0ODczMzZ9fQ==",
        "origin": "https://www.compra-agora.com",
        "referer": "https://www.compra-agora.com/",
        "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "traceparent": "00-99ad3133d20e07dfb60378086dea8ac8-70749d372e5be6dd-01",
        "tracestate": "3097167@nr=0-1-3097167-1134196607-70749d372e5be6dd----1697600487336",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    cookies = {
        "_gcl_au": "1.1.789191038.1697070740",
        "nav_id": "b063cba6-2b88-436d-be32-be3290e72350",
        "_pm_id": "683501697070739814",
        "legacy_p": "b063cba6-2b88-436d-be32-be3290e72350",
        "chaordic_browserId": "b063cba6-2b88-436d-be32-be3290e72350",
        "legacy_c": "b063cba6-2b88-436d-be32-be3290e72350",
        "legacy_s": "b063cba6-2b88-436d-be32-be3290e72350",
        "_fbp": "fb.1.1697070739995.1447552808",
        "_vwo_uuid_v2": "D956078A43BC98D35F932A23DF4E86DEB|9f5f4302a626454412937f73ab72a833",
        "_tt_enable_cookie": "1",
        "_ttp": "QG5ODYf7MsrHXPWrh5NfW6gSTSz",
        "_hjSessionUser_3232779": "eyJpZCI6IjZkYmE2NjhlLTAzZmUtNWI5My05Zjc3LTc2NGIyZDRlZjMyYiIsImNyZWF0ZWQiOjE2OTcwNzA3NDA5NzUsImV4aXN0aW5nIjp0cnVlfQ==",
        "chaordic_anonymousUserId": "anon-b063cba6-2b88-436d-be32-be3290e72350",
        "chaordic_testGroup": "%7B%22experiment%22%3Anull%2C%22group%22%3Anull%2C%22testCode%22%3Anull%2C%22code%22%3Anull%2C%22session%22%3Anull%7D",
        "usrfgpt": "045024450001201697465069",
        "mp_374315cbd6a8184d0bcfdd0f2a579e0e_mixpanel": "%7B%22distinct_id%22%3A%20113953%2C%22%24device_id%22%3A%20%2218b38cd7bd4a4ce1-01df8bc88dde6a-26031151-1fa400-18b38cd7bd4a4ce1%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20113953%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.compra-agora.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.compra-agora.com%22%7D",
        "PHPSESSID": "1fbk4qogvv8ktq0id2dqaf6bpv",
        "_gid": "GA1.2.1050502628.1697600374",
        "_pm_sid": "916501697600373989",
        "tfpsi": "15428dbe-117f-40a4-a13f-04c09fba66e9",
        "dicbo_fetch": "true",
        "_hjIncludedInSessionSample_3232779": "1",
        "_hjSession_3232779": "eyJpZCI6IjRjOTUwMTk4LWEyYTItNGQwMy04MDU4LTEzNDRiYThmODFjZSIsImNyZWF0ZWQiOjE2OTc2MDAzNzU4MDAsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=",
        "_hjAbsoluteSessionInProgress": "0",
        "impulsesuite_session": "1697600376660-0.8885422322147292",
        "voxusmediamanager_id": "16834988756160.2898742213548291uke55wl1kxr",
        "voxusmediamanager__ip": "186.222.69.243",
        "ca05-pesquisou": "-",
        "shownModalAprovacaoVendedoresPendentes": "true",
        "aceite_politicas_cookie": "2023-10-18%2000:39:59",
        "lx_sales_channel": "%5B%22default%22%5D",
        "loginTentativa": "true",
        "_gat_UA-77097824-7": "1",
        "_uetsid": "f45401606d6711ee9b8c752932a1881d",
        "_uetvid": "cdd59b10689611eeb799b5ef9460e740",
        "_ga": "GA1.1.1991479225.1697070740",
        "_dc_gtm_UA-77097824-7": "1",
        "cto_bundle": "FTXy5F9vY3cxRlNLVDdNekRTN3FwMXdJczJKQmdTbU9WZWxwV3J4RnkyayUyQjVxMG1MQnklMkJxRjRtTkFxMDdMS3BSVnFwc1pTYmRrS1V6aW1PYVpCTlE4UWRGdGJVd244SGVLZUZUS0ZTd00ySmlLWjhRdGFrS1NxbUs5RU5jJTJCbiUyRiUyQnNETjJoSkJLaVF3anpZcmF3cnI0RFRKQ0Q4QVhUYnhKWXVUMzVhUElWNFNYTVd6NWx4SlRCY0V5cnVZYmJqcDVqVEtHUzlaNjg2Z1NZOTdNbHZFOWRoVm9vRWclMkIwSG5BNHJJc0w1NkhxRG10JTJGYll3Y25sTG1zc1pJazg3RnFXZ1R0SWVFbWhGbmdTUW8lMkZtSmpCUiUyRmtyR1hPZyUzRCUzRA",
        "_pm_m": "c04502445000120",
        "_ga_5LTWWHFGYX": "GS1.1.1697600374.9.1.1697600474.44.0.0"
    }

    body = 'data=7f240aeda63f9464bf68eabe0dc1053b4f658df109baaa76dc4afbe56a987e27725cdcd2718fdae1a24380f3c038544cb424b3a7daeceebc1941cd322ef560b0936c8a6ce2c0da9d5b4a0ae2bf440619ab600f4d71a03809775f99f0a6f0c932023b9c236e210d1ac4d10ff09f77b07f2cc458d02989f42257258c94c83605f97d86b730aa373884cb86e345f97341adbe110015ae3d9403ce6d6ae31ea9a51fe99c31c9b7295930e96f221dcac574bc51c00d069dd1cd00d2975c7c650a4d50fec4ff513591002a865b0e288c1a4367bc19dc6bd214c4284425d3086a818444fe49c17d7c8edd961b616cefa12098fa5b48c4d4c9c4bd99d96de1edb0e6b49abcb9a02c82ba4cf3cf3ae1d721d4d7f13fe78387206048a8213d1bfc1d7c9b128efaa321efb731bb280e0c6161eecb437a00a199d521e4e7b75a69efe32b463fe68115cdf34fa746c6de6cb80a42507c8d05480365a49f42dfdd66ff47c4e34c9dd0aa48b8f126e921053700ca5aca117f026a5f87b058d95a91fdff597ff64e064575f80f749dffa44f6c497f4e2a6714e7c493817234e86f42dcc25adc2bb4d4cff0e0826eb49709e7fb54db2cba1da5cafea1932b54245ce0e4b66fe3cebc36b22ec27e0d40fe8a41355bb39f7ed558c03dfb8c0282493eb2fde085af929ca7666a340808815722931e2470e3882c137ad567c00008f28158a6f74f31db0e14ccdecaf0357aa0e376f0fadf0402c7ceec3172e21fec6b8cf3fd89297893a2a2a318a3fab7b8fc21ca0a73128aa1efa7361da3ad07b9fa5c8bb2ca13798bcca67a5551575aa737e3474dcb7d974fa53a0b6ab2e742f937287e7d3df8ca49a286f44af2c9db8899e98c762f4cfcba837d86bd5a8f0c10541bf56fed7ba0cf3f1e356252d532121add016340c0fd0a5fc65fb50f959bef11908c5e084ae9112e30f77095ca17942b34b1a8132b003cdc6f81b101b0247f7e2570050521aa2c722e12637fdb030d133e57a4af1f12fe44465ae623d97f5e25e094fb1497dd57d3bbb1d4fb5918b55d155e2296797f799a01f0293f8acea3c616452f03ea61d41694e3977a567cd3bcbee664e50b41ae63737d1e86cd367130465f0745eb581912c8'

    self.logger.info("Realizando login...")
    
    yield Request(
      url=url,
      method='POST',
      dont_filter=True,
      cookies=cookies,
      headers=headers,
      body=body,
      callback=self.enter_page
    )
  
  def enter_page(self, response):
    url = 'https://www.compra-agora.com/'
    yield Request(url, callback=self.get_categories)

  def get_categories(self, response):
    
    if response.status == 200:
      self.logger.info("Login realizado com sucesso.")
    else:
      self.logger.warning("Falha ao realizar login.")
      
    categories = []
    
    for category in response.css('li.lista-menu-itens'):
      categories.append({
        'name': category.css('a::text').getall()[1].strip('\\').strip('n').strip(),
        'url': "/".join(category.css('a').attrib['href'].split('/')[-2:])
      })
    
    print(categories)
    
    self.logger.info("Buscando itens por categoria...")
    for category in categories:
      #self.logger.info("Capturando produtos da categoria: " + category['name'])
      print(category['url'])
      url = 'https://www.compra-agora.com/api/catalogproducts/' + category['url']

      headers = {
          "authority": "www.compra-agora.com",
          "accept": "application/json, text/plain, */*",
          "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
          "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwOTcxNjciLCJhcCI6IjExMzQxOTY2MDciLCJpZCI6ImQ5NzA3YjgzYTJkMmEwOGUiLCJ0ciI6IjE5NTA4NTQwNjEyNWIxY2ZhNTA1ZDc0Y2FhNWZkYTVjIiwidGkiOjE2OTc2MDMxODY3NTJ9fQ==",
          "referer": "https://www.compra-agora.com/loja/bebidas/778",
          "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": "\"Windows\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "traceparent": "00-195085406125b1cfa505d74caa5fda5c-d9707b83a2d2a08e-01",
          "tracestate": "3097167@nr=0-1-3097167-1134196607-d9707b83a2d2a08e----1697603186752",
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
      }

      cookies = {
          "_gcl_au": "1.1.789191038.1697070740",
          "nav_id": "b063cba6-2b88-436d-be32-be3290e72350",
          "_pm_id": "683501697070739814",
          "legacy_p": "b063cba6-2b88-436d-be32-be3290e72350",
          "chaordic_browserId": "b063cba6-2b88-436d-be32-be3290e72350",
          "legacy_c": "b063cba6-2b88-436d-be32-be3290e72350",
          "legacy_s": "b063cba6-2b88-436d-be32-be3290e72350",
          "_fbp": "fb.1.1697070739995.1447552808",
          "_vwo_uuid_v2": "D956078A43BC98D35F932A23DF4E86DEB|9f5f4302a626454412937f73ab72a833",
          "_tt_enable_cookie": "1",
          "_ttp": "QG5ODYf7MsrHXPWrh5NfW6gSTSz",
          "_hjSessionUser_3232779": "eyJpZCI6IjZkYmE2NjhlLTAzZmUtNWI5My05Zjc3LTc2NGIyZDRlZjMyYiIsImNyZWF0ZWQiOjE2OTcwNzA3NDA5NzUsImV4aXN0aW5nIjp0cnVlfQ==",
          "chaordic_anonymousUserId": "anon-b063cba6-2b88-436d-be32-be3290e72350",
          "chaordic_testGroup": "%7B%22experiment%22%3Anull%2C%22group%22%3Anull%2C%22testCode%22%3Anull%2C%22code%22%3Anull%2C%22session%22%3Anull%7D",
          "usrfgpt": "045024450001201697465069",
          "_gid": "GA1.2.1050502628.1697600374",
          "_pm_sid": "916501697600373989",
          "tfpsi": "15428dbe-117f-40a4-a13f-04c09fba66e9",
          "_hjSession_3232779": "eyJpZCI6IjRjOTUwMTk4LWEyYTItNGQwMy04MDU4LTEzNDRiYThmODFjZSIsImNyZWF0ZWQiOjE2OTc2MDAzNzU4MDAsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjpmYWxzZX0=",
          "_hjAbsoluteSessionInProgress": "0",
          "impulsesuite_session": "1697600376660-0.8885422322147292",
          "voxusmediamanager_id": "16834988756160.2898742213548291uke55wl1kxr",
          "ca05-pesquisou": "-",
          "aceite_politicas_cookie": "2023-10-18%2000:39:59",
          "ccw": "2 3 39 94 147 235 558 595 606 760 798 800 831 837",
          "CPL": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpbmZyYWNvbW1lcmNlLmNvbS5iciIsInN1YiI6IkluZnJhY29tbWVyY2UiLCJhdWQiOiJjb21wcmEtYWdvcmEuY29tIiwiaWF0IjoxNjk3NjAwNDg5LCJkYXRhIjp7InVpZCI6IndPdmN1dzZDeFNsYlpOWHI3MDFQelE9PSJ9fQ.Ob50YJDltbkSvFd-_v2WSpG_1_xCBu-qhJQg4k-s-ecywlkcb4j1TOqazAvxRuDveXcuUuWB90cMVDobFjNN3kEnOmVKG1xB--Sr0Z_7H1cfX7544p4LjRTlheUOZtNthM0EO0jqNn_0Erwa7seMWo-BoE4tzBfyv5MM9G8yDSc1zf68NeBERkDGxD9UqY_-4X9DQQM6FSVSan7MUyf_pCRho7y01WUlFJ_yP5pu-RzREYjNfv9aicbp5teZXUsQrUE4MYHSaCeIkSpv5zJgu3w8QMpSp73XaOcm4JjZYIHe7D_IC4Vle0rp7mKw9tgPFr5eHMDUr22n5o5wH9A1vA",
          "PHPSESSID": "2j38v9fit7ca3q5q2in6bgh3jf",
          "mp_374315cbd6a8184d0bcfdd0f2a579e0e_mixpanel": "%7B%22distinct_id%22%3A%20113953%2C%22%24device_id%22%3A%20%2218b38cd7bd4a4ce1-01df8bc88dde6a-26031151-1fa400-18b38cd7bd4a4ce1%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20113953%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.compra-agora.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.compra-agora.com%22%7D",
          "shownModalAprovacaoVendedoresPendentes": "true",
          "chaordic_realUserId": "113953",
          "lx_sales_channel": "%5B%22unilever-fr-235%22%2C%22unilever-pc-147%22%2C%22unilever-fs-235%22%2C%22unilever-professionals-235%22%2C%22unilever-pi-147%22%2C%22gsk-pc-235%22%2C%22unilever-bw-147%22%2C%22unilever-hc-235%22%2C%22unilever-mtmgdb-235%22%2C%22kibon-ic-94%22%2C%22camil-fr-39%22%2C%22henkel-acc-595%22%2C%22diageo-bebidas-831%22%2C%22Selmi-Total-Todeschini-Biscoitos-39%22%2C%22Selmi-Todeschini-Biscoitos-39%22%2C%22Selmi-Biscoitos-800%22%2C%22Selmi-Total-Biscoitos-800%22%2C%22Faber-Castell-Papelaria-39%22%2C%22lactalis-fr-837%22%2C%22ontex-pc-3%22%2C%22condor-hc-760%22%2C%22condor-pc-760%22%2C%22jmacedo-fr-2%22%2C%22riclan-fr-760%22%2C%22ul-international-pc-3%22%2C%22sococo-fr-39%22%2C%22brf-fr-235%22%2C%22haribo-fr-39%22%2C%22predilecta-fr-837%22%2C%22piracanjuba-leites-fr-3%22%2C%22piracanjuba-queijos-fr-3%22%2C%22piracanjuba-kids-fr-3%22%2C%22piracanjuba-mercearia-fr-3%22%2C%22piracanjuba-especiais-fr-3%22%2C%22piracanjuba-farma-fr-3%22%2C%22predilecta-stella-d-oro-fr-837%22%2C%22predilecta-so-fruta-fr-837%22%2C%22predilecta-salsaretti-fr-837%22%2C%22predilecta-salatta-show-fr-837%22%2C%22predilecta-sacciali-fr-837%22%2C%22predilecta-predilecta-fr-837%22%2C%22predilecta-minas-mais-fr-837%22%2C%22predilecta-hops-fr-837%22%2C%22predilecta-etti-fr-837%22%2C%22predilecta-carpe-etiam-fr-837%22%2C%22predilecta-cajamar-fr-837%22%2C%22predilecta-budweiser-fr-837%22%2C%22predilecta-avellana-fr-837%22%2C%22predilecta-showcau-fr-837%22%2C%22predilecta-sao-joao-fr-837%22%2C%22linea-fr-39%22%2C%22jimo-hc-3%22%2C%22total-quimica-hc-798%22%2C%22josapar-fr-39%22%2C%22prime-hair-concept-pc-3%22%2C%22consigaz-gas-606%22%2C%22swedishmatch-pc-3%22%2C%22swedishmatch-hc-3%22%2C%22swedishmatch-bazar-3%22%2C%22poly-play-bazar-3%22%2C%22poly-play-hc-3%22%2C%22chock-fr-3%22%2C%22embelleze-pc-3%22%2C%22suavipan-fr-3%22%2C%22genomma-lab-pc-3%22%2C%22coty-pc-3%22%2C%22ontex-dvl-3%22%2C%22camil-biscoitos-39%22%2C%22tok-bothanico-pc-3%22%5D",
          "_pm_m": "s958eec6c6a98884ba00335dd60ae9ff82ed19111529281ffff5446949be27567",
          "_hjIncludedInSessionSample_3232779": "1",
          "dicbo_fetch": "true",
          "_gat_UA-77097824-7": "1",
          "voxusmediamanager__ip": "186.222.69.243",
          "_dc_gtm_UA-77097824-7": "1",
          "_uetsid": "f45401606d6711ee9b8c752932a1881d",
          "_uetvid": "cdd59b10689611eeb799b5ef9460e740",
          "_ga": "GA1.1.1991479225.1697070740",
          "cto_bundle": "eaqFSF9vY3cxRlNLVDdNekRTN3FwMXdJczJFaG9LeWhyaXJwY2VLNzh0cWx4SEU3TmY5czhWQlpUT09mZjk5QSUyRnE2NHZ5RWw5YmtlbndIS05mWG56RUJ6QkZLM1BkZlZ2eVVpN0MzNmFzc3JGOEd2WiUyQkVkSU1DVnRReDkzNERyJTJGVTlKMnNtZlhMJTJGR0ltS2ZGcHp3ZTglMkJFJTJGU3pBSkhJWUlkMjBKd0JJY3dONlB6UDFqVzZWTTY5Zm54eGR4TVVGY3VFTW9mN1FPM28lMkYxOHNaQmhhWTB0UWV4bTB4ayUyRnkxUWZqc0g0NWJpamFzN2xLaGFST3RiaXBQdUI4YUVuVmYyczU0cWMwZnZxNUh2TFRHZHpweFR6WkNLT3clM0QlM0Q",
          "_ga_5LTWWHFGYX": "GS1.1.1697600374.9.1.1697603185.10.0.0"
      }

      yield Request(
          url=url,
          method='GET',
          dont_filter=True,
          cookies=cookies,
          headers=headers,
          callback=self.start_scraping,
          meta={'url': category['url'].split('/')[0]}
      )
      #yield Request(category['url'], callback=self.start_scraping)


  def start_scraping(self, response):
    
    json_response = json.loads(response.text)
  
  #   for produto in json_response["produtos"]:
  #     meta = {
  #       "descricao": produto["Nome"],
  #       "fabricante": produto["Marca"],
  #     }
  #     yield Request(produto["Url"], callback=self.get_image_url, meta=meta)
    
  # def get_image_url(self, response):
    
  #   self.produtos.append({
  #     "descricao": response.meta.get("descricao"),
  #     "fabricante": response.meta.get("fabricante"),
  #     "image_url": response.css('elevateImg').attrib('src')
  #   })

    with open(f"{response.meta.get('url')}.json", "w") as outfile:
      json.dump(json_response, outfile)

  #   next_page_button = response.css('button#btnCarregarMais').get()
  #   if next_page_button is not None:
  #     previous_url = response.request.url
  #     auxList = previous_url.split('=')
  #     # next_url = auxList[0] + '=' + int(auxList[1] + 1)
  #     auxList[1] = str(int(auxList[1]) + 1)
  #     next_url = '='.join(auxList)
  #     yield response.follow(next_url, callback=self.start_scraping)