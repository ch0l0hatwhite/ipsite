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
    print("\n")
    sock=input("Ingresa host a escanear > ")
    print("\n")
    p=c.gethostbyname(sock)
    print(" ip del site > "+p)
    sock1=("https://"+ sock)
    print("\n")
    print(" mandando paquetes de prueba.. ")
    print("\n")
    for i in range(15):
        time.sleep(1)
        d=p3.ping(p)
        print("El host tardo en responder > ",+d," segundos")
        print("\n")
        print("Prueba finalizada! ")
        
    hostprint()
hostprint()

    
