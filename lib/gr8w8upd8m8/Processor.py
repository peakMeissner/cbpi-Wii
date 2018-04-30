from gr8w8upd8m8 import EventProcessor

class SingleEventProcessor(EventProcessor):
    def mass(self, event):
        if event.totalWeight > 5:
            self._events.append(event.totalWeight)
        else:
            self._events.append(0)
        
        self.done = True
    
    @EventProcessor.weight.getter
    def weight(self):
        if len(self._events) == 0:
            return 0
        return self._events.pop()
    
