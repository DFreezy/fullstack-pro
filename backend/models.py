from app import db

class Friend(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(200), nullable=True)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "role":self.role,
            "description":self.description,
            "gender":self.gender,
            "imgurl":self.img_url,
        }
    