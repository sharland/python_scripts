Python 3.1.3 (r313:86834, Nov 27 2010, 18:30:53) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
x is 2
>>> ================================ RESTART ================================
>>> 
x is 2
Traceback (most recent call last):
  File "F:/func_nonlocal.py", line 14, in <module>
    print('changed local x to', x)
NameError: name 'x' is not defined
>>> ================================ RESTART ================================
>>> 
x is 2
changed local x to 0
Traceback (most recent call last):
  File "F:/func_nonlocal.py", line 18, in <module>
    func_inner()
NameError: name 'func_inner' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "F:/func_nonlocal.py", line 14, in <module>
    func_inner()
NameError: name 'func_inner' is not defined
>>> ================================ RESTART ================================
>>> 
x is 2
changed local x to 5
>>> 
