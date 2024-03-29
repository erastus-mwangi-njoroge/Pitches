from app.models import Comment,User,Pitch
from app import db
import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_moringa = User(username = 'moringa',password = 'db1234', email = 'moringa@ms.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='This is a test pitch',category="interview",user = self.user_moringa,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_moringa,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_moringa)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
        
    try:
        
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()  # optional, depends on use case