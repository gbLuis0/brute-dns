from os import system, name
try:
    import dns.resolver
except:
    system('pip install dnspython')
finally:
    import dns.resolver


dns = dns.resolver.Resolver()

domain = input('Digite o domínio: ').strip().lower()

subd = input('caminho da wor')