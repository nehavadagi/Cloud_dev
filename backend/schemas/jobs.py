from pydantic import BaseModel

class JobCreate(BaseModel):
    task_type: str
    input_data: str

class JobStatusResponse(BaseModel):
    status: str
    output: str | None
