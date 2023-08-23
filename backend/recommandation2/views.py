from django.shortcuts import render
from django.http import JsonResponse

import subprocess
import os

from django.conf import settings


def trigger_recommandation2(request, user_id):
    fullpath =  str(settings.BASE_DIR)+"/scripts/reco2.py"
    if not user_id : 
        print('No user_id')
        return JsonResponse({})
    print('user_id', user_id)
    execution_output = subprocess.run(
        [
            "python3",
            fullpath,
            user_id,
            settings.BASE_DIR
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
