from create_tables import Workers


class WorkersCRUD:
    def __init__(self, session):
        self.session = session


    def create(self, worker, lastname, firstname, surname, sheet_amount):
        new_record = Workers(
            worker=int(worker),
            lastname=lastname,
            firstname=firstname,
            surname=surname,
            sheet_amount=int(sheet_amount)
            ) 
        self.session.add(new_record)
        self.session.commit()
        return new_record
    
    
    def read(self, record_id):
        return self.session.query(Workers).filter_by(id=record_id).first()
    
    
    def update(self, record_id, **kwargs):
        record = self.session.query(Workers).filter_by(id=record_id).first()
        if record:
            for key, value in kwargs.items():
                setattr(record, key, value)
            self.session.commit()
        return record


    def delete(self, record_id):
        record = self.session.query(Workers).filter_by(id=record_id).first()
        if record:
            self.session.delete(record)
            self.session.commit()
        return record