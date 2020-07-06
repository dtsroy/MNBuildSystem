import os, sys
sys.path.insert(0, os.path.abspath('Plugin'))
os.chdir(sys.path[0])
import mn
if __name__ == '__main__':
	mn.main()
