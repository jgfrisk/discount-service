#!/bin/bash

# Use exec so that signals are passed properly
# Use only 1 process (worker) so we don't have to deal with
# any shared memory problems
exec gunicorn app:app --workers 1 --threads 4 --bind 0.0.0.0:5000
