from datetime import datetime, timedelta
import os
from ad_leavers.user_operations import UserOps
from ad_leavers.models.data_classes.user import User

class TestUserOps:
    
    # > Define global variables
    host_servers = os.environ['HOST_SERVERS'].split(',')
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']

    # def test_disable_user(self):
        
    #     # * Arrange
    #     search_base = "OU=Leavers,OU=Users,OU=cko,DC=cko,DC=test"
    #     sam_name = "eren.yeager"
        
    #     # * Act

    #     try:

    #         user_ops = UserOps(
    #             hosts=self.host_servers,
    #             username=self.username,
    #             password=self.password,
    #         )

    #         # * Search for the user
    #         user = user_ops.deep_single_search(search_base=search_base, sam_name=sam_name)

    #         # * Set expiration on user
    #         user_ops.disable(
    #             distinguished_name=user.distinguished_name
    #         )

    #         results = "Passed"

    #     except Exception as e:

    #         results = f"Failed"

    #     print(f"Connection: {user_ops.connection}")
    #     print(f"Results: {results}")

    #     # * Assert
    #     assert False

    # def test_set_expiration(self):
        
    #     # * Arrange
    #     search_base = "OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local"
    #     sam_name = "eren.yeager"
    #     expiration_date = datetime.today() + timedelta(days=10)
        
    #     # * Act

    #     try:

    #         user_ops = UserOps(
    #             hosts=self.host_servers,
    #             username=self.username,
    #             password=self.password,
    #         )

    #         # * Search for the user
    #         user = user_ops.deep_single_search(search_base=search_base, sam_name=sam_name)

    #         # * Set expiration on user
    #         user_ops.set_expiration(
    #             distinguished_name=user.distinguished_name,
    #             expiration_date=expiration_date
    #         )

    #         results = "Passed"

    #     except Exception as e:

    #         results = f"Failed"

    #     print(f"Connection: {user_ops.connection}")
    #     print(f"Results: {results}")
    #     print(f"Expiration date: {expiration_date}")

    #     # * Assert
    #     assert False

    # def test_get_all(self):
        
    #     # * Arrange
    #     search_base = "OU=Leavers,OU=Users,OU=cko,DC=cko,DC=test"

    #     # * Act
    #     user_ops = UserOps(
    #         hosts=self.host_servers,
    #         username=self.username,
    #         password=self.password,
    #     )

    #     users = user_ops.get_all(search_base=search_base)

    #     print(f"Connection: {user_ops.connection}")
    #     print(f"Users: {[user.name for user in users]}")

    #     # * Assert
    #     assert False
    
    # def test_get(self):
        
    #     # * Arrange
    #     #search_base = "OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local"
    #     search_base = "OU=Leavers,OU=Users,OU=cko,DC=cko,DC=test"
    #     unique_identifier = "eren.yeager"

    #     # * Act
    #     user_ops = UserOps(
    #         hosts=self.host_servers,
    #         username=self.username,
    #         password=self.password,
    #     )

    #     user: User = user_ops.deep_single_search(search_base=search_base, unique_identifier=unique_identifier)

    #     print(f"Connection: {user_ops.connection}")
    #     print(f"User: {user.name}")

    #     # * Assert
    #     assert False

    # def test_delete(self):
        
    #     # * Arrange
    #     dn = "CN=Erwin Smith,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local"

    #     # * Act
    #     try:

    #         user_ops = UserOps(
    #             hosts=self.host_servers,
    #             username=self.username,
    #             password=self.password,
    #         )

    #         user_ops.delete(
    #             distinguished_name=dn
    #         )

    #         results = "Passed"

    #     except Exception as e:

    #         results = "Failed"

    #     print(f"Connection: {user_ops.connection}")
    #     print(f"Results: {results}")

    #     # * Assert
    #     assert False

    # def test_move(self):
        
    #     # * Arrange
    #     new_ou = "OU=USA, OU=Checkout Users,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local"
    #     cn = "Eren Yeager"
    #     dn = "CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local"

    #     # * Act
    #     try:

    #         user_ops = UserOps(
    #             hosts=self.host_servers,
    #             username=self.username,
    #             password=self.password,
    #         )

    #         user_ops.move(
    #             distinguished_name=dn,
    #             cn=cn,
    #             new_ou=new_ou
    #         )

    #         results = "Passed"

    #     except Exception as e:

    #         results = "Failed"

    #     print(f"Connection: {user_ops.connection}")
    #     print(f"Results: {results}")

    #     # * Assert
    #     assert False