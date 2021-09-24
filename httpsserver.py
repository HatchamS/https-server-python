import socketserver
import http.server
import ssl

adresse_serveur =("0.0.0.0",4443)

httpd = socketserver.TCPServer(adresse_serveur, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile="cert.pem",
                               keyfile="key.pem",
                               server_side=True
                               )
httpd.serve_forever()