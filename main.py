from os import system, name, getcwd
try:
    import dns.resolver
    from pyfiglet import Figlet
except:
    system('pip install dnspython pyfiglet')
finally:
    import dns.resolver
    from pyfiglet import Figlet

def cls():
    system('cls' if name == 'nt' else 'clear')

f = '\033[m'
verm = '\033[31;1m'
verd = '\033[32;1m'
dns = dns.resolver.Resolver()
banner = Figlet('slant').renderText('brute-dns')

per = 'y'
while per == 'y':
    cls()
    print('\033[34;1m'+banner+f)
    domain = input('Digite o domínio: ').strip().lower()
    cam = input('caminho da wordlist: (enter para inserir a wordlist da pasta) ').strip()
    if cam == '':
        cam = getcwd() + 'wordlist.txt'
    subdomains = open(cam, 'r').read().strip().splitlines()
    for s in subdomains:
        try:
            dom = s + '.' + domain
            res = dns.resolve(dom, 'A')
            for i in res:
                print(f'{dom} -> {verd}{i}{f}') 
        except:
            print(dom, verm + 'not found' + f + ' '*50, end='\r')
    per = input('Deseja voltar? [y/n] ').strip().lower()[0]
cls()
