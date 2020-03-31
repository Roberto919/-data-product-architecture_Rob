from luigi.contrib.postgres import CopyToTable

import pandas as pd
import luigi


class Task2(CopyToTable):
    x = luigi.IntParameter()

    credentials = pd.read_csv("postgres_credentials.csv")
    user = credentials.user[0]
    password = credentials.password[0]
    database = credentials.database[0]
    host = credentials.host[0]
    table = 'metadata'

    columns = [("x", "VARCHAR")]

    def rows(self):
        z = str(self.x + self.x)
        print("########### ", z)
        return (z)
