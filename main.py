#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning

def test_site(url):
    r = requests.get(url, verify=False)
    return r.status_code

def run():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
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
    
    for site in sites:
        print(f"Site: {site['nome']} - {site['url']} = Status: {test_site(site['url'])}")

def main():
    """ Main program """
    run()
    return 0

if __name__ == "__main__":
    main()