from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import subprocess
import os

from django.conf import settings


def trigger_recommandation2(request):
  print(os.getcwd())
  execution_output = subprocess.run(
      [
          "python",
          os.path.join(os.getcwd(), "scripts/reco2.py"),
      ],
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
  )
  
  print(execution_output)
  return JsonResponse(
      {
          "stdout": execution_output.stdout.decode("utf8"),
          "stderr": execution_output.stderr.decode("utf8"),
      }
  )
