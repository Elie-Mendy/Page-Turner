from django.shortcuts import render
from django.http import JsonResponse

import subprocess
import os

from django.conf import settings



def trigger_recommandation(request, searchValue=None):
    fullpath =  os.getcwd()+"/scripts/reco.py"
    if not searchValue : 
        print('No title')
        return JsonResponse({})
    print('title', searchValue)
    execution_output = subprocess.run(
        [
            "python3",
            fullpath,
            searchValue
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    print(execution_output)
    return JsonResponse(
        {
            "stdout": execution_output.stdout.decode("utf8").strip(),
        }
    )