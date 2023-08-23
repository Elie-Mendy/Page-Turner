from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings 
import subprocess
import os

from django.conf import settings



def trigger_recommandation(request, searchValue=None):
    fullpath =  str(settings.BASE_DIR)+"/scripts/reco.py"
    try:
        if not searchValue : 
            print('No title')
            return JsonResponse({})
        execution_output = subprocess.run(
            [
                "python3",
                fullpath,
                searchValue,
                settings.BASE_DIR
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except Exception as e:
        print(e)
        return JsonResponse({})
    return JsonResponse(
        {
            "stdout": execution_output.stdout.decode("utf8").strip(),
        }
    )