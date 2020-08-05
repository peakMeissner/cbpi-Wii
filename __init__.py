import sys
import subprocess
import threading

from modules import cbpi
from modules.core.hardware import SensorPassive
from modules.core.props import Property
from .lib.gr8w8upd8m8.Processor import SingleEventProcessor
from .lib.gr8w8upd8m8.WiiBoard import ConstantReceiverBoard


class WiiThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.value = 0
        self.running = True
        self.processor = SingleEventProcessor()
        self.board = ConstantReceiverBoard(self.processor)
        
        if len(sys.argv) == 1:
            cbpi.app.logger.info('Discover the Wii board')
            self.address = self.board.discover()
        else:
            self.address = sys.argv[1]
        
        cbpi.app.logger.info('Establish connection to the Wii board')
        self.board.connect(self.address)
        self.board.setLight(False)
    
    def shutdown(self):
        pass
    
    def stop(self):
        self.running = False
        cbpi.app.logger.info('Disconnect the Wii board')
        
        try:
            
            # Disconnect already-connected devices.
            # This is basically Linux black magic just to get the thing to work.
            
            subprocess.check_output(['bluez-test-input', 'disconnect',
                                    self.address],
                                    stderr=subprocess.STDOUT)
            subprocess.check_output(['bluez-test-input', 'disconnect',
                                    self.address],
                                    stderr=subprocess.STDOUT)
        except:
            pass
    
    def run(self):
        while self.running:
            self.board.receive()
            self.value = self.processor.weight
            self.processor.done = False
    

class WiiSensor(SensorPassive):
    
    offset = Property.Number('Offset', True, 0)
    unit_of_measure = Property.Select('Unit of measure', ['KG', 'LBS'])
    
    def init(self):
        self.t = WiiThread()
        
        def shudown():
            shudown.cb.shutdown()
            
        shudown.cb = self.t
        
        self.t.start()
    
    def stop(self):
        try:
            self.t.stop()
        except:
            pass
    
    def get_unit(self):
        if self.unit_of_measure == 'KG':
            return 'KG'
        else:
            return 'LBS'
    
    def read(self):
        if self.unit_of_measure == 'KG':
            self.data_received(round(self.t.value + float(self.offset),
                               2))
        else:
            self.data_received(round(self.t.value * 2.20462262185
                               + float(self.offset), 2))
    
