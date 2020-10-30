import unittest
from Sprint2 import searchByYears, getID

#tests for searching how many people were born in a given time frame.
#tests for searching how many people were born in a given time frame.
class BuggyGedcom(unittest.TestCase):
    def test_searchByYear(self):
        #test 1
        self.assertEqual(searchByYears("test GEDCOM file",1950,1970),3)
        #test 2
        self.assertEqual(searchByYears("test GEDCOM file",1900,2000),10)
        #test 3
        self.assertEqual(searchByYears("test GEDCOM file",1970,2000),7)
    
    def test_getId(self):
        #test 1
        self.assertEqual(getID("test GEDCOM file"), {'Nancy': 'I01', 'Jack': 'I02', 'Mike': 'I03', 'Greg': 'I07', 'Emma': 'I05', 'STEVE': 'I06'})

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)