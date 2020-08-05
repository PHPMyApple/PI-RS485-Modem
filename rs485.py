
from __future__ import absolute_import

import time 
import serial   
"""rx = Empfänger (reciever)  | tx=Sender (transmitter)"""
class RS485Settings(object):
    def __init__(
        self,
        rts_levgel_for_tx=True,
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

    def writ(self, b):
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
        
            



