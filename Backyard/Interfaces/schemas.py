from typing import Any
from sqlalchemy import ForeignKey, String, Double, Uuid, create_engine, Column, Date, DateTime
from sqlalchemy.orm import DeclarativeBase
import uuid

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__   = 'roles'

    role_name       = Column('role_name', String, primary_key=True)

    def __init__(self, role_name):
        self.role_name  = role_name

    def __repr__(self) -> str:
        return f'Role: {self.role_name}'

class User(Base):
    __tablename__ = 'users'

    user_id     = Column('user_id', Uuid, primary_key=True)
    name        = Column('name', String)
    email       = Column('email', String)
    role        = Column(String, ForeignKey('roles.role_name'))

    def __init__(self, name, email, role):
        self.user_id    = uuid.uuid4()
        self.name       = name
        self.email      = email
        self.role       = role

    def __repr__(self) -> str:
        return f'{self.name} {self.email} with user_id: {self.user_id} ({self.role})'
    
class Job(Base):
    __tablename__ = 'jobs'

    job_id      = Column('job_id', Uuid, primary_key=True)
    client_id   = Column(Uuid, ForeignKey('users.user_id'))
    gc_id       = Column(Uuid, ForeignKey('users.user_id'))
    start_date  = Column('start_date', Date)
    end_date    = Column('end_date', Date)

    def __init__(self, client_id, gc_id, start_date, end_date):
        self.job_id     = uuid.uuid4()
        self.client_id  = client_id
        self.gc_id      = gc_id
        self.start_date = start_date
        self.end_date   = end_date

    def __repr__(self) -> str:
        return f'{self.gc_id} is the general contractor on {self.job_id} with client: {self.client_id}\nStart: {self.start_date}\nEnd: {self.end_date}'
    

class Document(Base):
    __tablename__ = 'documents'

    document_id     = Column('document_id', Uuid, primary_key=True)
    job_id          = Column(Uuid, ForeignKey('jobs.job_id'))
    s3_key          = Column('s3_key', String)
    type            = Column('type', String)
    d_metadata        = Column('d_metadata', String)

    def __init__(self, job_id, s3_key, type, d_metadata):
        self.document_id    = uuid.uuid4()
        self.job_id         = job_id
        self.s3_key         = s3_key
        self.type           = type
        self.d_metadata       = d_metadata

    def __repr__(self) -> str:
        return f'Document_id: {self.document_id} ({self.job_id}) ({self.s3_key}) ({self.type}) ({self.d_metadata})'

class Event(Base):
    __tablename__   = 'events'

    event_id        = Column('event_id', Uuid, primary_key=True)
    job_id          = Column(Uuid, ForeignKey('jobs.job_id'))
    date_time       = Column('date_time', DateTime)
    e_metadata        = Column('metadata', String)

    def __init__(self, job_id, date_time, e_metadata):
        self.event_id   = uuid.uuid4()
        self.job_id     = job_id
        self.date_time  = date_time
        self.e_metadata   = e_metadata

    def __repr__(self) -> str:
        return f'Event_id: {self.event_id} ({self.job_id}) ({self.date_time}) ({self.e_metadata})'

class Invoice(Base):
    __tablename__       = 'invoices'

    invoice_id          = Column('invoice_id', Uuid, primary_key=True)
    job_id              = Column(Uuid, ForeignKey('jobs.job_id'))
    created_date        = Column('created_date', Date)
    due_date            = Column('due_date', Date)
    amount_total        = Column('amount_total', Double)
    amount_paid         = Column('amount_paid', Double)

    def __init__(self, job_id, created_date, due_date, amount_total, amount_paid):
        self.invoice_id     = uuid.uuid4()
        self.job_id         = job_id
        self.created_date   = created_date
        self.due_date       = due_date
        self.amount_total   = amount_total
        self.amount_paid    = amount_paid

    def __repr__(self) -> str:
        return f'Invoice: {self.invoice_id} ({self.job_id}) ({self.created_date}) ({self.due_date}) ({self.amount_total}, {self.amount_paid})'

class Photo(Base):
    __tablename__   = 'photos'

    photo_id        = Column('photo_id', Uuid, primary_key=True)
    job_id          = Column(Uuid, ForeignKey('jobs.job_id'))
    s3_key          = Column('s3_key', String)
    p_metadata        = Column('p_metadata', String)

    def __init__(self, job_id, s3_key, p_metadata):
        self.photo_id       = uuid.uuid4()
        self.job_id         = job_id
        self.s3_key         = s3_key
        self.p_metadata       = p_metadata

    def __repr__(self) -> str:
        return f'{self.photo_id} ({self.job_id}) ({self.s3_key}) ({self.p_metadata})'

class Product(Base):
    __tablename__   = 'products'

    product_id      = Column('product_id', Uuid, primary_key=True)
    job_id          = Column(Uuid, ForeignKey('jobs.job_id'))
    info            = Column('info', String)

    def __init__(self,job_id, info):
        self.product_id     = uuid.uuid4()
        self.job_id         = job_id
        self.info           = info

    def __repr__(self) -> str:
        return f'Product: {self.product_id} ({self.job_id}) ({self.info})'
    