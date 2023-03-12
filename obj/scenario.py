from lib2to3.pgen2.pgen import DFAState
import os 
import threading
import time 

class Scenario(): 
    # Class init 
    def __init__(self, *args):
        
        # Native descriptors 
        self.os_name = ''
        self.style = '' 
        self.py_version = ''
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
                
        # Threads 
        self.t_list = [] 

        self.virt_thread = None
        self.vcheck_thread = None 
        self.run_thread = None 

        # You 
        self.you = None
        self.args = None 
        self.app = None 
        
        self.init() 
                
    # GET / SET os name 
    def get_os_name(self): 
        return self.os_name
    def set_os_name(self, os_name):
        self.os_name = os_name 
        
    # GET / SET style  
    def get_style(self): 
        return self.style
    def set_style(self, style):
        self.style = style 
        
    # GET / SET python version 
    def get_py_version(self): 
        return self.py_version
    def set_py_version(self, py_version):
        self.py_version = py_version
       
    # GET / SET root directory 
    def get_root_dir(self): 
        return self.root_dir
    def set_root_dir(self, root_dir):
        self.root_dir = root_dir
    
    # GET / SET / ADD thread list
    def get_t_list(self): 
        return self.t_list
    def set_t_list(self, t_list):
        self.t_list = t_list
    def add_thread(self, thread): 
        self.t_list.append(thread)

    # GET / SET v check thread
    def get_vcheck_thread(self): 
        return self.vcheck_thread
    def set_vcheck_thread(self, vcheck_thread): 
        self.vcheck_thread = vcheck_thread
    
    # GET / SET virtual thread 
    def get_virt_thread(self): 
        return self.virt_thread
    def set_virt_thread(self, virt_thread):
        self.virt_thread = virt_thread

    # GET / SET run thread 
    def get_run_thread(self): 
        return self.run_thread
    def set_run_thread(self, run_thread): 
        self.run_thread = run_thread

    # GET / SET you 
    def get_you(self): 
        return self.you
    def set_you(self, you): 
        self.you = you 
        
    # GET / SET args 
    def get_args(self): 
        return self.args
    def set_args(self, args):
        self.args = args

    # GET / SET app 
    def get_app(self): 
        return self.app 
    def set_app(self, app): 
        self.app = app 

    # Init Scenario
    def init(self): 

        #self.clear_screen() 
        self.os_eval() 
        self.version_check() 
        #self.clean_sequence() 
        #self.virtual_init() 
                
    # Start app 
    def start(self): 
        import flaskr
        
        try: 
            self.set_app(flaskr.create_app().run())
            self.set_run_thread( threading.Thread(target=self.get_app, args=([])) )
            self.add_thread(self.get_run_thread())
        except Exception as ex: 
            self.throw_exc('app')

    # Throw exception with suggested fix / fix error 
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

    # Stop all running threads
    def stop_threads(self): 
        try: 
            for t in self.get_t_list():
                if not t.is_alive(): 
                    t.join() 
        except Exception as ex: 
            self.stop_threads() 
    
    # Init virtual environment 
    def virtual_init(self): 

        # Create a virtual instance
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
                
        # Check for existence of virtual environment 
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

            
        
    # Clean project directories 
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
        
    # Check Python version
    def version_check(self):  
        print('\nChecking Python Version ...')
        
        self.set_py_version(float( str(os.sys.version_info[0]) + "." + str(os.sys.version_info[1]) )) 
        if self.get_py_version() != 3.11:
            self.throw_exc('version')
        else: 
            print('\nCorrect Python version.')
                 
    # Check version
    def os_eval(self): 
        self.set_os_name(os.name.replace(' ', '')) 
        
        if self.get_os_name() == 'nt': 
            self.set_style('Windows')
        else: 
            self.set_style('Linux')
    
    # Empty terminal contents 
    def clear_screen(self): 
        if self.os_name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')
    