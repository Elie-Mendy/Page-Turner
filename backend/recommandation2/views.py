from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import subprocess
import os

from django.conf import settings


def trigger_recommandation2(request, user_id):
    print(os.getcwd())
    if not user_id : 
        print('No user_id')
        return JsonResponse({})
    print('user_id', user_id)
    execution_output = subprocess.run(
        [
            "python",
            os.path.join(os.getcwd(), "scripts/reco2.py"),
            user_id
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
