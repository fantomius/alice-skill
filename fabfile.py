# coding: utf-8

from fabric.api import task, local


@task
def train():
    local('python -m rasa_nlu.train --config nlu_config.yml --data demo-rasa.json --path projects')


@task
def run():
    local('python bot.py')
