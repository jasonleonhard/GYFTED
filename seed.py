"""Seed some data."""

from models import db, Ticket

# full examples
t1 = Ticket(item='13 hat assorted colors', deliverer='Bonnie', gyfter='Ashika',
            pickup_address='smith memorial', pickup_time='11am',
            pickup_date='11/11/17', requester='Jason',
            dropoff_address='pioneer square', dropoff_time='11pm',
            dropoff_date='11/11/17')

t2 = Ticket(item='11 coats assorted colors', deliverer='Michael',
            gyfter='Jason', pickup_address='pioneer square', pickup_time='9am',
            pickup_date='11/12/17', requester='Ashika',
            dropoff_address='smith memorial', dropoff_time='11am',
            dropoff_date='11/12/17')

t3 = Ticket(item='3 pairs size 11 womens shoes', deliverer='Jason',
            gyfter='Michael',
            pickup_address='US Bank Tower, Southwest 4th Avenue, Portland, OR',
            pickup_time='11am', pickup_date='11/11/17', requester='Jason',
            dropoff_address='pioneer square', dropoff_time='11pm',
            dropoff_date='11/11/17')

t4 = Ticket(item='a partridge in a pear tree', deliverer='Ashika',
            gyfter='Bonnie', pickup_address='The fields Park',
            pickup_time='9am', pickup_date='11/12/17', requester='Ashika',
            dropoff_address='Providence Park', dropoff_time='11am',
            dropoff_date='11/12/17')

# examples with fields intentiallly left blank
t5 = Ticket(item='a nice warm L mens winter coat black', deliverer='',
            gyfter='Jason', pickup_address='Clinton Street Theater',
            pickup_time='10pm', pickup_date='12/12/17', requester='',
            dropoff_address='', dropoff_time='',
            dropoff_date='')

t6 = Ticket(item='a blue L mens tucker hat', deliverer='',
            gyfter='', pickup_address='The fields Park',
            pickup_time='', pickup_date='', requester='Michael',
            dropoff_address='Providence Park', dropoff_time='8pm',
            dropoff_date='1/11/18')

# user1 = User(username='admin', password='admin')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)
db.session.add(t5)
db.session.add(t6)
db.session.add(user1)
db.session.commit()
tickets = Ticket.query.all()
donated_by_jason = Ticket.query.filter_by(gyfter='Jason').first()

print(tickets)
print(donated_by_jason)
