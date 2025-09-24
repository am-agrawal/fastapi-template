from db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)


class SurveyQuestion(Base):
    __tablename__ = "survey_questions"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    question_text = Column(String, nullable=False)
    question_type = Column(String, nullable=False)
    required = Column(Boolean, default=False)
    options = Column(String, nullable=True)


class SurveyResponse(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    submitted_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)


class SurveyAnswer(Base):
    __tablename__ = "survey_answers"

    id = Column(Integer, primary_key=True, index=True)
    response_id = Column(Integer, ForeignKey("survey_responses.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("survey_questions.id"), nullable=False)
    answer_text = Column(String, nullable=True)
    selected_option = Column(String, nullable=True)