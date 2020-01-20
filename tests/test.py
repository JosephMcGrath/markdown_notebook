import unittest
import shutil, tempfile
import os
from tidynotes.notebook import Tidybook


class TidynoteInit(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_notebook_creation_explicit(self):
        book = Tidybook(self.test_dir, initialise=True)

        resource_map = book.resource_map
        paths = [os.path.join(resource_map[x], x) for x in resource_map]
        for path in paths:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, path)))

    def test_notebook_creation_implicit(self):
        book = Tidybook(self.test_dir, initialise=False)

        resource_map = book.resource_map
        paths = [os.path.join(resource_map[x], x) for x in resource_map]
        for path in paths:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, path)))

    def test_notebook_creation_cli_explicit(self):
        cmd = f'tidynotes -notedir "{self.test_dir}" -i'
        os.system(cmd)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "config.json")))

    def test_notebook_creation_cli_implicit(self):
        cmd = f'tidynotes -notedir "{self.test_dir}"'
        os.system(cmd)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "config.json")))

    def test_notebook_creation_cli_implicit_blocked(self):
        with open(os.path.join(self.test_dir, "temp.txt"), "w") as f:
            f.write(" ")
        cmd = f'tidynotes -notedir "{self.test_dir}"'
        os.system(cmd)
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, "config.json")))


if __name__ == "__main__":
    unittest.main()