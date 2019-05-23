#
# Created by Collin Fox 5/22/2019
#
import os, glob, shutil, sys, py_compile

def main():
	'''
	PythonHome=sys.argv[1]
	Version=""
	for character in PythonHome:
		if character.isdigit():
			Version+=character

	if Version == "":
		print("")
		print("ERROR: Unable to determine Python version from PYTHONHOME system variable as it does not have a number in it.")
		print("")
		sys.exit(0)
	else:
		majorVersion=int(Version[0:1]) #e.g. python1, python2, python3
	'''
	print("")
	
	if len(sys.argv) == 3: #specific input directory passed to pycomp.bat. Output directory is pycomp->Output
		Input=sys.argv[2]
		success=True
		print("")
		
		if os.path.isdir(Input): #directory passed
			rootPycompDir = os.getcwd()
			os.chdir(Input)
			count=0
			for file in glob.glob("*.py"):
				if (os.getcwd() != Input):
					os.chdir(Input)
				fullPath=Input+os.sep+file
				print( "Input File: " + str(fullPath))
				pathParts = fullPath.split("\\")
				filename = pathParts[len(pathParts)-1]
				os.chdir(rootPycompDir+"/Output")
				compiledScriptFullPath=os.getcwd()+os.sep+filename+"c"
				if os.path.isfile(compiledScriptFullPath):
					os.remove(compiledScriptFullPath)
				py_compile.compile(fullPath,compiledScriptFullPath)
				if os.path.isfile(compiledScriptFullPath):
					print( "Compiled to "+str(compiledScriptFullPath))
					count=count+1
					print("")
				else:
					success = False
					break
					
		elif os.path.isfile(Input): #single file passed
			count=0
			rootPycompDir = os.getcwd()
			pathParts = Input.split("\\")
			filename = pathParts[len(pathParts)-1]
			pathToFile=""
			for i in range(0,len(pathParts)-2):
				pathToFile+=pathParts[i]+os.sep
			
			fullPath=Input
			os.chdir(pathToFile)
			
			print("Input File: " + str(fullPath))
			pathParts = fullPath.split("\\")
			filename = pathParts[len(pathParts)-1]
			os.chdir(rootPycompDir+"/Output")
			compiledScriptFullPath=os.getcwd()+os.sep+filename+"c"
			if os.path.isfile(compiledScriptFullPath):
				os.remove(compiledScriptFullPath)
			py_compile.compile(fullPath,compiledScriptFullPath)
			if os.path.isfile(compiledScriptFullPath):
				print( "Compiled to "+str(compiledScriptFullPath))
				count=count+1
				print("")
			else:
				success = False	
		else:
			print("Error: input directory '"+str(Input)+"' is neither a file nor directory.")
			print("")
			count=0
			success=False
			
		if count==0:
			if success==False:
				pass
			else:
				print("No .py Files in '"+str(Input)+"' to Compile.")
				print("")
		elif success==True:
			print("Compile Completed Successfully!")	
			print("")
			
	elif len(sys.argv) == 4: #specific input AND output directories passed to pycomp.bat
		Input=sys.argv[2]
		Output=sys.argv[3]
		
		success=True
		print("")
		
		if not os.path.isdir(Output):
			print("Error: Specified Output Folder '"+str(Output)+ "' does not exist.")
			print("")
			count=0
			success=False
		
		elif os.path.isdir(Input): #directory
			rootPycompDir = os.getcwd()
			os.chdir(Input)
			count=0
			for file in glob.glob("*.py"):
				if (os.getcwd() != Input):
					os.chdir(Input)
				fullPath=Input+os.sep+file
				print( "Input File: " + str(fullPath))
				pathParts = fullPath.split("\\")
				filename = pathParts[len(pathParts)-1]
				os.chdir(Output)
				compiledScriptFullPath=os.getcwd()+os.sep+filename+"c"
				if os.path.isfile(compiledScriptFullPath):
					os.remove(compiledScriptFullPath)
				py_compile.compile(fullPath,compiledScriptFullPath)
				if os.path.isfile(compiledScriptFullPath):
					print( "Compiled to "+str(compiledScriptFullPath))
					count=count+1
					print("")
				else:
					success = False
					break
				
		elif os.path.isfile(Input): #single file passed
			count=0
			rootPycompDir = os.getcwd()
			pathParts = Input.split("\\")
			filename = pathParts[len(pathParts)-1]
			pathToFile=""
			for i in range(0,len(pathParts)-2):
				pathToFile+=pathParts[i]+os.sep
			
			fullPath=Input
			os.chdir(pathToFile)
			if ".py" not in filename:
				pass
			else:
				print( "Input File: " + str(fullPath))
				os.chdir(Output)
				compiledScriptFullPath=os.getcwd()+os.sep+filename+"c"
				if os.path.isfile(compiledScriptFullPath):
					os.remove(compiledScriptFullPath)
				py_compile.compile(fullPath,compiledScriptFullPath)
				if os.path.isfile(compiledScriptFullPath):
					print( "Compiled to "+str(compiledScriptFullPath))
					count=count+1
					print("")
				else:
					success = False
		else:
			print("Error: input directory '"+str(Input)+"' is neither a file nor directory.")
			print("")
			count=0
			success=False
			
		if count==0:
			if success==False:
				pass
			else:
				print("No .py Files in '"+str(Input)+"' to Compile.")
				print("")
		elif success==True:
			print("Compile Completed Successfully!")	
			print("")
			
	
	else: #No directories passed, using Input & Output directories (in pycomp folder) 
		success=True
		print("")
		rootPycompDir = os.getcwd()
		os.chdir("Input")
		count = 0
		for file in glob.glob("*.py"):
			count=count+1
			if "Input" not in str(os.getcwd()):
				os.chdir("../Input")
			fullPath=rootPycompDir+os.sep+"Input"+os.sep+file
			print( "Input File: " + str(fullPath))
			pathParts = fullPath.split("\\")
			filename = pathParts[len(pathParts)-1]
			os.chdir("../Output")
			compiledScriptFullPath=os.getcwd()+os.sep+filename+"c"
			if os.path.isfile(compiledScriptFullPath):
				os.remove(compiledScriptFullPath)
			py_compile.compile(fullPath,compiledScriptFullPath)
			if os.path.isfile(compiledScriptFullPath):
				
				print("Compiled to "+str(compiledScriptFullPath))
				print("")
			else:
				success = False
				break

		print("")
		
		if count==0:
			print("No .py Files in '"+str(rootPycompDir+os.sep+"Input")+"' to Compile.")
			print("")
		elif success==True:
			print("Compile Completed Successfully!")
			print("")
		
	 
if __name__ == "__main__":
    sys.exit(main())