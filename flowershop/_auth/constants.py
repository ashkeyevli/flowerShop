USER_ROLE_ADMIN = 1
USER_ROLE_MANAGER = 2
USER_ROLE_CUSTOMER = 3
USER_ROLES = (
    (USER_ROLE_ADMIN, 'Admin'),
    (USER_ROLE_MANAGER, 'Manager'),
    (USER_ROLE_CUSTOMER, 'Customer'),
)

CUSTOMER_ROLE_ORDINARY = 1
CUSTOMER_ROLE_VIP = 2
CUSTOMER_ROLES = (
    (CUSTOMER_ROLE_ORDINARY, 'Ordinary'),
    (CUSTOMER_ROLE_VIP, 'VIP Client')
)
