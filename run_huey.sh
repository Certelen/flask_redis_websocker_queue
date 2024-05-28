#!/bin/sh

# Ensure that the huey package is on the python-path, in the event it hasn't
# been installed using pip.
export PYTHONPATH="../../:$PYTHONPATH"

# Run the consumer with 2 worker threads.
python ./backend/huey_consumer.py app.huey
