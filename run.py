if __name__ == "__main__":
    try:
        __import__("ShoxaGen_module").make()
    except Exception as e:
        exit(str(e))
