import os
from mock.mock import patch
from LaunchEditor.launchEditor import getEditor, LaunchEditorException,\
    SystemException, launchEditor
from AssertRaises import assertRaises



@patch.dict(os.environ, { 'EDITOR': 'my-editor' })
def test_getEditor_happy_path():
     
    assert getEditor() == 'my-editor'
     
 
@patch('os.environ', {})
def test_EDITOR_not_set():
     
    assertRaises(getEditor, LaunchEditorException, '\$EDITOR undefined')
        
    
@patch.dict(os.environ, { 'EDITOR': 'non-existent-editor' })
def test_launchEditor_editor_fails():
     
    assertRaises(launchEditor, SystemException, 'Editor failed with status 32512')
    
     
def _test_launchEditor_for_real(self):
     
    print "'{}'".format(launchEditor())
