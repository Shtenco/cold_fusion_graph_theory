"""Legacy bridge for the archived energy-reinvestment concept model.

The original Russian-language prototype is preserved as a historical text file
under archive/original_russian_scripts. It is not part of the verified runtime.
Use scripts/verify_all.py for the current machine-checked package.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVED_SOURCE = (
    ROOT
    / "archive"
    / "original_russian_scripts"
    / "energy_reinvestment_low_energy_transmutation_model.py.txt"
)
VERIFICATION_ENTRYPOINT = ROOT / "scripts" / "verify_all.py"


def describe() -> dict[str, str]:
    """Return the status of this archived legacy concept."""
    return {
        "status": "archived_legacy_concept",
        "archived_source": str(ARCHIVED_SOURCE),
        "verified_entrypoint": str(VERIFICATION_ENTRYPOINT),
        "safety_boundary": "Mathematical verification only; no laboratory or device instructions.",
    }


if __name__ == "__main__":
    for key, value in describe().items():
        print(f"{key}: {value}")
