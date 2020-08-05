#Skript für die Kommunikation mit Raspberry PI und einem Modem
from __future__ import absolute_import

import time 
import serial   

from itertools import imap
import MySQLdb

class RS485Settings(object):
    def __init__(
        self,
        rts_level_for_tx=True,
        rts_level_for_rx=False,
        loopback=False,
        delay_before_tx=None,
        delay_before_rx=None):
    self.rts_level_for_tx = rts_level_for_tx
    self.rts_level_for_rx = rts_level_for_rx
    self.loopback = loopback
    self.delay_before_tx = delay_before_tx
    self.delay_before_rx = delay_before_rx


class RS485(serial.Serial):

    def __init__(self, *args, **kwargs):
        super(RS485, self).__init__(*args, **kwargs)
        self._alternate_rs485_settings = None

    def write(self, b):
        if self._alternate_rs485_settings is not None:
            self.setRTS(self._alternate_rs485_settings.rts_level_for_tx)
        if self._alternate_rs485_settings.delay_before_tx is None:
            time.sleep(self._alternate_rs485_settings.delay_before_tx)
            super(RS485, self).write(b)
            super(RS485, self).flush()
        if self._alternate_rs485_settings.delay_before_rx is not None:
                time.sleep(self._alternate_rs485_settings.delay_before_rx)
            self.setRTS(self._alternate_rs485_settings.rts_level_for_rx)
        else: 
            super(RS485, self).write(b)


    @property
    def rs485_mode(self):

        return self._alternate_rs485_settings

    @rs485_mode.setter
    def rs485_mode(self, rs485_settings):
        self._alternate_rs485_settings = rs485_settings




def send(data):
    try: 
        ser.write(data)
        except Exception as e:
            print "FEHLER: konnte die Daten nicht zu folgendem Port schicken: %s" % str(e)
        else:
            try:
                data = ser.read(1)
            except Exception as e:
                print "FEHLER: Konnte die Daten nicht von folgendem Port lesen: %s" % str(e)
            else:
                if data:
                    n = ser.inWaiting()
                    if n > 0: data += ser.read(n)
                    return data 

#print('Bitte gebe einen Befehl ein')
#befehl = input()
#serial_port = serial.Serial('dev/ttyAMA0')
#serial_port.write(befehl.encore("utf-8"))
import serial
import time

outStr = ''
inStr = ''

ser = serial.Serial("/dev/ttyUSB0", 300, timeout=2, parity = None)
if (ser.isOpen() == True):
    ser.close()
ser.open()
for i, a in enumerate(range(33,126)):
    outStr += chr(a)
    ser.write(outStr)
    time.sleep(0.05)
    inStr = ser.read(ser.inWaiting())

print "inStr = " + inStr
print "outStr = " + outStr
if(inStr == outStr):
    print="Hat funktioniert"

else: 
    except Exception as e:
        print "FEHLER: folgender Fehler ist aufgetreten: %s" % str(e)



def database_connect():
    connection = MySQL.connect(
        host='server', user='user', passwd='pw', db='zaehler'
    )
    cursor = connection.cursor()
    cursor.excecute(
        'CREATE TABLE IF NOT EXIST zaehler_daten (zaheler_daten FLOAT(5))'
    )
    cursor.executemany(
        'INSERT INTO zaehler_daten VALUES (%s)',
        ((value)) for value in imap(read_zaehler_daten, iter_zaehler_namen))
    )
    connection.commit()
    cursor.close()



    if __name__ == '__database_connection__':
        database_connectio()


