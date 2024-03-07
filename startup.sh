#!/bin/bash
gnome-terminal -- bash -c "cd ./src/code && python app.py; exec bash" &
gnome-terminal -- bash -c "cd ./src/gui && ng serve -o; exec bash" &
