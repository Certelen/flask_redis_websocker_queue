#!/bin/sh

# Ensure that the huey package is on the python-path, in the event it hasn't
# been installed using pip.
export PYTHONPATH="../../:$PYTHONPATH"

# Run the consumer with 2 worker threads.
python ./backend/tasks/huey_consumer.py main.huey
