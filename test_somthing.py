__author__ = 'Sergey'

import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys


sys.path.append("TestStack.White.9.2.0.11\\lib\\net40")
sys.path.append("Castle.Core.3.1.0\\lib\\net40-client")
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application

def test_somthing():
    Application.Launch("notepad.exe")
    print ('ok')