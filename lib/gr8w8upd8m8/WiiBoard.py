from gr8w8upd8m8 import Wiiboard

INPUT_STATUS = 20
INPUT_READ_DATA = 21
EXTENSION_8BYTES = 32

class ConstantReceiverBoard(Wiiboard):
    def receive(self):
        #try:
        #   self.receivesocket.settimeout(0.1)       #not for windows?
        while self.status == "Connected" and not self.processor.done:
            data = self.receivesocket.recv(25)
            intype = int(data.encode("hex")[2:4])
            if intype == INPUT_STATUS:
                # TODO: Status input received. It just tells us battery life really
                self.setReportingType()
            elif intype == INPUT_READ_DATA:
                if self.calibrationRequested:
                    packetLength = (int(str(data[4]).encode("hex"), 16) / 16 + 1)
                    self.parseCalibrationResponse(data[7:(7 + packetLength)])
                    
                    if packetLength < 16:
                        self.calibrationRequested = False
            elif intype == EXTENSION_8BYTES:
                self.processor.mass(self.createBoardEvent(data[2:12]))
            else:
                print "ACK to data write received"
        
    
