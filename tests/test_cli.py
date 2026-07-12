from pathlib import Path

import pytest

from founder.cli import main
from founder.paths import LakePaths
from founder.table_io import read_json, read_rows


def test_cli_prints_project_name(capsys: pytest.CaptureFixture[str]) -> None:
    main([])

    output = capsys.readouterr()
    assert output.out == "founder\n"


def test_cli_runs_dry_run(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    main(["dry-run", "--root", str(tmp_path / "lake")])

    output = capsys.readouterr()
    assert '"canonical_rows": 2' in output.out


def test_cli_runs_search_and_fetch_modules(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    root = tmp_path / "lake"
    input_path = tmp_path / "candidates.json"
    input_path.write_text(
        """
        [
          {
            "Code": "EXAMPLE",
            "Exchange": "XETRA",
            "Type": "ETF",
            "Country": "DE",
            "Currency": "EUR",
            "Isin": "IE0000000001",
            "Name": "Example UCITS ETF"
          }
        ]
        """,
        encoding="utf-8",
    )

    main(
        [
            "search",
            "UCITS ETF",
            "--root",
            str(root),
            "--input",
            str(input_path),
            "--search-run-id",
            "search-cli",
            "--debug",
        ]
    )
    search_output = capsys.readouterr()
    assert '"canonical_rows": 1' in search_output.out

    main(
        [
            "fetch",
            "--root",
            str(root),
            "--mock",
            "--debug",
        ]
    )
    fetch_output = capsys.readouterr()
    assert '"fetch_plan_rows": 1' in fetch_output.out
    assert '"quote_rows": 2' in fetch_output.out

    paths = LakePaths(root=root)
    assert read_json(paths.current_universe())["search_run_id"] == "search-cli"
    assert len(read_rows(paths.coverage())) == 1
    log_path = next((tmp_path / ".logs").glob("founder-*.log"))
    assert " DEBUG founder.cli parsed cli args" in log_path.read_text(encoding="utf-8")
