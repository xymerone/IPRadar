from requests import get, post




def geo(ip):
	GEO_IP_URL = 'https://api.2ip.ua/geo.json?ip='
	GEO_IP_URL += ip
	res = get(GEO_IP_URL)
	if res.status_code == 200:
		return res.json()
	else:
		return {'error':"error response server"}

def provider(ip):
	PROVIDER_IP_URL = 'https://api.2ip.ua/provider.json?ip='
	PROVIDER_IP_URL += ip
	res = get(PROVIDER_IP_URL)
	if res.status_code == 200:
		return res.json()
	else:
		return {'error':"error response server"}

def show(title, dic):
	print(title)
	tab = '\t'
	for v, k in dic.items():
		if type(k) is dict:
			show('', k)
		elif type(k) is list:
			k = ', '.join(k)
		print(f"{tab} {v}: {k}")
	

while True:
	IP = input("IP: ")
	print(f"Show info to ip {IP}", end='\n\n')
	show('GEO Location.', geo(IP))
	print('\n')
	show('Provider info.', provider(IP))
	print('\n\n')
