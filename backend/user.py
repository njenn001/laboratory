""" User class. """
class User(): 

    """ 
        A class representation of the users. 

        ...
        
        Attributes
        ----------
        content_type : str
        username : str 
        pin : str 
        creds : dict
        existence : bool

        Methods
        -------

        get/set_attributes
            Returns or sets each individual attribute. 
        __init__
            Creates user instance.
        
    """
    
    """ Initialize the user. 
    
    @return none
    """
    def __init__(self): 
        self.content_type = None
        self.username = ''
        self.pin = ''
        self.creds = {}
        self.existence = False


    """ Returns the users content type. 
    
    @return content_type : User content type
    @rtype content_type : str
    """
    def get_content_type(self): 
        return self.content_type
    def set_content_type(self, content_type): 
        self.content_type = content_type

    """ Returns the users username. 
    
    @return username : User username
    @rtype username : str
    """
    def get_username(self): 
        return self.username
    def set_username(self, username):
        self.username = username  

    """ Returns the users pin. 
    
    @return pin  : User pin
    @rtype pin : int
    """
    def get_pin(self): 
        return self.pin
    def set_pin(self, pin): 
        self.pin = pin 

    """ Returns the users credentials. 
    
    @return creds : User credentials
    @rtype creds : dict
    """
    def get_creds(self): 
        return self.creds
    def set_creds(self, creds): 
        self.creds = creds

    """ Returns the users existence. 
    
    @return existence : User existence
    @rtype existence : bool
    """
    def get_existence(self): 
        return self.existence
    
    """ Sets the users existence. 
    
    @param existence : User existence
    @type existence : bool
    """
    def set_existence(self, existence): 
        self.existence = existence 

    """ Examine other users. 
    
    @return none
    """
    def examine_others(self): 
        #df = pd.read_csv (r'admin.csv')
        
        
        print('df') 

    """ Further initialization. 
    
    @param creds : User credentials
    @type creds : dict
    """ 
    def init(self, creds): 
        self.set_creds(creds)
        self.set_pin(creds['pin'])
        self.set_username(creds['username'])

        self.examine_others()
