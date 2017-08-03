import subprocess
import time
import os

#number_of_GPU_to_check=7

while True:
  cmd = r'"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe"'
  process =  subprocess.Popen(cmd, \
                            shell=True, \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE)


  ID=0
  GPUID=0
  output=""
  for line in process.stdout:
    if ID >=7:
      if (ID+1)%3==0:
        lst = line.split()

        if lst[0][0] == '+':
          break

        #print lst[0]
        if lst[0][1:] == 'ERR!' or lst[8] == 'Unknown':
          os.system("shutdown -t 15 -r -f")

        
    ID +=1

  print("OK!")


  time.sleep(10)
