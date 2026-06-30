import importlib.util
import sys
import os

if __name__ == "__main__":
    try:
        so_files = [f for f in os.listdir('.') if f.startswith("ShoxaGen_module") and f.endswith('.so')]
        if not so_files:
            print("Error: File .so tidak ditemukan!")
            sys.exit(1)
        
        so_file = so_files[0]

        spec = importlib.util.spec_from_file_location("ShoxaGen_module", so_file)
        module = importlib.util.module_from_spec(spec)
        sys.modules["ShoxaGen_module"] = module
        spec.loader.exec_module(module)
        
        if hasattr(module, 'make'):
            module.make()
        elif hasattr(module, 'main'):
            module.main()
        else:
            print("Module berhasil di-import!")
            print("Fungsi yang tersedia:", dir(module))
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
