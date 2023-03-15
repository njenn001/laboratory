from backend.user import User

""" Server class. """
class Server(): 
    
    """ 
        A class representation of the server. 

        ...
        
        Attributes
        ----------

        scenario : The system scenario
        you : The user

        Methods
        -------

        get/set_attributes
            Returns or sets each individual attribute. 
        __init__
            Creates user instance.
        
    """


    def __init__(self):

        """ Variables. """
        self.scenario = None
        self.you = None 

    def __init__(self, *args): 

        """ Variables. """
        self.scenario = args[0]
        self.you = None