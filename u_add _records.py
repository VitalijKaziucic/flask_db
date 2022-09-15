from models import db, Message

# db.create_all()


# jonas = Message("Jonas", "jonas@ev.lt", "Žinutė iš Jono")
# paulius = Message("Paulius", "paulius@ev.lt", "Žinutė iš Pauliaus")
# povilas = Message("Povilas", "povilas@ev.lt", "Žinutė iš Povilo")
# rapolas = Message("Rapolas", "rapolas@ev.lt", "Žinutė iš Rapolo")


# db.session.add_all([jonas, paulius, povilas, rapolas])
# db.session.commit()


find = Message.query.filter(Message.name == "Paulius").first()
print(find)
# find.message = "Sveikas, kaip einasi"
# print(db.session.dirty)
# db.session.commit()
# db.session.delete(find)
# print(db.session.dirty)
# db.session.commit()
