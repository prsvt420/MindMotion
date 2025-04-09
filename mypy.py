import subprocess
import sys

result: subprocess.CompletedProcess = subprocess.run(
    ["mypy", "."], capture_output=True, text=True, check=False
)

print(result.stdout)  # noqa
print(result.stderr, file=sys.stderr)  # noqa

sys.exit(result.returncode)
