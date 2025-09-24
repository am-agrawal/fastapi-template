from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, foreign_key="users.id")
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)


class SurveyQuestion(Base):
    __tablename__ = "survey_questions"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, nullable=False, foreign_key="surveys.id")
    question_text = Column(String, nullable=False)
    question_type = Column(String, nullable=False)
    required = Column(Boolean, default=False)
    options = Column(String, nullable=True)


class SurveyResponse(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, nullable=False, foreign_key="surveys.id")
    user_id = Column(Integer, nullable=False, foreign_key="users.id")
    submitted_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)


class SurveyAnswer(Base):
    __tablename__ = "survey_answers"

    id = Column(Integer, primary_key=True, index=True)
    response_id = Column(Integer, nullable=False, foreign_key="survey_responses.id")
    question_id = Column(Integer, nullable=False, foreign_key="survey_questions.id")
    answer_text = Column(String, nullable=True)
    selected_option = Column(String, nullable=True)