#!/bin/bash

sleep 20s
uvicorn app.main:app --reload --host=0.0.0.0 --port=8001