import argparse
from sys import argv
import dns.resolver
from os import system, name

verm = '\033[31;1m'
verd = '\033[32;1m'
f = '\033[m'
t = '\033[1;4m'

dns = dns.resolver.Resolver()

parser = argparse.ArgumentParser(
    prog='DNS brute',
    description='Programa de brute force para DNS; by: Spyware'
)

parser.add_argument(
    '-d','--domain', metavar=f'{t}DOMAIN{f}',
    help='Domínio usado para o brute force'
)

parser.add_argument(
    '-w', '--wordl', metavar=f'{t}WORDLIST{f}',
    help='Caminho da wordlist usada para o brute force (use cada subdomínio em linhas diferentes)'
)

parser.add_argument(
    '-n', '--notf', metavar=f'{t}False{f}',
    help='Para mostrar os domínios não encontrados, use este argumento (True)'
)

system('cls' if name == 'nt' else 'clear')

if len(argv) <= 1:
    parser.print_help()
    exit(0)

args = parser.parse_args()
if not args.wordl:
    args.wordl = 'wordlist.txt'
subdomains = open(args.wordl, 'r').read().strip().splitlines()
try:
    for s in subdomains:
            try:
                dom = s + '.' + args.domain
                res = dns.resolve(dom)
                print(f'{dom} ->                     '+''*20)
                for r in res:
                    print(f'{verd}{r}{f}')
                print()
            except:
                if args.notf:
                    print(dom, verm + 'not found' + f)
                else:
                    print(dom, verm + 'not found' + f + ' '*50, end='\r')
except:
    exit(0)
