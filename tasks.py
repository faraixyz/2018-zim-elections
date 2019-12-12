import os
from pathlib import Path
from invoke import task

CWD = Path.cwd()


@task
def clean(c):
  extentions = ['*.db', '*.json']
  for ext in extentions:
    for f in CWD.glob(ext):
      f.unlink()
  print('Cleaned directory')

@task
def build_DS(c, clean=False):
  if clean == True:
    c.run('invoke clean')
  c.run('python ./disability_senators.py')
  print('Ran disability_senators.py')
