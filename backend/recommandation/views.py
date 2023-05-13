from django.shortcuts import render

from django.http import JsonResponse

import subprocess
import os

from django.conf import settings



def trigger_recommandation(request, book_title=None):
    fullpath =  os.getcwd()+"/scripts/reco.py"
    if not book_title : 
        print('No title')
        return JsonResponse({})
    print('title', book_title)
    execution_output = subprocess.run(
        [
            "python3",
            fullpath,
            book_title
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