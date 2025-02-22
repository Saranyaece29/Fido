from datetime import datetime
import pytest
from app.schemas import AudioFile, ProcessAudioRequest, ProcessAudioResponse
import base64

# Testcases for audio file validator
def test_valid_audio_file():
    encoded_audio = base64.b64encode(b"\x01" * 8000).decode()
    audio_file = AudioFile(file_name="validaudio.wav", encoded_audio=encoded_audio)
    assert audio_file.file_name == "validaudio.wav"
    print(f"Success - valid audio file")

def test_invalid_base64():
    with pytest.raises(ValueError, match="Invalid base64-encoded string"):
        AudioFile(file_name="invalidaudio.wav", encoded_audio="InvalidBase64")
    print(f"Success - validated invalid base64 audio file")

def test_short_audio():
    encoded_audio = base64.b64encode(b"\x01" * 2000).decode()
    with pytest.raises(ValueError, match="Audio file is too short"):
        AudioFile(file_name="shortaudio.wav", encoded_audio=encoded_audio)
    print(f"Success - validated short audio file")

def test_audio_file_empty_audio():
    encoded_audio = base64.b64encode(b"").decode()
    with pytest.raises(ValueError, match="Audio file is empty or has no valid data"):
        AudioFile(file_name="emptyaudio.wav", encoded_audio=encoded_audio)
    print(f"Success - validated empty audio file")


# Testcases for process audio request
def test_process_audio_request_valid():
    encoded_audio = base64.b64encode(b"\x01" * 8000).decode()
    request_data = {
        "session_id": "test_session123",
        "timestamp": datetime.now(),
        "audio_files": [
            {"file_name": "validaudio1.wav", "encoded_audio": encoded_audio},
            {"file_name": "validaudio2.wav", "encoded_audio": encoded_audio},
            {"file_name": "validaudio3.wav", "encoded_audio": encoded_audio}
        ]
    }
    request = ProcessAudioRequest(**request_data)

    assert request.session_id == "test_session123"
    assert len(request.audio_files) == 3
    assert request.audio_files[1].file_name == "validaudio2.wav"
    print(f"Success -Process audio request - schema correctly parses and sets the attributes.")


# Testcases for process audio response
def test_process_audio_response_valid():
    response_data = {
        "status": "success",
        "processed_files": [
            {"file_name": "validaudio1.wav", "length_seconds": 10.0},
            {"file_name": "validaudio2.wav", "length_seconds": 15.0}
        ]
    }
    response = ProcessAudioResponse(**response_data)

    assert response.status == "success"
    assert len(response.processed_files) == 2
    assert response.processed_files[0]["file_name"] == "validaudio1.wav"
    print(f"Success - Process audio response - schema correctly parses and sets the attributes.")

# Testcases for process invalid audio response
# Testcases for process invalid audio response