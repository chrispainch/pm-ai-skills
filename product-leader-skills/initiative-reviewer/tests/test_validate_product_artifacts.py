import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_product_artifacts", ROOT / "scripts" / "validate_product_artifacts.py"
)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class ProductArtifactContractTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.product_root = self.temp_dir / "product"
        shutil.copytree(ROOT / "tests" / "fixtures" / "complete-product" / "product", self.product_root)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_complete_fixture_is_valid(self):
        self.assertEqual(validator.validate(self.product_root), [])

    def test_missing_required_framing_fails(self):
        (self.product_root / "initiatives" / "invite-consent" / "framing.md").unlink()
        errors = validator.validate(self.product_root)
        self.assertTrue(any("missing required framing.md" in error for error in errors))

    def test_missing_product_direction_fails(self):
        (self.product_root / "strategy" / "direction" / "product-direction.md").unlink()
        errors = validator.validate(self.product_root)
        self.assertTrue(any("missing required product direction" in error for error in errors))

    def test_wrong_initiative_filename_fails(self):
        initiative = self.product_root / "initiatives" / "invite-consent"
        (initiative / "solution.md").rename(initiative / "proposal.md")
        errors = validator.validate(self.product_root)
        self.assertTrue(any("missing solution.md" in error for error in errors))
