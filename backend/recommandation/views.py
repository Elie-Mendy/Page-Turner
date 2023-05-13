from django.shortcuts import render

from django.http import JsonResponse

import subprocess
import os

from django.conf import settings



def trigger_recommandation(request):
    fullpath =  os.getcwd()+"/scripts/reco.py"
    execution_output = subprocess.run(
        [
            "python3",
            fullpath,
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