# generated manually for a2a.json

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field, RootModel


class A2AProtocolSchema(RootModel):
    """JSON Schema for A2A Protocol"""
    root: Any = Field(..., title='A2A Protocol Schema', description='JSON Schema for A2A Protocol')


class AgentAuthentication(BaseModel):
    schemes: List[str] = Field(..., title='Schemes')
    credentials: Optional[str] = Field(None, title='Credentials')


class AgentCapabilities(BaseModel):
    streaming: bool = Field(False, title='Streaming')
    pushNotifications: bool = Field(False, title='PushNotifications')
    stateTransitionHistory: bool = Field(False, title='Statetransitionhistory')


class AgentProvider(BaseModel):
    organization: str = Field(..., title='Organization')
    url: Optional[str] = Field(None, title='Url')


class AgentSkill(BaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    description: Optional[str] = Field(None, title='Description')
    tags: Optional[List[str]] = Field(None, title='Tags')
    examples: Optional[List[str]] = Field(None, title='Examples')
    inputModes: Optional[List[str]] = Field(None, title='Inputmodes')
    outputModes: Optional[List[str]] = Field(None, title='Outputmodes')


class AuthenticationInfo(BaseModel):
    schemes: List[str] = Field(..., title='Schemes')
    credentials: Optional[str] = Field(None, title='Credentials')


class PushNotificationNotSupportedError(BaseModel):
    code: Literal[-32003] = Field(-32003, examples=[-32003], title='Code', description='Error code')
    message: Literal['Push Notification is not supported'] = Field(
        'Push Notification is not supported',
        examples=['Push Notification is not supported'],
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Any] = Field(None, title='Data')


class DataPart(BaseModel):
    type: Literal['data'] = Field('data', examples=['data'], title='Type', description='Type of the part')
    data: Dict[str, Any] = Field(..., title='Data')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class FileContent(BaseModel):
    """
    Represents the content of a file, either as base64 encoded bytes or a URI.

    Ensures that either 'bytes' or 'uri' is provided, but not both.
    """
    name: Optional[str] = Field(None, title='Name')
    mimeType: Optional[str] = Field(None, title='Mimetype')
    bytes: Optional[str] = Field(None, title='Bytes')
    uri: Optional[str] = Field(None, title='Uri')


class FilePart(BaseModel):
    type: Literal['file'] = Field('file', examples=['file'], title='Type', description='Type of the part')
    file: FileContent
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class InternalError(BaseModel):
    code: Literal[-32603] = Field(-32603, examples=[-32603], title='Code', description='Error code')
    message: Literal['Internal error'] = Field(
        'Internal error', 
        examples=['Internal error'], 
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Dict[str, Any]] = Field(None, title='Data')


class InvalidParamsError(BaseModel):
    code: Literal[-32602] = Field(-32602, examples=[-32602], title='Code', description='Error code')
    message: Literal['Invalid parameters'] = Field(
        'Invalid parameters',
        examples=['Invalid parameters'],
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Dict[str, Any]] = Field(None, title='Data')


class InvalidRequestError(BaseModel):
    code: Literal[-32600] = Field(-32600, examples=[-32600], title='Code', description='Error code')
    message: Literal['Request payload validation error'] = Field(
        'Request payload validation error',
        examples=['Request payload validation error'],
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Dict[str, Any]] = Field(None, title='Data')


class JSONParseError(BaseModel):
    code: Literal[-32700] = Field(-32700, examples=[-32700], title='Code', description='Error code')
    message: Literal['Invalid JSON payload'] = Field(
        'Invalid JSON payload',
        examples=['Invalid JSON payload'],
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Dict[str, Any]] = Field(None, title='Data')


class JSONRPCError(BaseModel):
    code: int = Field(..., title='Code')
    message: str = Field(..., title='Message')
    data: Optional[Dict[str, Any]] = Field(None, title='Data')


class JSONRPCMessage(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')


class JSONRPCRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: str = Field(..., title='Method')
    params: Optional[Dict[str, Any]] = Field(None, title='Params')


class JSONRPCResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[Dict[str, Any]] = Field(None, title='Result')
    error: Optional[JSONRPCError] = None


class Role(Enum):
    user = 'user'
    agent = 'agent'


class MethodNotFoundError(BaseModel):
    code: Literal[-32601] = Field(-32601, examples=[-32601], title='Code', description='Error code')
    message: Literal['Method not found'] = Field(
        'Method not found', 
        examples=['Method not found'], 
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Any] = Field(None, title='Data')


class PushNotificationConfig(BaseModel):
    url: str = Field(..., title='Url')
    token: Optional[str] = Field(None, title='Token')
    authentication: Optional[AuthenticationInfo] = None


class TaskPushNotificationConfig(BaseModel):
    id: str = Field(..., title='Id')
    pushNotificationConfig: PushNotificationConfig


class TaskNotCancelableError(BaseModel):
    code: Literal[-32002] = Field(-32002, examples=[-32002], title='Code', description='Error code')
    message: Literal['Task cannot be canceled'] = Field(
        'Task cannot be canceled',
        examples=['Task cannot be canceled'],
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Any] = Field(None, title='Data')


class TaskNotFoundError(BaseModel):
    code: Literal[-32001] = Field(-32001, examples=[-32001], title='Code', description='Error code')
    message: Literal['Task not found'] = Field(
        'Task not found', 
        examples=['Task not found'], 
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Any] = Field(None, title='Data')


class TaskIdParams(BaseModel):
    id: str = Field(..., title='Id')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class TaskQueryParams(BaseModel):
    id: str = Field(..., title='Id')
    historyLength: Optional[int] = Field(None, title='HistoryLength')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class TaskState(Enum):
    """An enumeration."""
    submitted = 'submitted'
    working = 'working'
    input_required = 'input-required'
    completed = 'completed'
    canceled = 'canceled'
    failed = 'failed'
    unknown = 'unknown'


class TextPart(BaseModel):
    type: Literal['text'] = Field('text', examples=['text'], title='Type', description='Type of the part')
    text: str = Field(..., title='Text')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class UnsupportedOperationError(BaseModel):
    code: Literal[-32004] = Field(-32004, examples=[-32004], title='Code', description='Error code')
    message: Literal['This operation is not supported'] = Field(
        'This operation is not supported',
        examples=['This operation is not supported'],
        title='Message',
        description='A short description of the error'
    )
    data: Optional[Any] = Field(None, title='Data')


class Part(RootModel):
    root: Union[TextPart, FilePart, DataPart] = Field(..., title='Part')


class TaskStatus(BaseModel):
    state: TaskState
    message: Optional['Message'] = None
    timestamp: Optional[datetime] = Field(None, title='Timestamp')


class Message(BaseModel):
    role: Role = Field(..., title='Role')
    parts: List[Part] = Field(..., title='Parts')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class Artifact(BaseModel):
    name: Optional[str] = Field(None, title='Name')
    description: Optional[str] = Field(None, title='Description')
    parts: List[Part] = Field(..., title='Parts')
    index: Optional[int] = Field(0, title='Index')
    append: Optional[bool] = Field(None, title='Append')
    lastChunk: Optional[bool] = Field(None, title='LastChunk')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class Task(BaseModel):
    id: str = Field(..., title='Id')
    sessionId: Optional[str] = Field(None, title='Sessionid')
    status: TaskStatus
    artifacts: Optional[List[Artifact]] = Field(None, title='Artifacts')
    history: Optional[List[Message]] = Field(None, title='History')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class TaskSendParams(BaseModel):
    id: str = Field(..., title='Id')
    sessionId: Optional[str] = Field(None, title='Sessionid')
    message: Message
    pushNotification: Optional[PushNotificationConfig] = None
    historyLength: Optional[int] = Field(None, title='HistoryLength')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class TaskStatusUpdateEvent(BaseModel):
    id: str = Field(..., title='Id')
    status: TaskStatus
    final: Optional[bool] = Field(False, title='Final')
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class TaskArtifactUpdateEvent(BaseModel):
    id: str = Field(..., title='Id')
    artifact: Artifact
    metadata: Optional[Dict[str, Any]] = Field(None, title='Metadata')


class TaskResubscriptionRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/resubscribe'] = Field('tasks/resubscribe', title='Method')
    params: TaskQueryParams


class SendTaskRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/send'] = Field('tasks/send', title='Method')
    params: TaskSendParams


class SendTaskStreamingRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/sendSubscribe'] = Field('tasks/sendSubscribe', title='Method')
    params: TaskSendParams


class SendTaskStreamingResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[Union[TaskStatusUpdateEvent, TaskArtifactUpdateEvent]] = None
    error: Optional[JSONRPCError] = None


class AgentCard(BaseModel):
    name: str = Field(..., title='Name')
    description: Optional[str] = Field(None, title='Description')
    url: str = Field(..., title='Url')
    provider: Optional[AgentProvider] = None
    version: str = Field(..., title='Version')
    documentationUrl: Optional[str] = Field(None, title='Documentationurl')
    capabilities: AgentCapabilities
    authentication: Optional[AgentAuthentication] = None
    defaultInputModes: List[str] = Field(default=['text'], title='Defaultinputmodes')
    defaultOutputModes: List[str] = Field(default=['text'], title='Defaultoutputmodes')
    skills: List[AgentSkill] = Field(..., title='Skills')


class GetTaskRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/get'] = Field('tasks/get', title='Method')
    params: TaskQueryParams


class GetTaskResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[Task] = None
    error: Optional[JSONRPCError] = None


class CancelTaskRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/cancel'] = Field('tasks/cancel', title='Method')
    params: TaskIdParams


class CancelTaskResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[Task] = None
    error: Optional[JSONRPCError] = None


class SendTaskResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[Task] = None
    error: Optional[JSONRPCError] = None


class SetTaskPushNotificationRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/pushNotification/set'] = Field('tasks/pushNotification/set', title='Method')
    params: TaskPushNotificationConfig


class SetTaskPushNotificationResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[TaskPushNotificationConfig] = None
    error: Optional[JSONRPCError] = None


class GetTaskPushNotificationRequest(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    method: Literal['tasks/pushNotification/get'] = Field('tasks/pushNotification/get', title='Method')
    params: TaskIdParams


class GetTaskPushNotificationResponse(BaseModel):
    jsonrpc: Literal['2.0'] = Field('2.0', title='Jsonrpc')
    id: Optional[Union[int, str]] = Field(None, title='Id')
    result: Optional[TaskPushNotificationConfig] = None
    error: Optional[JSONRPCError] = None


class A2ARequest(RootModel):
    root: Union[
        SendTaskRequest,
        GetTaskRequest,
        CancelTaskRequest,
        SetTaskPushNotificationRequest,
        GetTaskPushNotificationRequest,
        TaskResubscriptionRequest,
    ] = Field(..., title='A2ARequest')
