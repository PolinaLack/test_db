from create_tables import Defects


class DefectsCRUD:
    def __init__(self, session):
        self.session = session


    def create(self, defect, name_of_works, unit, number):
        new_record = Defects(defect=defect, name_of_works=name_of_works, unit=unit, number=int(number)) 
        self.session.add(new_record)
        self.session.commit()
        return new_record
    
    
    def read(self, record_id):
        return self.session.query(Defects).filter_by(id=record_id).first()
    
    
    def update(self, record_id, **kwargs):
        record = self.session.query(Defects).filter_by(id=record_id).first()
        if record:
            for key, value in kwargs.items():
                setattr(record, key, value)
            self.session.commit()
        return record


    def delete(self, record_id):
        record = self.session.query(Defects).filter_by(id=record_id).first()
        if record:
            self.session.delete(record)
            self.session.commit()
        return record