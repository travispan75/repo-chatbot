import sys
from pipeline_runner import Pipeline

def main(argv):
    if len(argv) != 2:
        print("Usage: python main.py <path-to-repo>")
        sys.exit(1)

    repo_path = argv[1]

    pipeline = Pipeline()
    pipeline.run(repo_path)

if __name__ == "__main__":
    main(sys.argv)