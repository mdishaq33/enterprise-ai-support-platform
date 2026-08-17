import random
from datetime import datetime, timedelta
import mysql.connector


# ============================================================
# 1. DATABASE CONNECTION
# ============================================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anas@786",
    database="enterprise_support"
)

print("Connected to MySQL successfully!")


# ============================================================
# 2. CATEGORY MAPPING
# ============================================================

CATEGORY_IDS = {
    "Network": 1,
    "Email": 2,
    "Authentication": 3,
    "Hardware": 4,
    "Software": 5,
    "Database": 6,
    "Cloud": 7,
    "Security": 8,
    "Application": 9,
    "Access Management": 10
}


# ============================================================
# 3. TICKET SCENARIOS
# ============================================================

TICKET_SCENARIOS = {

    "Network": {
        "service_id": 1,
        "scenarios": [
            (
                "VPN not connecting",
                "I am unable to connect to the company VPN. The connection fails during authentication."
            ),
            (
                "VPN keeps disconnecting",
                "The VPN connection disconnects every few minutes while I am working remotely."
            ),
            (
                "Slow network connection",
                "The network connection is extremely slow and internal applications are taking a long time to load."
            ),
            (
                "Unable to access internal server",
                "I cannot access an internal company server even though my internet connection is working."
            )
        ]
    },

    "Email": {
        "service_id": 2,
        "scenarios": [
            (
                "Outlook not syncing",
                "Outlook is open but new emails are not appearing in my mailbox."
            ),
            (
                "Unable to send email",
                "I am unable to send emails and Outlook keeps showing a send error."
            ),
            (
                "Unable to receive email",
                "Incoming emails are not being delivered to my mailbox."
            ),
            (
                "Mailbox is full",
                "I received a notification that my mailbox has reached its storage limit."
            )
        ]
    },

    "Authentication": {
        "service_id": 1,
        "scenarios": [
            (
                "Unable to login",
                "I am entering the correct credentials but the system says authentication failed."
            ),
            (
                "MFA verification failing",
                "The multi-factor authentication code is not being accepted."
            ),
            (
                "Account locked",
                "My account has been locked after several unsuccessful login attempts."
            ),
            (
                "Password expired",
                "The system says my password has expired and I cannot log in."
            )
        ]
    },

    "Hardware": {
        "service_id": 8,
        "scenarios": [
            (
                "Laptop not starting",
                "My company laptop is not turning on when I press the power button."
            ),
            (
                "Keyboard not working",
                "Several keys on my laptop keyboard have stopped responding."
            ),
            (
                "Monitor not displaying",
                "My external monitor is connected but the screen remains blank."
            )
        ]
    },

    "Software": {
        "service_id": 11,
        "scenarios": [
            (
                "Application installation failed",
                "I tried to install the required software but the installation keeps failing."
            ),
            (
                "Application crashing",
                "The application closes unexpectedly whenever I try to open it."
            ),
            (
                "Software update failed",
                "The latest software update failed and the application is not working correctly."
            )
        ]
    },

    "Database": {
        "service_id": 5,
        "scenarios": [
            (
                "Database connection timeout",
                "The application is reporting a database connection timeout."
            ),
            (
                "Database unavailable",
                "The database service appears to be unavailable and applications cannot connect."
            ),
            (
                "Slow database query",
                "A database query that normally completes quickly is now taking several minutes."
            )
        ]
    },

    "Cloud": {
        "service_id": 9,
        "scenarios": [
            (
                "Cloud storage unavailable",
                "I cannot access the company's cloud storage service."
            ),
            (
                "Cloud deployment failed",
                "The latest application deployment to the cloud failed."
            ),
            (
                "Cloud service timeout",
                "The cloud service is responding very slowly and frequently times out."
            )
        ]
    },

    "Security": {
        "service_id": 10,
        "scenarios": [
            (
                "Suspicious login detected",
                "I received an alert about a login to my account from an unknown location."
            ),
            (
                "Possible phishing email",
                "I received a suspicious email asking me to provide my company credentials."
            ),
            (
                "Unauthorized access attempt",
                "The security system detected an unusual attempt to access a company application."
            )
        ]
    },

    "Application": {
        "service_id": 3,
        "scenarios": [
            (
                "CRM not loading",
                "The CRM application is not loading and shows a connection timeout."
            ),
            (
                "CRM application error",
                "The CRM displays an unexpected error when I try to open a customer record."
            ),
            (
                "CRM performance issue",
                "The CRM application is taking several minutes to load each page."
            )
        ]
    },

    "Access Management": {
        "service_id": 12,
        "scenarios": [
            (
                "Application access required",
                "I recently joined a new team and need access to the required business application."
            ),
            (
                "Permission denied",
                "I have access to the application but I am unable to access a required feature."
            ),
            (
                "Shared folder access",
                "I cannot access the shared folder required for my work."
            )
        ]
    }
}


# ============================================================
# 4. USER GENERATOR
# ============================================================

def generate_user(user_id):

    first_names = [
        "Rahul", "Ayesha", "Arjun", "Sara",
        "Vikram", "Priya", "Aditya", "Neha"
    ]

    last_names = [
        "Sharma", "Khan", "Rao",
        "Patel", "Reddy", "Singh"
    ]

    roles = [
        "employee",
        "employee",
        "employee",
        "employee",
        "support_engineer",
        "admin"
    ]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"

    email = f"user{user_id}@company.com"

    department_id = random.randint(1, 4)

    role = random.choice(roles)

    return {
        "user_id": user_id,
        "name": name,
        "email": email,
        "department_id": department_id,
        "role": role
    }


# ============================================================
# 5. GENERATE MULTIPLE USERS
# ============================================================

def generate_users(count):

    users = []

    for user_id in range(5, count + 5):

        user = generate_user(user_id)

        users.append(user)

    return users


# ============================================================
# 6. INSERT USERS INTO MYSQL
# ============================================================

def insert_users(connection, users):

    cursor = connection.cursor()

    query = """
        INSERT INTO users
        (user_id, name, email, department_id, role, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = []

    for user in users:

        values.append((
            user["user_id"],
            user["name"],
            user["email"],
            user["department_id"],
            user["role"],
            "2026-08-11 18:00:00"
        ))

    cursor.executemany(query, values)

    connection.commit()

    print(f"{cursor.rowcount} users inserted successfully!")

    cursor.close()


# ============================================================
# 7. GENERATE ONE TICKET
# ============================================================

from datetime import datetime, timedelta


def generate_ticket(ticket_id):

    # Choose a category
    category_name = random.choice(
        list(TICKET_SCENARIOS.keys())
    )

    category_id = CATEGORY_IDS[category_name]

    # Choose a problem scenario
    scenario = random.choice(
        TICKET_SCENARIOS[category_name]["scenarios"]
    )

    title, description = scenario

    # Generate a realistic creation time
    created_at = datetime(
        2026,
        8,
        random.randint(1, 11),
        random.randint(8, 18),
        random.randint(0, 59)
    )

    # Choose priority
    priority = random.choices(
        ["low", "medium", "high", "critical"],
        weights=[15, 40, 35, 10],
        k=1
    )[0]

    # Choose status
    status = random.choices(
        ["open", "in_progress", "resolved"],
        weights=[30, 30, 40],
        k=1
    )[0]

    # Updated time
    updated_at = created_at + timedelta(
        minutes=random.randint(5, 240)
    )

    # Incident relationship
    incident_id = None

    # Resolved tickets get a resolution time
    resolved_at = None

    if status == "resolved":

        resolved_at = updated_at

    return {
        "ticket_id": ticket_id,
        "user_id": random.randint(2, 504),
        "service_id": TICKET_SCENARIOS[category_name]["service_id"],
        "category_id": category_id,
        "incident_id": incident_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": status,
        "created_at": created_at,
        "updated_at": updated_at,
        "resolved_at": resolved_at
    }


# ============================================================
# 8. TEST ONE TICKET
# ============================================================


def generate_tickets(count, start_id=1000):

    tickets = []

    for ticket_id in range(start_id, start_id + count):

        ticket = generate_ticket(ticket_id)

        tickets.append(ticket)

    return tickets

def insert_tickets(connection, tickets):

    cursor = connection.cursor()

    query = """
        INSERT INTO tickets
        (
            ticket_id,
            user_id,
            service_id,
            category_id,
            incident_id,
            title,
            description,
            priority,
            status,
            created_at,
            updated_at,
            resolved_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = []

    for ticket in tickets:

        values.append((
            ticket["ticket_id"],
            ticket["user_id"],
            ticket["service_id"],
            ticket["category_id"],
            ticket["incident_id"],
            ticket["title"],
            ticket["description"],
            ticket["priority"],
            ticket["status"],
            ticket["created_at"],
            ticket["updated_at"],
            ticket["resolved_at"]
        ))

    cursor.executemany(query, values)

    connection.commit()

    print(f"{cursor.rowcount} tickets inserted successfully!")

    cursor.close()
# ============================================================
# 9. CLOSE DATABASE CONNECTION
# ============================================================

tickets = generate_tickets(5000, start_id=1000)

print(f"\nTotal tickets generated: {len(tickets)}")

print("\nFirst ticket:")
print(tickets[0])

print("\nLast ticket:")
print(tickets[-1])

insert_tickets(connection, tickets)

connection.close()

print("\nDatabase connection closed.")