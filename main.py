#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def test_site(url):
    r = requests.get(url, verify=False)
    return r.status_code

def run():
    sites = [
        {"nome": "cliente-havan", "url": "https://cliente.havan.com.br/"},
        {"nome": "lista-havan", "url": "https://lista.havan.com.br/"},
        {"nome": "transaction", "url": "https://transaction.havan.com.br/"},
        {"nome": "correio-entancar-api", "url": "https://correioencantarapi.apps.havan.com.br/"},
        {"nome": "ficha-oferta", "url": "https://fichaoferta.apps.havan.com.br/health"},
        {"nome": "meuspedidos", "url": "https://meuspedidos.apps.havan.com.br/"},
        {"nome": "pixhavan", "url": "https://pixhavanapi.apps.havan.com.br/health"},
        {"nome": "cobranca-externa-api", "url": "https://cobrancaexternaapi.apps.havan.com.br/health"}
    ]
    
    status = []
    
    for site in sites:
        status.append({"nome": site['nome'],"url":site['url'],"status":test_site(site['url'])})
        
    return status

def main():
    run()
    return 0

if __name__ == "__main__":
    main()