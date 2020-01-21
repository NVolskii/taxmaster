#!/usr/bin/bash
pip freeze | grep -v "0.0.0" > requirements.txt