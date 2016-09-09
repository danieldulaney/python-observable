import unittest


if __name__ == "__main__":
    testsuite = unittest.TestLoader().discover(".", top_level_dir="..")
    unittest.TextTestRunner().run(testsuite)
