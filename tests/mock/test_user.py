import datetime, pytest
from ad_leavers.models.data_classes.user import User

class TestUser:

    testdata = [
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'sAMAccountName': 'eren.yeager',    
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2023, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 10, 23, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 2, 23, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            True
        ),
    ]
    @pytest.mark.parametrize("schema,expected_result", testdata)
    def test_is_eligible_to_disable(self, schema, expected_result):
        
        # * Arrange
        user = User(schema=schema)

        # * Act
        try:
            
            result = user.is_eligible_for_deletion(days_limit=90)

        except Exception as e:

            result = str(e)

        # * Assert
        assert result == expected_result

    testdata = [
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'0'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(1601, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2023, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            False
        ),
        (
            {
                'raw_attributes':{
                    'accountExpires': [b'1'],
                },
                'attributes': {
                    'description': ['10/25/2022'],
                    'distinguishedName': 'CN=Eren Yeager,OU=Leavers,OU=Users,OU=checkoutaws,DC=checkoutaws,DC=local',
                    'whenCreated': datetime.datetime(2022, 1, 15, 17, 25, 18, tzinfo = datetime.timezone.utc),
                    'memberOf': ['CN=Domain Admins,CN=Users,DC=checkoutaws,DC=local'],
                    'name': 'Eren Yeager',
                    'accountExpires': datetime.datetime(2022, 1, 1, 0, 0, tzinfo = datetime.timezone.utc),
                    'sAMAccountName': 'eren.yeager',    
                    'userPrincipalName': 'eren.yeager@checkoutaws.local',
                    'displayName': 'Eren Yeager',
                }
            },
            True
        ),
    ]
    @pytest.mark.parametrize("schema,expected_result", testdata)
    def test_is_eligible_for_deletion(self, schema, expected_result):
        
        # * Arrange
        user = User(schema=schema)

        # * Act
        try:
            
            result = user.is_eligible_to_disable()

        except Exception as e:

            result = str(e)

        # * Assert
        assert result == expected_result