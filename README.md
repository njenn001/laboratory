# Laboratory 

This repository will hold an application programming interface used by laboratory personel. 

## Background 

This repository will hold a very important tool to TC Laboratory personel. Not only will it allow TC personel to quickly start or stop TC Servers on the TC Network, it will also help facilitate communication between TC Clients and services available throughout the network.

This repository was developed in part for use during the instruction of basic and advanced programming principles. These are the core fundamentals to programming techniques and paradigms. The following topics are implemented into the projects: 

  - Program Structure
  - Packages / Imports
  - Input / Output
  - Execution   
  - Documentation 
  - Naming Conventions 
  - Functions
  - Scoping
  - Variables 
  - Conditions
  - Looping  
  - Abstraction 
  - Encapsulation 
  - Inheritance 
  - Parallelism 


## Software/OS Requirements

```
  - Ubuntu 22.04.3 LTS
  - python 3.8
```

## Usage 

The server is spun by simply pulling the repo and using one of the starting methods. Please confirm listed software requirements have been downloaded prior to starting the server. 

Clone and enter the repository 

```
git clone https://github.com/njenn001/laboratory.git
cd laboratory
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
source .\venv\bin\activate
```

Start the server
```
python __init__.py --r
```

### Fresh Installations

The database this API stands on will need to be initialized and populated, outlined in this section. This will help ensure server integrity and reproducibility. 

Initialize the database 
* From within the root dir
```
flask --app flaskr init-db
```

## Acknowledgements

Special thank you to those who contributed to the project. 

	Noah Jennings 
	    TC 
	    ntjennings1@gmail.com
	    Pomona, CA

    TC
      th3orycc@gmail.com
    	Virginia Beach, VA 
