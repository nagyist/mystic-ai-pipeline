from typing import Optional

from pipeline.schemas.base import BaseModel
from pipeline.schemas.file import FileGet


class ModelBase(BaseModel):
    id: str
    name: str


class ModelGet(ModelBase):
    hex_file: FileGet

    source_sample: str

    class Config:
        orm_mode = True


class ModelGetDetailed(ModelGet):
    ...


class ModelGetOverview(ModelBase):
    description: str
    pipeline_count: int


class ModelCreate(BaseModel):
    # The local ID is assigned when a new model is used as part of a new
    # pipeline; the server uses the local ID to associated a model to a
    # Pipeline before replacing the local ID with the server-generated one
    local_id: Optional[str]

    model_source: str
    hash: str
    name: str
