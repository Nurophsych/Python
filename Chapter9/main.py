from pg211 import Resturants as r
from pg211 import Admin as a

my_resturant = r("Chris P Bacon", 'Pork based')

my_resturant.open_resturant()
my_resturant.description()

print()
print()
print()

new_admin = a('Tom', 'Riddle', 17, '33 Bogrider lane')

new_admin.user_info()
new_admin.show_priv()

print()
print()
print()

admin_user = a("Alice", "Smith", "admin_alice", "alice.smith@example.com")

admin_user.show_priv()

