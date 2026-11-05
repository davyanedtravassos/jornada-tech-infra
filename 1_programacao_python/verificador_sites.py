import urllib.request

sites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.ifpb.edu.br",
    "https://site-que-nao-existe-12345.com",
]

for site in sites:
    try:
        resposta = urllib.request.urlopen(site, timeout=5)
        if resposta.status == 200:
            print("✅ No ar:", site)
        else:
            print("❌ Problema:", site)
    except Exception:
        print("❌ Fora do ar:", site)
