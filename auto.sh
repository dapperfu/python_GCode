#!/bin/sh

find GCode -name "*.py" | xargs -n1 -P8 ./fix.sh
