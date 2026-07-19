import importlib.util
import sys
import os

if __name__ == "__main__":
    MODULE = "shoxagen"
    
    so_file = next((f for f in os.listdir('.') if f.startswith(MODULE) and (f.endswith('.so') or f.endswith('.pyd'))), None)
    
    if not so_file:
        sys.exit("File kompilasi tidak ditemukan!")
    
    try:
        spec = importlib.util.spec_from_file_location(MODULE, so_file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[MODULE] = module
        spec.loader.exec_module(module)
        
        if hasattr(module, 'make'):
            module.make()
        elif hasattr(module, 'main'):
            module.main()
            
    except Exception as e:
        sys.exit(f"Error: {e}")
