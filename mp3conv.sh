#!/bin/sh


source "${HOME}/.venv/bin/activate"

pip3 install pytube
python3 converter_mp3.py
