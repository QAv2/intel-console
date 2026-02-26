"""Pydantic request/response models."""

from pydantic import BaseModel, Field


# ---- Entities ----

class EntityCreate(BaseModel):
    name: str
    entity_type: str
    description: str = ""
    aliases: str = ""
    metadata: dict = Field(default_factory=dict)


class EntityUpdate(BaseModel):
    name: str | None = None
    entity_type: str | None = None
    description: str | None = None
    aliases: str | None = None
    metadata: dict | None = None


class EntityOut(BaseModel):
    id: int
    name: str
    entity_type: str
    description: str
    aliases: str
    metadata: dict


# ---- Relationships ----

class RelationshipCreate(BaseModel):
    source_id: int
    target_id: int
    relationship_type: str
    evidence_tier: str
    description: str = ""
    year_start: int | None = None
    year_end: int | None = None
    source_ids: list[int] = Field(default_factory=list)


class RelationshipOut(BaseModel):
    id: int
    source_id: int
    target_id: int
    relationship_type: str
    evidence_tier: str
    description: str
    year_start: int | None
    year_end: int | None
    sources: list[dict] = Field(default_factory=list)


# ---- Sources ----

class SourceCreate(BaseModel):
    title: str
    url: str = ""
    source_type: str = "journalism"
    author: str = ""
    year: int | None = None


class SourceOut(BaseModel):
    id: int
    title: str
    url: str
    source_type: str
    author: str
    year: int | None


# ---- Graph ----

class GraphNode(BaseModel):
    id: int
    name: str
    entity_type: str
    connection_count: int = 0
    photo_url: str = ""


class GraphEdge(BaseModel):
    id: int
    source: int
    target: int
    relationship_type: str
    evidence_tier: str
    description: str = ""
    year_start: int | None = None
    year_end: int | None = None


class GraphData(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]


# ---- Stats ----

class Stats(BaseModel):
    entities: int
    relationships: int
    sources: int
    by_type: dict[str, int]
    by_tier: dict[str, int]
