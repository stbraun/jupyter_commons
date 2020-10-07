# coding=utf-8
""" Configuration of nox test automation tool. """

import nox


@nox.session(python=['3.7', '3.8'])
def tests(session):
    session.run("pipenv", "install", external=True)
    session.run("pytest", "tests/")


@nox.session(python=['3.8'])
def lint(session):
    session.run("pipenv", "install", external=True)
    session.run("flake8", "jupyter_commons/", "tests/")
