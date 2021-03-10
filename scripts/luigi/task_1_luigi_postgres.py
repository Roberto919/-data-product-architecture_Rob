from luigi.contrib.postgres import CopyToTable

import pandas as pd
import luigi
import psycopg2
import yaml


class Task1(CopyToTable):
    x = luigi.IntParameter()

    with open('credentials.yaml', 'r') as f:
        config = yaml.safe_load(f)

    credentials = config['db']

    user = credentials['user']
    password = credentials['pass']
    database = credentials['db']
    host = credentials['host']
    port = credentials['port']
    table = 'metadata'

    columns = [("col_1", "VARCHAR"),
               ("col_2", "VARCHAR")]

    def rows(self):
        z = str(self.x + self.x)
        print("########### ", z)
        r = [("test 1", z), ("test 2","45")]
        for element in r:
            yield element
