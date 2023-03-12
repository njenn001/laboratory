class User(): 
    def __init__(self): 
        self.content_type = None
        self.username = ''
        self.pin = ''
        self.creds = {}
        self.existence = False


    # GET / SET content type 
    def get_content_type(self): 
        return self.content_type
    def set_content_type(self, content_type): 
        self.content_type = content_type

    # GET / SET username 
    def get_username(self): 
        return self.username
    def set_username(self, username):
        self.username = username  

    # GET / SET pin 
    def get_pin(self): 
        return self.pin
    def set_pin(self, pin): 
        self.pin = pin 

    # GET / SET creds
    def get_creds(self): 
        return self.creds
    def set_creds(self, creds): 
        self.creds = creds

    # GET / SET existence 
    def get_existence(self): 
        return self.existence
    def set_existence(self, existence): 
        self.existence = existence 

    # Examine other hardcoded admin users 
    def examine_others(self): 
        #df = pd.read_csv (r'admin.csv')
        
        
        print('df') 
    # Initial user object 
    def init(self, creds): 
        self.set_creds(creds)
        self.set_pin(creds['pin'])
        self.set_username(creds['username'])

        self.examine_others()
