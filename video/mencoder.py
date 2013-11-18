import subprocess
import hashlib
mencoder = "/usr/bin/mencoder"  

def call_mencoder_mp4(fichero,destino):
    m = hashlib.md5()
    m.update(fichero)
    archivo = m.hexdigest()+".mp4"
    salida = destino+"/"+archivo
    print "Vamos a encodear %s y convertirlo en %s"%(fichero,salida)
    m = hashlib.md5()
    try:
        print "Lanzamos mencoder"
        subprocess.check_call(mencoder+" "+fichero+\
            " -oac copy -fafmttag 0x706D -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -o "+salida,\
            shell=True,stdin=open("/dev/null"),stderr=open("/dev/null"))
        return 0, archivo

    except Exception as e:
        print "Error",e
        return -1, None


def call_mencoder_flv(fichero):
    m = hashlib.md5()
    m.update(fichero)
    salida = m.hexdigest()+".flv"
    print "Vamos a encodear %s y convertirlo en %s"%(fichero,salida)
    m = hashlib.md5()
    try:
        print "lll"
        #subprocess.check_call(mencoder+" "+fichero+\
        #    " -oac copy -fafmttag 0x706D -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -o /tmp/output.avi ",\
        #    shell=True,stdin=open("/dev/null"),stderr=open("/dev/null"))
    except Exception as e:
        print "Error",e
        return -1


if __name__ == "__main__":
    print "somos main"
    fichero = "/home/patataman/Escritorio/e427f892191fa9a75167964ebcfc91a4.mp4"
    ret = call_mencoder_mp4(fichero)
    print "Hemos terminado con %s"%ret
    ret = call_mencoder_flv(fichero)
    print "Hemos terminado con %s"%ret
