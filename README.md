# Laboratory 

This repository will hold an application programming interface used by laboratory instruments. 

## Background 

This repository was developed for use during the instruction of basic and advanced programming principles. These are the core fundamentals to programming techniques and paradigms. The following topics are implemented into the projects: 

    - Documentation 
    - Compilation & Execution
    - Naming Conventions 
    - Packages 
    - Abstraction 
    - Encapsulation
    - Interfaces
    - Polymorphism  
    - Error Handling 
    - Looping 
    - System Analysis 

## Software Requirements

```
  - python 3.11
```

## Usage 

The server is spun by simply pulling the repo and using one of the starting methods (machine dependent). Please satisfy listed software requirements prior to running the server. 

### Windows machines 

Clone the repository 

```
git clone https://github.com/njenn001/ClusterAPI.git
```

System configurations
```
set FLASK_APP=flaskr
set FLASK_ENV=development
```

Initialize the virtual environment
```
python __init__.py --v
```

Activate the virtual environment 
```
.\venv\Scripts\activate
```

Start the server
```
python __init__.py --r
```

### Linux machines 

Clone the repository 

```
git clone https://github.com/njenn001/ClusterAPI.git
```

System configurations 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
```

Initialize the virtual environment
```
python __init__.py --v
```

Activate the virtual environment 
```
.\venv\Scripts\activate
```

Start the server
```
python __init__.py --r
```


#### Credentials 

Admin user credentials are essential to using API utilities. 
  - stored in /creds/admin

Base user credentials are used to view API readings. 
  - stored in /creds/users 

## Acknowledgements

Special thank you to those who contributed to the project. 

	Noah Jennings 
	    TC 
	    ntjennings1@gmail.com
	    Pomona, CA

    TC
    	Virginia Beach, VA 
