#!/usr/bin/env python
import sys
import importlib

# Test if functions are defined in generator module
print("Testing if functions are defined in generator module...")

# First, let's directly exec the generator file content
print("\nAttempting direct import...")

try:
    import rag.generator as gen_module
    print(f"Module imported: {gen_module}")
    print(f"Module file: {gen_module.__file__}")
    print(f"Module dict keys: {list(gen_module.__dict__.keys())}")
    
    # Check specific functions
    print(f"\nFunction 'build_prompt' defined: {hasattr(gen_module, 'build_prompt')}")
    print(f"Function 'generate_answer' defined: {hasattr(gen_module, 'generate_answer')}")
    
    # If functions exist, try to access them
    if hasattr(gen_module, 'generate_answer'):
        print(f"generate_answer: {gen_module.generate_answer}")
    else:
        print("generate_answer NOT FOUND in module")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

# Now let's read the actual file and check it
print("\n\nReading generator.py file directly...")
with open('rag/generator.py', 'r') as f:
    content = f.read()
    print(f"File size: {len(content)} bytes")
    print(f"'def generate_answer' in file: {'def generate_answer' in content}")
    print(f"'def build_prompt' in file: {'def build_prompt' in content}")
    
    # Print first 500 chars
    print(f"\nFirst 500 chars of file:\n{content[:500]}")
