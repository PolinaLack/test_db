from repository.Defects import DefectsCRUD
from repository.Workers import WorkersCRUD
from start_session import curr_session

with curr_session as session:
    crud = DefectsCRUD(session)

    new_defect = crud.create(
        defect="defect", name_of_works="name_of_works", unit="unit", number=1)

    print(crud.read(new_defect.id))

    updated_defect = crud.update(new_defect.id, number=456)
    print(f"Updated: {updated_defect}")

    deleted_defect = crud.delete(new_defect.id)
    print(f"Deleted: {deleted_defect}")

#############################

    crud = WorkersCRUD(session)
    
    new_worker = crud.create(
        worker=1, lastname="lastname", firstname="firstname", surname="surname", sheet_amount=1)

    print(crud.read(new_worker.id))

    updated_defect = crud.update(new_worker.id, firstname="not_firstname")
    print(f"Updated: {updated_defect}")

    deleted_defect = crud.delete(new_worker.id)
    print(f"Deleted: {deleted_defect}")