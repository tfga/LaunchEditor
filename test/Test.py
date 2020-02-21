import unittest
from LaunchEditor.launchEditor import getEditor, LaunchEditorException
from mock.mock import patch
import os


class Test(unittest.TestCase):

    @patch.dict(os.environ, { 'EDITOR': 'my-editor' })
    def test_happy_path(self):
        
        self.assertEquals(getEditor(), 'my-editor')
        

    @patch('os.environ', {})
    def test_EDITOR_not_set(self):
        
        with self.assertRaises(LaunchEditorException) as cm:
            
            getEditor()
            
        self.assertEqual(cm.exception.message, '$EDITOR undefined')

        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    