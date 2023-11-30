#!/bin/bash

# Defines the main function. 
main(){
    sudo kill -9 `sudo lsof -t -i:5000`
}

# Runs the main function 
main