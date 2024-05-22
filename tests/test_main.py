import subprocess

def test_yellow_banana():
    result = subprocess.run(
        ['python', '-m', 'yellow_banana.main', 'Test Message'],
        capture_output=True,
        text=True
    )
    assert 'Message: Test Message' in result.stdout
