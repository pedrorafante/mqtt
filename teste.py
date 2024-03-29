import socket
import os

#alteração de 
s = socket.socket(socket.PF_CAN, socket.SOCK_DGRAM, socket.CAN_J1939)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
canal = "vcan0"
src_name = socket.J1939_NO_NAME
src_pgn = socket.J1939_NO_PGN 
src_addr = socket.J1939_NO_ADDR
src_sck_addr = (canal, src_name, src_pgn, src_addr)
s.bind(src_sck_addr)
Hor =0.0
RPM = 0.0
PerTorque = 0
FuelRate = 0.0
ThrottlePos = 0.0
TempCoolant = 0
TempFuel = 0
TempEngOil = 0.0
TempTurbOil = 0.0
TempInletAir = 0
PressFuel = 0
PressEngOil = 0
PressCoolant = 0
PressBoost = 0
PressAirInlet = 0
TempExhaustGas = 0.0
while True:
            data, addr = s.recvfrom(128)
            if addr[2]==65253:
            	Hor = 0.05*int.from_bytes(data[:4], byteorder='little')
            if addr[2]==61444:
            	RPM = 0.125*int.from_bytes(data[3:5], byteorder='little')
            	PerTorque = data[2]-125
            if addr[2]==65266:
            	FuelRate = 0.05*int.from_bytes(data[:2], byteorder='little')
            	ThrottlePos=0,4*int.from_bytes(data[7], byteorder='little')
            if addr[2]==65262:
            	TempCoolant = data[0]-40
            	TempFuel = data[1]-40
            	TempEngOil = (0.03125*int.from_bytes(data[2:4], byteorder='little'))-273
            	TempTurbOil = (0.03125*int.from_bytes(data[4:6], byteorder='little'))-273
            	TempInletAir = data[6]-40
            if addr[2]==65263:
            	PressFuel = 4*data[0]
            	PressEngOil = 4*data[3]
            	PressCoolant = 2*data[6]
            if addr[2]==65270:
            	PressBoost = 2*data[1]
            	PressAirInlet = 2*data[3]
            	TempExhaustGas = (0.03125*int.from_bytes(data[5:7], byteorder='little'))-273
            
            #os.system("clear")
            print("Horímetro: ", Hor,"hrs")
            print("Rotação: ", RPM,"rpm")
            print("Torque: ", PerTorque,"%")
            print("Litros/Hora: ", FuelRate,"l/h")
            print("% Acelerador: ", ThrottlePos,"%")
            print("Temp. Água: ", TempCoolant,"ºc")
            print("Temp. Óleo Motor: ", TempEngOil,"ºc")
            print("Temp. Óleo Turbo: ", TempTurbOil,"ºc")
            print("Temp. Ar: ", TempInletAir,"ºc")
            print("Temp. Gas Exaustão: ", TempExhaustGas,"ºc")
            print("Pres. de Combustível.: ", PressFuel,"kPa")
            print("Pres. óleo: ", PressEngOil,"kPa")
            print("Pres. Água: ", PressCoolant,"kPa")
            print("Pres. Boost: ", PressBoost,"kPa")
            print("Pres. Absoluta Ar: ", PressAirInlet,"kPa")
            #print("{:02x} {:04x} :".format(addr[3], addr[2]), end="")
            #for j in range(len(data)):
            #    if j % 8 == 0 and j != 0:
            #        print("\n{:05x}    ".format(j), end="")
            #    print(" {:02x}".format(data[j]), end="")
            #print("\n", end="")

