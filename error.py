class Error():
    exceptions = []
    
    def append(self, ex):
        self.exceptions.append(ex)
        
    def get_message(self):
        if len(self.exceptions) > 0:
            return str(self.exceptions[-1])
        else:
            return ''