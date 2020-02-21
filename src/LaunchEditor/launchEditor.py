# encoding: utf-8

from tempfile import NamedTemporaryFile
import os


def getEditor():

    editor = os.environ.get('EDITOR')

    if editor == None:

        raise Exception('$EDITOR undefined')

    return editor


def launchEditor(**tmpFileArgs):
    '''
    @param **tmpFileArgs: extra args to NamedTemporaryFile(), e.g.
    
        prefix='pm-msg-', suffix='.txt',
         
    '''
    
    temp = NamedTemporaryFile(delete=False, dir='.', **tmpFileArgs)
    temp.close()

    system('{} {}'.format(getEditor(), temp.name))
    
    # Now that the editor has finished, let's reopen the file
    temp = open(temp.name)
    
    msg = temp.read()
    temp.close()

    return msg
