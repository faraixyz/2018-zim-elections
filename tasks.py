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
def build_ds(c):
    c.run('python ./disability_senators.py')
    print('Built Disability Senators')


@task(clean, build_ds)
def build(c):
    print('Built The Project!')
