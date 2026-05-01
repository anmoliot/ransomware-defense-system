import os
import time

class CanaryManager:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.canary_files = [
            'salary.xlsx',
            'passwords.txt',
            'tax_returns.pdf'
        ]
        self.deployed_paths = set()

    def deploy(self):
        """Creates dummy files in the target directory."""
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

        for filename in self.canary_files:
            path = os.path.join(self.target_dir, filename)
            try:
                with open(path, 'w') as f:
                    f.write("CONFIDENTIAL DATA DO NOT DISTRIBUTE\n" * 100)
                self.deployed_paths.add(os.path.abspath(path))
            except Exception as e:
                print(f"Failed to deploy canary {path}: {e}")

    def is_canary(self, path: str) -> bool:
        """Checks if a given path is a canary file."""
        return os.path.abspath(path) in self.deployed_paths
