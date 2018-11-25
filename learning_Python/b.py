import sys
sys.path.append('.') # manually modify sys.path
import a # execute the the top-level code

a.module()

print(sys.modules) # import modules dict
print(sys.path) # modules search path

