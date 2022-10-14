import socket as c
import time 
import ping3 as p3

print("""
 █████ ███████████     █████                        █████   
░░███ ░░███░░░░░███   ░░███                        ░░███    
 ░███  ░███    ░███    ░███████    ██████   █████  ███████  
 ░███  ░██████████     ░███░░███  ███░░███ ███░░  ░░░███░   
 ░███  ░███░░░░░░      ░███ ░███ ░███ ░███░░█████   ░███    
 ░███  ░███            ░███ ░███ ░███ ░███ ░░░░███  ░███ ███
 █████ █████           ████ █████░░██████  ██████   ░░█████ 
░░░░░ ░░░░░           ░░░░ ░░░░░  ░░░░░░  ░░░░░░     ░░░░░  
                                                            
                                                            
                                                            
                                               █████        
                                              ░░███         
  █████   ██████   ██████   ████████   ██████  ░███████     
 ███░░   ███░░███ ░░░░░███ ░░███░░███ ███░░███ ░███░░███    
░░█████ ░███████   ███████  ░███ ░░░ ░███ ░░░  ░███ ░███    
 ░░░░███░███░░░   ███░░███  ░███     ░███  ███ ░███ ░███    
 ██████ ░░██████ ░░████████ █████    ░░██████  ████ █████   
░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░ ░░░░░

  creado por cholohatwhite : https://github.com/ch0l0hatwhite

            script de busqueda de ip por host

               usage example : google.com
""")
def hostprint():    
    sock=input("\n\033[32m[*] host a escanear > ")    
    p=c.gethostbyname(sock)
    print("\n[*] ip del sitio > "+p)
    sock1=("https://"+ sock) 
    print("\n[*] Enviando Paquetes...\n")
    
    for i in range(20):
        time.sleep(0.1)
        d=p3.ping(p)
        print("[*] El host tardo en responder > ",+d," segundos")                       
    hostprint()

try:
	hostprint()
except :
	print("\n\033[31m[*] Error! Intente nuevamente")
	hostprint()

    
