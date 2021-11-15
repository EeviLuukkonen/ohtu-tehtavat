from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        parsed_toml = toml.loads(content)

        a = []
        for i in parsed_toml["tool"]["poetry"]["dependencies"]:
            a.append(i)

        b = []
        for i in parsed_toml["tool"]["poetry"]["dev-dependencies"]:
            b.append(i)

        print(parsed_toml)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_toml["tool"]["poetry"]["name"], parsed_toml["tool"]["poetry"]["description"], a, b)
