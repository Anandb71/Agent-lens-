import os
import httpx
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

BACKEND_URL = os.getenv("AGENT_LENS_BACKEND_URL", "http://127.0.0.1:8000/log/")
REQUEST_TIMEOUT = float(os.getenv("AGENT_LENS_LOG_TIMEOUT", "5.0"))

async def log_step(session_id: int, step_type: str, content: str, **kwargs) -> bool:
    """
    Log a step asynchronously to the Agent-Lens backend.
    Additional kwargs will be merged into the payload.
    Returns True if successful, False otherwise.
    """
    payload: Dict[str, Any] = {
        "step_type": step_type,
        "content": content,
        "session_id": session_id,
    }
    payload.update(kwargs)

    try:
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.post(BACKEND_URL, json=payload)
            response.raise_for_status()
            return True
    except httpx.RequestError as e:
        logger.warning(f"Could not connect to Agent-Lens backend: {e}. Logging step failed.")
    except httpx.HTTPStatusError as e:
        logger.warning(f"Backend returned error status {e.response.status_code}. Logging step failed.")
    except Exception as e:
        logger.warning(f"Unexpected error while logging: {e}")
        
    return False

def log_step_sync(session_id: int, step_type: str, content: str, **kwargs) -> bool:
    """
    Synchronous counterpart for log_step.
    """
    payload: Dict[str, Any] = {
        "step_type": step_type,
        "content": content,
        "session_id": session_id,
    }
    payload.update(kwargs)

    try:
        with httpx.Client(timeout=REQUEST_TIMEOUT) as client:
            response = client.post(BACKEND_URL, json=payload)
            response.raise_for_status()
            return True
    except httpx.RequestError as e:
        logger.warning(f"Could not connect to Agent-Lens backend: {e}. Logging step failed.")
    except httpx.HTTPStatusError as e:
        logger.warning(f"Backend returned error status {e.response.status_code}. Logging step failed.")
    except Exception as e:
        logger.warning(f"Unexpected error while logging: {e}")
        
    return False
