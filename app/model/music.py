from sqlalchemy import ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base import Base




class Music(Base):
    __tablename__ = 'Music'
    # mno : 음악번호
    mno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(50))# 제목
    singer: Mapped[str] = mapped_column(String(20))# 가수
    year: Mapped[int] # 발매년도
    genre: Mapped[str] = mapped_column(String(20))# 장르
    country :Mapped[str] = mapped_column(String(20))# 국가유형 (Jpop/Kpop/Pop)
    ment: Mapped[str] = mapped_column(Text)# 앨범소개
    iname: Mapped[str] = mapped_column(String(50))# 이미지이름
    fname: Mapped[str] = mapped_column(String(50))# 파일이름

class MusicVideo(Base):
    __tablename__ = 'Musicvideo'
    # mvno : MV번호
    mvno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    lyrics: Mapped[str] = mapped_column(Text)# 가사
    iname: Mapped[str] = mapped_column(String(50))# 이미지이름
    fname: Mapped[str] = mapped_column(String(50))# 파일이름

class Storage(Base):
    __tablename__ = 'storage'
    # sno : 보관함 번호
    sno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    userid: Mapped[str] = mapped_column(String(20),ForeignKey('member.userid')) # Member의 userid
    mno: Mapped[int] = mapped_column(ForeignKey('Music.mno'), index=True) # Music의 mno
    music = relationship("Music")
