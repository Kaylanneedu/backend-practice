# tests/test_highscore.py
import highscore

def test_load_highscores_empty_when_file_missing(tmp_path, monkeypatch):
    fake_file = tmp_path / "highscores.json"
    monkeypatch.setattr(highscore, "HIGHSCORE_FILE", str(fake_file))

    result = highscore.load_highscores()
    assert result == {}

def test_save_and_load_highscores(tmp_path, monkeypatch):
    fake_file = tmp_path / "highscores.json"
    monkeypatch.setattr(highscore, "HIGHSCORE_FILE", str(fake_file))

    highscore.save_highscores({"Easy": 3, "Medium": 5})
    result = highscore.load_highscores()

    assert result == {"Easy": 3, "Medium": 5}

def test_save_overwrites_previous_scores(tmp_path, monkeypatch):
    fake_file = tmp_path / "highscores.json"
    monkeypatch.setattr(highscore, "HIGHSCORE_FILE", str(fake_file))

    highscore.save_highscores({"Easy": 3})
    highscore.save_highscores({"Easy": 2})

    result = highscore.load_highscores()
    assert result == {"Easy": 2}