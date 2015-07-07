

# Fullstack Project 2 - Tournament

## Files
* tournament.py
* tournament.sql
* tournament_test.py

## Requirements
You will need to have vagrant and virtual box installed, for instructions on vagrant go to [install vagrant](https://www.vagrantup.com/) for instruction on virtual box go to [install virtual box](https://www.virtualbox.org/).
You will also need [postresql](https://wiki.postgresql.org/wiki/Detailed_installation_guides) and [psycopg2](https://pypi.python.org/pypi/psycopg2)


## Steps

1. Launch virtual box
2. cd to this repo
3. Launch vagrant ``` vagrant up```
4. Log into vagrant ``` vagrant ssh```
5. CD to the corresponding directory ``` cd /vagrant/tournament ```
6. Prep commandline to insert queries ``` psql```
7. Insert the tables ``` \i tournament.sql```
8. Exit psql ``` \q ```
9. Run the tests ``` python tournament_test.py```

You should see the following output <br>
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```
