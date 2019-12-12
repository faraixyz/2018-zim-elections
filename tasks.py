from pathlib import Path
from invoke import task

CWD = Path.cwd()


@task
def clean(c):
    outdir = CWD / Path('output')
    if outdir.exists():
        for f in outdir.iterdir():
            f.unlink()
    outdir.rmdir()
    print('Deleted output')


@task
def build_DS(c, clean=False):
    if clean == True:
        c.run('invoke clean')
    c.run('python ./disability_senators.py')
    print('Ran disability_senators.py')
