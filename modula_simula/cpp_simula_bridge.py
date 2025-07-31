'''Simula - 2025
	/*Changes:
	Array starts at 0. I dont care about breaking compat. I hate to start at 1.
	
	Also can run somewhat MODULA-2 compilant code snippets. Not perfect, but nothing is
	'''

import os
import subprocess
import re

VERBOSE=True
def run_command(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"x Command failed: {command}")
        print(f"stdout: {result.stdout.strip()}")
        print(f"stderr: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result.stdout.strip()
    
def transpile_to_cpp(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        
        stripped2=re.sub(r'!.*?!','',code,flags=re.DOTALL);
        stripped=re.sub(r'\(\*.*?\*\)','',stripped2,flags=re.DOTALL);
        updated_code = stripped.replace(':=', '=')
        
        lines= updated_code.split('\n')
        lines[0]="#include \"cpp_simula_bridge.hpp\"\nint main() "+lines[0];
        updated_code=""
        was_class=0
        for line in lines:
            if "MODULE" in line:
                line = line.replace("MODULE","#define")
            if "FROM" in line and "InOut" in line:
                line = "#include <iostream>"
            if "OutImage" in line:
                line = line.replace('OutImage','OutImage()')
            if "WriteLn" in line:
                line = line.replace('WriteLn','OutImage()')
            if "WriteString" in line:
                line = line.replace('WriteString','OutText')
            if "Class" in line:
                line = line.replace(';',' Begin public:\n')
                was_class=2 
            if "Call" in line:
                line = line.replace(';','();')
            if "Procedure" in line:
                line = line.replace(';','()')
            if ":-" not in line:
                if was_class==0:
                    
                    updated_code+=line+'\n';
                else:
                    if was_class==2:
                        updated_code+=line+'\n';
                    was_class -=1;
        new_file_name=filename+"_to"

        with open(new_file_name+".cpp", 'w', encoding='utf-8') as f:
            f.write(updated_code)

        print(f"Transpiled to CPP file: {new_file_name}")
        
        if VERBOSE==True:
            print("g++ "+new_file_name+".cpp -o "+new_file_name+" && ./"+new_file_name)
        run_command("g++ "+new_file_name+".cpp -o "+new_file_name+" && ./"+new_file_name)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python simula_replace.py <filename>.sim")
    else:
        transpile_to_cpp(sys.argv[1])
