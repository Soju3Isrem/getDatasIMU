import serial, time
import pandas as pd

imu = serial.Serial('/dev/ttyUSB0',115200)
time.sleep(2)
data=[]
dataInput=[]
aX=[]
aY=[]
aZ=[]
gX=[]
gY=[]
gZ=[]
i=0
verif = False
while verif  == False:
    dataImu = imu.readline()
    if format(dataImu[:2].decode("utf-8")) == 'aX':
                  verif = True
while i<12:
    dataInput.append("{} {}".format(dataImu[:2].decode("utf-8"),dataImu[3:].decode('utf-8').strip()))
    dataImu = imu.readline()
    i+=1
for i in dataInput:
    if i[:2] == 'aX':
        aX.append(i[3:])
    if i[:2] == 'aY':
        aY.append(i[3:])
    if i[:2] == 'aZ':
        aZ.append(i[3:])
    if i[:2] == 'gX':
        gX.append(i[3:])        
    if i[:2] == 'gY':
        gY.append(i[3:])        
    if i[:2] == 'gZ':
        gZ.append(i[3:])        
        
dataSave = {'aX':aX[:],
            'aY':aY[:],
            'aZ':aZ[:],
            'gX':gX[:],
            'gY':gY[:],
            'gZ':gZ[:],}

print(dataSave)
df = pd.DataFrame(dataSave)
df.to_csv('gesture.csv')



