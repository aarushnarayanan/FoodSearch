from sqlalchemy import Column, Text, Double, SmallInteger, Boolean, Integer, Float, TIMESTAMP, BigInteger, ARRAY, JSON, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Place(Base):
    __tablename__ = "places"

    place_id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    address = Column(Text)
    lat = Column(Double, nullable=False)
    lng = Column(Double, nullable=False)
    cuisine_tags = Column(ARRAY(Text))
    price_level = Column(SmallInteger)
    phone = Column(Text)
    hours = Column(JSON)
    google_rating = Column(Float)
    google_ratings_count = Column(Integer)
    is_sponsored = Column(Boolean, default=False)
    first_seen_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    last_updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    metadata_cached_at = Column(TIMESTAMP(timezone=True))


class Mention(Base):
    __tablename__ = "mentions"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    reddit_post_id = Column(Text, nullable=False)
    reddit_comment_id = Column(Text)
    subreddit = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    author_account_age_days = Column(Integer)
    author_karma = Column(Integer)
    raw_text = Column(Text, nullable=False)
    extracted_name = Column(Text, nullable=False)
    resolved_place_id = Column(Text)
    resolution_confidence = Column(Float)
    needs_manual_review = Column(Boolean, default=False)
    upvotes = Column(Integer, nullable=False)
    sentiment_score = Column(Float)
    is_shill_suspected = Column(Boolean, default=False)
    posted_at = Column(TIMESTAMP(timezone=True), nullable=False)
    ingested_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("reddit_post_id", "reddit_comment_id", "extracted_name"),
    )


class Score(Base):
    __tablename__ = "scores"

    place_id = Column(Text, primary_key=True)
    reddit_mention_count = Column(Integer, nullable=False)
    reddit_sentiment_avg = Column(Float, nullable=False)
    commenter_trust_score = Column(Float, nullable=False)
    recency_score = Column(Float, nullable=False)
    longevity_score = Column(Float, nullable=False)
    sponsored_penalty = Column(Float, nullable=False)
    local_trust_score = Column(Float, nullable=False)
    computed_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


class ResolutionCache(Base):
    __tablename__ = "resolution_cache"

    extracted_name_normalized = Column(Text, primary_key=True)
    city = Column(Text, primary_key=True)
    resolved_place_id = Column(Text)
    confidence = Column(Float)
    resolved_at = Column(TIMESTAMP(timezone=True), server_default=func.now())