import subprocess
import sys

def main():
    print("Starting Lunaar MkDocs server...")
    try:
        subprocess.run([sys.executable, "-m", "mkdocs", "serve"], check=True)
    except KeyboardInterrupt:
        print("\nShutting down MkDocs server...")
    except subprocess.CalledProcessError as e:
        print(f"Error while running MkDocs: {e}")

if __name__ == "__main__":
    main()
