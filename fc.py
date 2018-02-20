import os
import shutil
from PIL import Image, ImageOps
import numpy as np
from numpy.random import *
#from timeout import on_timeout
import subprocess
from subprocess import STDOUT, check_output
import time
import re
import glob

count = 0
pid = 0

def increase():

    global count

    files = os.listdir("./data/celebA")

    for i in files:

        r = (rand() - 1) / 2
        g = (rand() - 1) / 2
        b = (rand() - 1) / 2

        img = Image.open("./data/celebA/"+i)

        count = count + 1
        img_lig = img.point(gamma_table(1 + r, 1 + g, 1 + b))
        img_lig.save("./data/celebA/img"+str(count)+".jpg")

        print(count)


def gamma_table(gamma_r, gamma_g, gamma_b, gain_r=1.0, gain_g=1.0, gain_b=1.0):
    r_tbl = [min(255, int((x / 255.) ** (1. / gamma_r) * gain_r * 255.)) for x in range(256)]
    g_tbl = [min(255, int((x / 255.) ** (1. / gamma_g) * gain_g * 255.)) for x in range(256)]
    b_tbl = [min(255, int((x / 255.) ** (1. / gamma_b) * gain_b * 255.)) for x in range(256)]
    return r_tbl + g_tbl + b_tbl

def stopAndDisplay():
    global pid
    os.system("kill -9 {0}".format(pid.pid))
    print("gan stop")

#@on_timeout(limit=30, handler=stopAndDisplay, hint="2min")
def dcgan():

    print("START GAN!!!!!!!!!!!!!!!!!!")

    global pid
    #os.system("python main.py --dataset celebA --input_height=108 --train --crop")
    pid = subprocess.Popen(["python","main.py","--dataset","celebA","--input_height=108","--train","--crop"],shell=True)

cn = 0

ii=0
jj=0
kk=0
ddd=0
#os.getcwd()
#os.system("rm -f data/celebA/*")
#os.system("rm -f checkpoint/celebA_64_64_64/*")
dirs = os.listdir("../../Downloads")
for i in dirs:
    ddirs = os.listdir("../../Downloads/"+i)
    for j in ddirs:
        # jpg no maisuu
        while cn < 45:
            cn = 0
            dddirs = os.listdir("../../Downloads/"+i+"/"+j)
            for k in dddirs:
                index = re.search(".JPG","../../Downloads/"+i+"/"+j+"/"+k)
                if index:
                    cn = cn + 1
            print(str(cn))
            ii = i
            jj = j
            kk = dddirs
            time.sleep(1)

sampleDir = os.listdir("./")
samplesCount = 0
for i in sampleDir:
    index = re.search(r"samples", i)
    if index:
        samplesCount = samplesCount + 1
os.system("mv samples samples"+str(samplesCount))

print("transfer")
#print(dirs)
cn = 0

print(kk)

for i in kk:
    try:
        shutil.move(os.path.join("C:/Users/sho/Downloads/" + ii+"/"+jj , i),os.path.join("./data/celebA",i))
    except:
        print("thr")

#for i in dirs:
#    ddirs = os.listdir("../../Downloads/"+i)
#    for j in ddirs:
#            dddirs = os.listdir("../../Downloads/"+i+"/"+j)
#            for k in dddirs:
#                cn = cn + 1
#                shutil.move(os.path.join("C:/Users/sho/Downloads/" + i+"/"+j , k),os.path.join("./data/celebA",k))
#                if cn > 29:
#                    break

#for i in dirs:
#    files = os.listdir("C:/Users/sho/Downloads/" + i)
#    for j in files:
#        shutil.move(os.path.join("C:/Users/sho/Downloads/" + i , j),os.path.join("./data/celebA",j))


#os.system("rm -fr ~/Downloads/*")

files = glob.glob("./data/celebA/*.JPG")
for f in files:
    img = Image.open(f)
    nw = img.width / 130
    img_resize = img.resize((int(img.width/nw),int(img.height/nw)),Image.ANTIALIAS)
    img_resize.save(f)


for i in range(6):
    increase()

files = os.listdir("./data/celebA")
for i in files:
    img = Image.open("./data/celebA/"+i)

    count = count + 1
    img_mir = ImageOps.mirror(img)
    img_mir.save("./data/celebA/img"+str(count)+".jpg")

    print(count)

#dcgan()
print("gan start !!!!!!!!!!!!!!!!!!!!")
output = check_output("python main.py --dataset celebA --input_height=108 --train --crop",timeout=30,shell=True)
#output = check_output(["python","main.py","--dataset","celebA","--input_height=108","--train","--crop"],stderr=STDOUT,timeout=30)
print(output)
print("gan stop !!!!!!!!!!!!!!!!!!!!!")
