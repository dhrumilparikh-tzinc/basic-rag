import sys
import traceback

print("Attempting to import rag.generator module...")
try:
    import rag.generator
    print("Successfully imported rag.generator module")
except Exception as e:
    print(f"Exception occurred during import:")
    print(f"Exception Type: {type(e).__name__}")
    print(f"Exception Message: {str(e)}")
    print("\nFull Traceback:")
    traceback.print_exc()
