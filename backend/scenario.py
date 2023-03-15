""" Imports. """
from lib2to3.pgen2.pgen import DFAState
import os 
import threading
import time

from backend.server import Server 

""" Scenario class. """
class Scenario(): 

    """ 
        A class representation of the users system environment. 

        ...
        
        Attributes
        ----------
        os_name : str
        style : str 
        py_version : str 
        root_dir : str 
        t_list : list 
        virt_thread : threading.Thread
        vcheck_thread : threading.Thread 
        run_thread : threading.Thread 
        args : list
        app : flask.App

        Methods
        -------

        get/set_attributes
            Returns or sets each individual attribute. 
        __init__
            Creates scenario instance.
        clear_screen
            Clears the terminal. 
        clean_sequence
            Cleans the file structure. 
        throw_exec
            Throws any programmed exceptions. 
        stop_thread
            Stops all thread. 
        start
            Runs the scenario evaluation.
        os_eval
            Evaluates the operating system. 
        version_check
            Checks the Python version.
        virtual_init
            Initializes the virtual environment. 
    """
     
    """ Initialized the scenario. 
    
    @param args : List of arguments 
    @type args : list
    """
    def __init__(self, *args):
        
        """ Variables. """
        self.os_name = ''
        self.style = '' 
        self.py_version = ''
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.t_list = [] 
        self.virt_thread = None
        self.vcheck_thread = None 
        self.run_thread = None 
        self.args = None 
        self.app = None 
        self.server = None 
        
        """ Further initialization. """
        self.init() 
                
    """ Returns the scenarios os name. 
    
    @return os_name : OS name
    @rtype os_name : str
    """
    def get_os_name(self): 
        return self.os_name
    
    """ Sets the scenarios os name. 
    
    @param os_name : OS name 
    @type os_name : str
    """
    def set_os_name(self, os_name):
        self.os_name = os_name 
         
    """ Returns the scenarios style. 
    
    @return style : The style
    @rtype style : str
    """ 
    def get_style(self): 
        return self.style
    
    """ Sets the scenarios style. 
    
    @param style : The style 
    @type style : str
    """
    def set_style(self, style):
        self.style = style 
            
    """ Returns the scenarios python version. 
    
    @return py_version : The python version
    @rtype py_version : str
    """
    def get_py_version(self): 
        return self.py_version
    
    """ Sets the scenarios python version. 
    
    @param py_version : The python version
    @type py_version : str
    """
    def set_py_version(self, py_version):
        self.py_version = py_version
         
    """ Returns the scenarios root directory. 
    
    @return root_dir : The root directory 
    @rtype root_dir : str
    """
    def get_root_dir(self): 
        return self.root_dir
    
    """ Sets the scenarios root directory. 
    
    @param root_dir : The root directory 
    @type root_dir : str
    """
    def set_root_dir(self, root_dir):
        self.root_dir = root_dir
      
    """ Returns the scenarios thread list. 
    
    @return t_list : The thread list
    @rtype t_list: list
    """
    def get_t_list(self): 
        return self.t_list
    
    """ Sets the scenarios thread list. 
    
    @param t_list : The thread list
    @type t_list: list
    """
    def set_t_list(self, t_list):
        self.t_list = t_list
      
    """ Adds to the scenarios thread list. 
    
    @param thread : The new thread
    @type thread : threading.Thread 
    """
    def add_thread(self, thread): 
        self.t_list.append(thread)
  
    """ Returns the scenarios virtual check thread. 
    
    @return vcheck_thread : The vcheck thread
    @rtype vcheck_thread : threading.Thread
    """
    def get_vcheck_thread(self): 
        return self.vcheck_thread
    
    """ Sets the scenarios virtual check thread. 
    
    @param vcheck_thread : The vcheck thread
    @type vcheck_thread : threading.Thread
    """
    def set_vcheck_thread(self, vcheck_thread): 
        self.vcheck_thread = vcheck_thread
    
    """ Returns the scenarios virtual thread. 
    
    @return virt_thread : The virtual thread
    @rtype virt_thread : threading.Thread
    """
    def get_virt_thread(self): 
        return self.virt_thread
    
    """ Sets the scenarios virtual thread. 
    
    @param virt_thread : The virtual thread
    @type virt_thread : threading.Thread
    """
    def set_virt_thread(self, virt_thread):
        self.virt_thread = virt_thread

    """ Returns the scenarios run thread. 
    
    @return run_thread : The run thread
    @rtype run_thread : threading.Thread
    """
    def get_run_thread(self): 
        return self.run_thread
    
    """ Sets the scenarios run thread. 
    
    @param run_thread : The run thread
    @type run_thread : threading.Thread
    """
    def set_run_thread(self, run_thread): 
        self.run_thread = run_thread

    """ Returns the scenarios arguments. 
    
    @return args : The argumnets
    @rtype args : list
    """
    def get_args(self): 
        return self.args
    
    """ Sets the scenarios arguments. 
    
    @param args : List of arguments
    @type args : list
    """
    def set_args(self, args):
        self.args = args

    """ Returns the scenarios application. 
    
    @return app : The app
    @rtype app : flask.App
    """
    def get_app(self): 
        return self.app 
    
    """ Sets the scenarios application. 
    
    @param app : The app
    @type app : flask.App
    """
    def set_app(self, app): 
        self.app = app 

    """ Returns the scenarios server. 
    
    @return server : The server
    @rtype server : server.Server
    """
    def get_server(self): 
        return self.server
    
    """ Sets the scenarios server. 
    
    @param server : The server
    @type server : server.Server
    """
    def set_server(self, server): 
        self.server = server 


    """ Further init scripts. 
    
    @return none
    """
    def init(self): 

        #self.clear_sequence()
        self.os_eval() 
        self.version_check() 
                
    """ Starts the application. 
    
    @return none 
    """
    def start(self): 
        import flaskr
        
        try: 
            self.set_server(Server(self))
            self.set_app(flaskr.create_app().run())
            self.set_run_thread( threading.Thread(target=self.get_app, args=([])) )
            self.add_thread(self.get_run_thread())
        except Exception as ex: 
            self.throw_exc('app')

    """ Throws necessary exceptions. 
    
    @param msg : Exception message.
    @type msg : str
    """
    def throw_exc(self, msg): 
        
        # Python version error 
        if msg == 'version':
            
            
            self.clean_sequence()             
            raise Exception("Must be using Python 3.11.") 
        
        if msg == 'venv': 
            if self.get_style() == "Windows": 

                self.clean_sequence()
                raise Exception("Error installing virtual environment")
            else: 
                

                self.clean_sequence()
                raise Exception("Error installing virtual environment")

        # Flask app error
        elif msg == 'app': 
            if self.get_style() == 'nt':      


                self.clean_sequence() 
                raise Exception("Windows Flask app.")
            else:


                self.clean_sequence() 
                raise Exception("Linux Flask app.")

        # Dependency install error 
        elif msg == 'inst': 
            if self.get_style() == 'nt':      


                self.clean_sequence() 
                raise Exception("Windows virtual environment.")
            else:


                self.clean_sequence() 
                raise Exception("Linux virtual environment.")

    """ Stop all running thread. 
    
    @return none 
    """
    def stop_threads(self): 
        try: 
            for t in self.get_t_list():
                if not t.is_alive(): 
                    t.join() 
        except Exception as ex: 
            self.stop_threads() 
    
    """ Initialize the virtual environment. 
    
    @return none 
    """
    def virtual_init(self): 

        """ Refines the virtual instance.  
        
        @param object : Scenario obj
        @type object : obj.Scenario
        """
        def virtual_instance(object): 
            print("\nCreating virtual instance ...")

            if object.get_style() == "Windows":
                
                try:
                    
                    print('\nCreating virtual environment ...\n')
                    os.system(r"python -m  venv " + object.get_root_dir() + r"\..\venv")
                    time.sleep(5)
                    
                    os.sys.execuatble = str(object.get_root_dir() + r"\venv\Scripts\python.exe")
                    val = os.system(r'.\venv\Scripts\activate.bat')
                    if val == 0: 
                        
                        print('\nActivating virtual environment ...\n')
                        os.system(r'.\venv\Scripts\activate.bat')
                        
                        print('\nInstall virtual requirments ...\n')
                        os.system(r'.\venv\Scripts\pip.exe install -r .\requirements.txt')


                except Exception as ex: 
                    object.throw_exc('venv')
            else: 
                try: 


                    print('\nCreating virtual environment ...\n') 
                    os.system(r"python -m  venv " + object.get_root_dir() + r"/../venv")
                    time.sleep(5)
                    
                    os.sys.execuatble = object.get_root_dir() + r"/../venv/bin/python"
                    val = os.system(object.get_root_dir() + r'/../venv/bin/activate')
                    if val == 0: 
                        
                        '''print('\nActivating virtual environment ...\n')
                        os.system(r'./venv/bin/activate')'''
                        
                        print('\nInstalling virtual requirments ...\n')
                        os.system(object.get_root_dir() + r'/../venv/bin/pip install -r requirements.txt')


                except Exception as ex: 
                    object.throw_exc('venv')
                
        """ Check for the existence of a virtual environment. 
        
        @param object : Scenario obj
        @type object : obj.Scenario

        @param go : Indicator
        @type go : bool
        """
        def virtual_check(object, go): 
            print("\nChecking File Structure ...")
            
            if object.get_style() == "Windows":
                try: 
                    v_folder = os.path.isdir(object.get_root_dir() + r'\..\venv')
                    if v_folder: 
                        go = True 
                        print("\nVirtual Environment Exists")
                except Exception as ex:
                    #object.throw_exc('env')
                    go = False                    
                    print("\nVirtual Environment does not exist")
                    
            else: 
                try: 
                    v_folder = os.path.isdir(object.get_root_dir() + r'/../venv')
                    if v_folder: 
                        go = True 
                        print("\nVirtual Environment exists")
                except Exception as ex:
                    #object.throw_exc('env')
                    go = False
                    print("\nVirtual Environment does not exist")

            if not go: 
                try: 
                    
                    self.set_virt_thread( threading.Thread(target=virtual_instance, args=([self])) )
                    self.add_thread(self.get_virt_thread())        
                    self.get_virt_thread().start()
                except Exception as ex: 
                    self.throw_exc('venv')
                    
        go = False 
        self.set_vcheck_thread( threading.Thread(target=virtual_check, args=([self, go])) )
        self.get_vcheck_thread().start() 

    """ Clean project directories. 
    
    @return none 
    """
    def clean_sequence(self):
        print("\nCleaning ...")
        
        # Windows Version
        def windows_clean(object): 
            try:
                os.system(r'rmdir __pycache__ /S /Q && rmdir flaskr\__pycache__ /S /Q && del flaskr\*.pyc && del *.pyc')
            except Exception as ex: 
                print(ex) 
        # Linux Verison
        def linux_clean(object): 
            try: 
                os.system(r'rm -rf app\__pycache__')
            except Exception as ex: 
                print(ex) 
            
        if self.get_style() == 'Windows': 
            windows_clean(self)
        else: 
            linux_clean(self)
        
    """ Checks Python version. 
    
    @return none
    """
    def version_check(self):  
        print('\nChecking Python Version ...')
        
        self.set_py_version(float( str(os.sys.version_info[0]) + "." + str(os.sys.version_info[1]) )) 
        if self.get_py_version() != 3.11:
            self.throw_exc('version')
        else: 
            print('\nCorrect Python version.')
                 
    """ Evaluates the operating system. 
    
    @return none
    """
    def os_eval(self): 
        self.set_os_name(os.name.replace(' ', '')) 
        
        if self.get_os_name() == 'nt': 
            self.set_style('Windows')
        else: 
            self.set_style('Linux')
    
    """ Empty terminal contents.
     
    @return none  
    """
    def clear_screen(self): 
        if self.os_name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')
    