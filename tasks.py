from invoke import task
from invoke import run 

@task
def clean():
    run("cd lessons && make clean")

@task
def build(docs=False, impress=False, pdf=False):
    if docs:
        run("cd lessons && make html")
    if pdf:
        run("cd lessons && make latexpdf")
    if impress:
        run("cd lessons && hovercraft impress/index_impress.rst _build/impress/", echo=True, pty=True)
        run("cp -f lessons/_static/impressConsole.css lessons/_build/impress/css", echo=True, pty=True)
