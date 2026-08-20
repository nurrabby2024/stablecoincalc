"""Minimal example for StableCoinCalc."""

from stablecoincalc import stablecoincalc


def main():
 runner = stablecoincalc({"name": "StableCoinCalc", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()