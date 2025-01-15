from datetime import datetime, timezone
from fastapi.encoders import isoformat
from fastapi.testclient import TestClient
from app.database import create_tables
from app.main import app
import base64
from app.schemas import ProcessAudioResponse

client = TestClient(app)

create_tables() 

def test_process_audio_valid():
    payload = {
        "session_id": "test_session",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "audio_files": [
            {
                "file_name": "test.wav",
                "encoded_audio": base64.b64encode(b"\x01" * 8000).decode()
            }
        ]
    }
    response = client.post("/process-audio", json=payload)
    response_json = response.json()

    try:
        assert response.status_code == 200
        assert response_json["status"] == "success"
        assert len(response_json["processed_files"]) == 1
    except AssertionError as e:
        print(response_json)  # Print the response JSON for debugging
        raise e
    

def test_process_audio_invalid_base64():
    payload = {
        "session_id": "test_session",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "audio_files": [
            {
                "file_name": "test_file.wav",
                "encoded_audio": "InvalidBase64String==="
            }
        ]
    }
    response = client.post("/process-audio", json=payload)
    #assert response.status_code == 400
    assert response.status_code == 422  # Expecting 422 Unprocessable Entity
    response_json = response.json()
