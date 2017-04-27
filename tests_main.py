from app.room import Room
from app.dojo import Dojo
from app.living_space import LivingSpace
from app.office import Office
from app.person import Person
from app.dojo import Dojo
from app.fellow import Fellow
from app.staff import Staff
import unittest
import nose
import coverage
import os

def main():    
    file_path = os.path.abspath(__file__)
    tests_path = os.path.join(os.path.abspath(os.path.dirname(file_path)), "tests")
    result = nose.run(argv=[os.path.abspath(__file__),
                            "--with-cov", "--verbosity=3", "--cover-package=app", tests_path])

if __name__ == '__main__':
    main()
