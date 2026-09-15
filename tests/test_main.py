"""Tests for EcoBin waste classification."""

from pathlib import Path

from src.ecobin.main import categorize_waste, log_to_file


def test_categorize_recyclable():
    assert categorize_waste("plastic bottle") == "Recyclable"


def test_categorize_compostable():
    assert categorize_waste("banana peel") == "Compostable"


def test_categorize_electronic_waste():
    assert categorize_waste("old laptop") == "Electronic Waste"


def test_unknown_item_goes_to_landfill():
    assert categorize_waste("broken ceramic plate") == "Landfill"


def test_matching_is_case_insensitive():
    assert categorize_waste("GLASS BOTTLE") == "Recyclable"


def test_log_is_appended(tmp_path: Path):
    log_file = tmp_path / "waste_log.txt"
    log_to_file("banana peel", "Compostable", log_file)
    assert log_file.read_text(encoding="utf-8") == "banana peel -> Compostable\n"
