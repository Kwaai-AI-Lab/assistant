from uuid import uuid4
from datetime import datetime
from sqlmodel import Field, Relationship
from backend.db import SQLModelBase
from typing import List, Optional, ForwardRef

# Forward references
UserRef = ForwardRef("User")
CredRef = ForwardRef("Cred")
SessionRef = ForwardRef("Session")

class Config(SQLModelBase, table=True):
    key: str = Field(primary_key=True)
    value: str | None = Field(default=None)
    
class Resource(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    name: str = Field()
    uri: str = Field()
    description: str | None = Field(default=None)
    resource_llm_id: str | None = Field(default=None)
    persona_id: str | None = Field(default=None)
    status: str | None = Field(default=None)
    allow_edit: str | None = Field(default=None)
    kind: str | None = Field(default=None)
    icon: str | None = Field(default=None)
    active: str | None = Field(default=None)
    user_id: str | None = Field(default=None)

class User(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    webauthn_user_id: str = Field(unique=True, default_factory=lambda: str(uuid4()))
    name: Optional[str] = Field(default=None)
    email: str = Field()
    webauthn_user_id: str = Field()
    creds: List["Cred"] = Relationship(back_populates="user")
    sessions: List["Session"] = Relationship(back_populates="user")

class Cred(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    public_key: str = Field()
    webauthn_user_id: str = Field(foreign_key="user.webauthn_user_id")
    backed_up: str = Field()
    name: str | None = Field(default=None)
    transports: str = Field()
    user: "User" = Relationship(back_populates="creds")

class Session(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    user_id: str = Field(foreign_key="user.id")
    token: str = Field()
    expires_at: datetime = Field()
    user: User = Relationship(back_populates="sessions")

class Asset(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    user_id: str | None = Field(default=None, foreign_key="user.id")
    title: str = Field()
    creator: str | None = Field(default=None)
    subject: str | None = Field(default=None)
    description: str | None = Field(default=None)

class Persona(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    name: str = Field()
    description: str | None = Field(default=None)
    voice_id: str | None = Field(default=None)
    face_id: str | None = Field(default=None)

class Share(SQLModelBase, table=True):
    id: str = Field(primary_key=True)  # the short URL tag, eg abcd-efgh-ijkl
    resource_id: str = Field(foreign_key="resource.id")  # the bot ID
    user_id: str | None = Field(default=None)  # the user granted access (optional)
    expiration_dt: datetime | None = Field(default=None)  # the link expiration date/time (optional)
    is_revoked: bool = Field()

class File(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    name: str = Field()
    assistant_id: str = Field(foreign_key="resource.id")
    indexing_status: str = Field()

class Page(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    file_id: str= Field(foreign_key="file.id")
    assistant_id: str= Field(foreign_key="resource.id")

class Chunk(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    page_id: str= Field(foreign_key="page.id")
    file_id: str= Field(foreign_key="file.id")
    assistant_id: str= Field(foreign_key="resource.id")
    
class Message(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    assistant_id: str= Field(foreign_key="resource.id")
    conversation_id: str | None = Field(default=None, foreign_key="conversation.id")
    timestamp: str = Field()
    prompt: str = Field()
    chat_response: str = Field()
    voice_active: str = Field()

class Conversation(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    name: str = Field()
    created_timestamp: str = Field()
    last_updated_timestamp: str = Field()
    archive: str = Field()
    assistant_id: str | None = Field(default=None, foreign_key="resource.id")
    user_id: str | None = Field(default=None, foreign_key="user.id")

class Voice(SQLModelBase, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: str(uuid4()))
    xi_id: str = Field()
    name: str = Field()
    image_url: str | None = Field(default=None)
    sample_url: str | None = Field(default=None)
    
# Resolve forward references
User.model_rebuild()
Cred.model_rebuild()
Session.model_rebuild()
