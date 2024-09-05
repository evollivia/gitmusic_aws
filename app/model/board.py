from datetime import datetime
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.model.base import Base


# 게시판 테이블
class Board(Base):
    __tablename__ = 'board'
    # __table_args__ = {'sqlite_autoincrement': True}

    bno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(30), index=True)
    userid: Mapped[str] = mapped_column(String(20),ForeignKey('member.userid')) # Member의 userid
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str] = mapped_column(Text)

    files = relationship("BoardFile", back_populates="board")
    replys = relationship('Reply', back_populates='board')


# 게시판 파일업로드 테이블
class BoardFile(Base):
    __tablename__ = 'boardfile'
    fno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    bno: Mapped[int] = mapped_column(ForeignKey('board.bno'), index=True)
    fname: Mapped[str] = mapped_column(String(50),nullable=False)
    fsize: Mapped[int] = mapped_column(default=0)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    board = relationship("Board", back_populates="files")

# 게시판 댓글
class Reply(Base):
    __tablename__ = 'reply'

    rno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    reply: Mapped[str] = mapped_column(String(250),index=True)
    userid: Mapped[str] = mapped_column(String(20),ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=lambda: datetime.now().replace(microsecond=0))
    bno: Mapped[int] = mapped_column(ForeignKey('board.bno'))
    rpno: Mapped[int] = mapped_column(ForeignKey('reply.rno'),nullable=True)
    board = relationship('Board', back_populates='replys')
    # 댓글과 대댓글
    parent = relationship('Reply', remote_side=[rno], backref='children')
