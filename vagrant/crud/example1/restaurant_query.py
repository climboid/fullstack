from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


def get_restaurants():
	restaurants = []
	for instance in session.query(Restaurant):
		restaurants.append(instance)

	return restaurants

def add_restaurant(restaurant):
	restaurant = Restaurant(name=restaurant)
	session.add(restaurant)
	session.commit()
	return

def get_restaurant(id):
	restaurant = session.query(Restaurant).filter_by(id=id).one()
	return restaurant

def edit_restaurant(restaurant):
	print "in edit_restaurant"
	session.add(restaurant)
	session.commit()
	return

def delete_restaurant(restaurant):
	print restaurant
	session.delete(restaurant)
	session.commit()
	return



