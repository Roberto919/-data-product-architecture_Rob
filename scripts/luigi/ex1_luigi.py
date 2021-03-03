# tienes quu hacer este script visible al pythonpath!
# puedes agregar antes de la ejecución PYTHONPATH="." luigi --module ex1 MyTask --local-scheduler --x 123
import luigi

class MyTask(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=45)

    def run(self):
        print("******* ", str(self.x + self.y))
