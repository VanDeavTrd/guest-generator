if __name__ == "__main__":
    try:
        __import__("ShoxaGen").make()
    except Exception as e:
        exit(str(e))
