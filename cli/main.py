from services.orchestrator import Orchestrator
import sys

def main(args):
    orchestrator = Orchestrator()
    orchestrator.start()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))