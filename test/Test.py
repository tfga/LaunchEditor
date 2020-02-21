import unittest
from LaunchEditor.launchEditor import getEditor, LaunchEditorException,\
    launchEditor, SystemException
from mock.mock import patch
import os
from AssertThrowsMixin import AssertThrowsMixin


class Test(unittest.TestCase, AssertThrowsMixin):

    @patch.dict(os.environ, { 'EDITOR': 'my-editor' })
    def test_getEditor_happy_path(self):
        
        self.assertEquals(getEditor(), 'my-editor')
        

    @patch('os.environ', {})
    def test_EDITOR_not_set(self):
        
        self.assertThrows(getEditor, LaunchEditorException, '$EDITOR undefined')
        
        
    @patch.dict(os.environ, { 'EDITOR': 'non-existent-editor' })
    def test_launchEditor_editor_fails(self):
        
        self.assertThrows(launchEditor, SystemException, 'Editor failed with status 32512')
        
        
    def _test_launchEditor_for_real(self):
        
        print "'{}'".format(launchEditor())
            

        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    