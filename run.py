from app import app
import os

if __name__ == '__main__':
	if os.environ.get('APP_LOCATION') == 'heroku':
		app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
	else:
		app.run(host='localhost', port=8889, debug=True, reloader=True)

#Servidor_Castelo_Ad; Servidor_Castelo_Blue; Servidor_Castelo_Blue_Antigo; Servidor_Castelo_RH; Ips_Liberados; Ips_Liberados_Stoky; 192.168.105.86;192.168.105.20
