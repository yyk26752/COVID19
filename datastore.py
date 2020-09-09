from app import db, migrate


class Details(db.Model):
    __tablename__ = "details"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    update_time = db.Column(db.DATETIME)
    province = db.Column(db.VARCHAR(50))
    city = db.Column(db.VARCHAR(50))
    nowConfirm = db.Column(db.Integer)
    confirm = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    dead = db.Column(db.Integer)


class Province(db.Model):
    __tablename__ = "province"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    update_time = db.Column(db.DATETIME)
    province = db.Column(db.VARCHAR(50))
    nowConfirm = db.Column(db.Integer)
    confirm = db.Column(db.Integer)


class History(db.Model):
    __tablename__ = "history"

    time = db.Column(db.DATETIME, primary_key=True, nullable=False, index=True)
    confirm = db.Column(db.Integer)
    confirm_add = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    heal_add = db.Column(db.Integer)
    dead = db.Column(db.Integer)
    dead_add = db.Column(db.Integer)
    nowConfirm = db.Column(db.Integer)
    nowConfirm_add = db.Column(db.Integer)
    noInfect = db.Column(db.Integer)
    noInfect_add = db.Column(db.Integer)
    importedCase = db.Column(db.Integer)
    importedCase_add = db.Column(db.Integer)

class ProvinceHistory(db.Model):
    __tablename__ = "province_history"

    time = db.Column(db.DATETIME, primary_key=True)
    province = db.Column(db.VARCHAR(50))
    confirm = db.Column(db.Integer)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
