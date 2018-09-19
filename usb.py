from platform import system
from subprocess import call
import win32file
import os
import os.path

os.system('color b')


bisrat = '''                                        ___          
                   ========================
                   \.     USB SCANNER    ../
                    \....            ...../
                     \__________________/
                     '''

drive_list = []
drivebits=win32file.GetLogicalDrives()
for d in range(1,26):
   mask=1 << d
   if drivebits & mask:
      drname='%c:\\' % chr(ord('A')+d)
      t=win32file.GetDriveType(drname)
      if t == win32file.DRIVE_REMOVABLE:
         drive_list.append(drname)
if drive_list:
   for USB in drive_list:
       print bisrat
       Usb = USB+'\\'
       os.chdir('%s'%Usb)
       call(["attrib", "-H", '-r', '-s', '/s', '/d', '*.*'])
       #####################################################
       #-----------USB SCANNER --------------#
       #####################################################
       Lnk = 'lnk' 
       exten = '.%s'%(Lnk)
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB0 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB0
                  os.remove(KB0)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       Ini = 'ini' 
       exten = '.%s'%(Ini)
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB1 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB1
                  os.remove(KB1)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       Bak = 'bak' 
       exten = '.%s'%(Bak)
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB2 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB2
                  os.remove(KB2)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Porn.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB3 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB3
                  os.remove(KB3)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Music.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB4 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB4
                  os.remove(KB4)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Nurd.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB5 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB5
                  os.remove(KB5)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'IndexerVolumeGuid'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB6 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB6
                  os.remove(KB6)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Sex.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB7 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB7
                  os.remove(KB7)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = '_05040.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB8 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB8
                  os.remove(KB8)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = '_INDRV.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB9 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB9
                  os.remove(KB9)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Documents.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB10 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB10
                  os.remove(KB10)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Movies.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB11 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB11
                  os.remove(KB11)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Pictures.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB12 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB12
                  os.remove(KB12)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Private.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB13 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB13
                  os.remove(KB13)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Secret.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB14 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB14
                  os.remove(KB14)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = '_UTORUN.INF'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB15 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB15
                  os.remove(KB15)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'System Volume Information.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB16 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB16
                  os.remove(KB16)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'SysAnti.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB17 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB17
                  os.remove(KB17)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'Exam.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB18 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB18
                  os.remove(KB18)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'service.exe'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB19 = os.path.join(dirname, name)
                  print 'Virus Found In: '+KB19
                  os.remove(KB19)
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       exten = 'AutoRun.inf'
       def step(ext, dirname, names):
           ext = ext.lower()
           for name in names:
               if name.lower().endswith(ext):
                  KB20 = os.path.join(dirname, name)
                  print 'AUTORUN Found In: '+KB18
                  KBB20 = raw_input('Do You Have Remove AutoRun.inf (y/n): ').lower()
                  if KBB20 == 'y':
                     os.remove(KB20)
                     print 'OK...AutoRun.inf Remove Is Done'
                  elif KBB20 == 'n':
                     print 'OK...AutoRun.inf NOT Remove Is Done'
                  else:
                     print 'ERROR: Just Type \"Y\" or \"N\"....TryAgin'
       os.path.walk(Usb, step, exten)
       #----------------------------------------------------
       print 'REMOVE(Delete)...Scan-DONE!'
       
elif not drive_list:
   os.system('color c')
   W13 = '''#No USB (Removable Disk) DRIVE IS DETECTED Or'''
   print bisrat
   print W13
raw_input('\nPress ENTER To Exit...Virus Cleared!')
   


