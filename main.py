from os import system, name
try:
    import dns.resolver
except:
    system('pip install dnspython')
finally:
    import dns.resolver

f = '\033[m'
verm = '\033[31;1m'
verd = '\033[32;1m'


dns = dns.resolver.Resolver()

domain = input('Digite o domínio: ').strip().lower()

cam = input('caminho da worldlist: ').strip()
subdomains = open(cam, 'r').read().strip().splitlines()

per = 's'
while per == 's':
    for s in subdomains:
        try:
            dom = s + '.' + domain
            res = dns.resolve(dom, 'A')
            for i in res:
                print(f'{dom} -> \033[32;1m{i}\033[m') 
        except:
            print(dom, '\033[31;1mnot found\033[m')
